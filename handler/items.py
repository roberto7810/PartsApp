from flask import jsonify
from dao.parts import ItemsDAO


class ItemHandler:
    def build_item_dict(self, row):
        result = {}
        return result

    def build_person_dict(self, row):
        result = {}
        return result

    def build_part_attributes(self, item_id, resource_name, brand, item_latitude, item_longitude, expiration_date, price, type, amount):
        result = {}
        return result

    def getAllItems(self):
        dao = ItemsDAO()
        items_list = dao.getAllItems()
        result_list = []
        for row in items_list:
            result = self.build_item_dict(row)
            result_list.append(result)
        return jsonify(Items=result_list)

    def getItemById(self, item_id):
        dao = ItemsDAO()
        row = dao.getPartById(item_id)
        if not row:
            return jsonify(Error = "Item Not Found"), 404
        else:
            item = self.build_part_dict(row)
            return jsonify(Item = item)

##################################################################
    def searchItems(self, args):
        typeOfItem = args.get("type")
        resourceName = args.get("resourceName")
        dao = ItemsDAO()
        items_list = []
        if (len(args) == 2) and typeOfItem and resourceName:
            items_list = dao.getPartsByColorAndMaterial(typeOfItem, resourceName)
        elif (len(args) == 1) and typeOfItem:
            items_list = dao.getPartsByColor(typeOfItem)
        elif (len(args) == 1) and resourceName:
            items_list = dao.getPartsByMaterial(resourceName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in items_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getSuppliersByPId(self, pid):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = dao.getSuppliersByPartId(pid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertItem(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            itemResourceName = form['Item Resource Name']
            iprice = form['item price']
            itype = form['item type']
            ibrand = form['item brand']
            if ibrand and iprice and itype and itemResourceName:
                dao = PartsDAO()
                pid = dao.insert(itemResourceName, ibrand, itype, iprice)
                result = self.build_part_attributes(pid, itemResourceName, ibrand, itype, iprice)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertItemJson(self, json):
        itemResourceName = json['Item Resource Name']
        iprice = json['item price']
        itype = json['item type']
        ibrand = json['item brand']
        if ibrand and iprice and itype and itemResourceName:
            dao = PartsDAO()
            pid = dao.insert(itemResourceName, ibrand, itype, iprice)
            result = self.build_part_attributes(pid, itemResourceName, ibrand, itype, iprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteItem(self, pid):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePart(self, pid, form):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                itemResourceName = form['Item Resource Name']
                iprice = form['item price']
                itype = form['item type']
                ibrand = form['item brand']
                if ibrand and iprice and itype and itemResourceName:
                    dao.update(pid, itemResourceName, ibrand, itype, iprice)
                    result = self.build_part_attributes(pid, itemResourceName, ibrand, itype, iprice)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_part_counts(self, part_counts):
        result = []
        #print(part_counts)
        for P in part_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByPartId(self):
        dao = PartsDAO()
        result = dao.getCountByPartId()
        #print(self.build_part_counts(result))
        return jsonify(PartCounts = self.build_part_counts(result)), 200




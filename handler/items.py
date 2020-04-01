from flask import jsonify
from dao.parts import ItemsDAO


class ItemHandler:
    def build_item_dict(self, row):
        result = {}
        result['item_id'] = row[0]
        result['resource_name'] = row[1]
        result['brand'] = row[2]
        result['item_latitud'] = row[3]
        result['item_longitud'] = row[4]
        result['expiration_date'] = row[5]
        result['price'] = row[6]
        result['type'] = row[7]
        result['amount'] = row[8]
        return result

    def build_person_dict(self, row):
        result = {}
        result['person_id'] = row[0]
        result['person_name'] = row[1]
        result['person_latitud'] = row[2]
        result['person_longitud'] = row[3]
        result['phone_num'] = row[4]
        result['card'] = row[5]
        result['gender'] = row[6]
        result['age'] = row[7]
        return result

    def build_part_attributes(self, item_id, resource_name, brand, item_latitud, item_longitud, expiration_date, price, type, amount):
        result = {}
        result['item_id'] = item_id
        result['resource_name'] = resource_name
        result['brand'] = brand
        result['item_latitud'] = item_latitud
        result['item_longitud'] = item_longitud
        result['expiration_date'] = expiration_date
        result['price'] = price
        result['type'] = type
        result['amount'] = amount
        return result

    def getAllItems(self):
        dao = ItemsDAO()
        parts_list = dao.getAllItems()
        result_list = []
        for row in parts_list:
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
        color = args.get("color")
        material = args.get("material")
        dao = ItemsDAO()
        parts_list = []
        if (len(args) == 2) and color and material:
            parts_list = dao.getPartsByColorAndMaterial(color, material)
        elif (len(args) == 1) and color:
            parts_list = dao.getPartsByColor(color)
        elif (len(args) == 1) and material:
            parts_list = dao.getPartsByMaterial(material)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in parts_list:
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

    def insertPart(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            pname = form['pname']
            pprice = form['pprice']
            pmaterial = form['pmaterial']
            pcolor = form['pcolor']
            if pcolor and pprice and pmaterial and pname:
                dao = PartsDAO()
                pid = dao.insert(pname, pcolor, pmaterial, pprice)
                result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertPartJson(self, json):
        pname = json['pname']
        pprice = json['pprice']
        pmaterial = json['pmaterial']
        pcolor = json['pcolor']
        if pcolor and pprice and pmaterial and pname:
            dao = PartsDAO()
            pid = dao.insert(pname, pcolor, pmaterial, pprice)
            result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePart(self, pid):
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
                pname = form['pname']
                pprice = form['pprice']
                pmaterial = form['pmaterial']
                pcolor = form['pcolor']
                if pcolor and pprice and pmaterial and pname:
                    dao.update(pid, pname, pcolor, pmaterial, pprice)
                    result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
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




from flask import jsonify
from dao.supplier import PersonDAO


class RequestorHandler:
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

    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllSuppliers(self):

        dao = PersonDAO()
        suppliers_list = dao.getAllPersons()
        result_list = []
        for row in suppliers_list:
            result = self.build_person_dict(row)
            result_list.append(result)
        return jsonify(persons=result_list)

    def getSupplierById(self, sid):

        dao = PersonDAO()

        row = dao.getPersonById(sid)
        if not row:
            return jsonify(Error="person Not Found"), 404
        else:
            item = self.build_person_dict(row)
        return jsonify(Item=item)

    def getPartsBySupplierId(self, sid):
        dao = PersonDAO()
        if not dao.getPersonById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        parts_list = dao.getItemsBySupplierId(sid)
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(PartsSupply=result_list)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            city = args.get("city")
            if city:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByCity(city)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(row)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, form):
        if form and len(form) == 3:
            sname = form['sname']
            scity = form['scity']
            sphone = form['sphone']
            if sname and scity and sphone:
                dao = SupplierDAO()
                sid = dao.insert(sname, scity, sphone)
                result = {}
                result["sid"] = sid
                result["sname"] = sname
                result["scity"] = scity
                result["sphone"] = sphone
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")



from purview_py.controller.type.Attribute import PurviewAttribute, PurviewRelationshipAttribute
from datetime import datetime
import requests, json, uuid, pprint


class PurviewType(object):
    
    def __init__(self, category, name, superTypes, subTypes=[], guid=str(uuid.uuid4()), createdBy="purview_py", updatedBy="purview_py", createTime=datetime.now(), updateTime=datetime.now(), version=2, description="", typeVersion="1.0", options={}, lastModifiedTS=None, attributeDefs=[], relationshipAttributeDefs=[], serviceType=None, newType=False):
        self.guid = guid
        self.category = category
        self.createdBy = createdBy
        self.updatedBy = updatedBy
        self.createTime = createTime
        self.updateTime = updateTime
        self.version = version
        self.name = name
        self.description = description
        self.typeVersion = typeVersion
        self.serviceType = serviceType
        self.options = options
        self.lastModifiedTS = lastModifiedTS
        self.attributeDefs = attributeDefs
        self.superTypes = superTypes
        self.subTypes = subTypes
        self.relationshipAttributeDefs = relationshipAttributeDefs
        self.newType = newType

    @classmethod
    def getTypeByName(cls, conn, name):
        urlheaders = {"Content-Type": "application/json", "Authorization": f"Bearer {conn.auth.return_token()}"}
        response = requests.get(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedef/name/{name}", headers=urlheaders)
        if response.status_code == 200:
            return cls.getClassByJSON(response.json())
        else:
            raise Exception(response.status_code, response.json())

    @classmethod
    def getTypeByGUID(cls, conn, guid):
        urlheaders = {"Content-Type": "application/json", "Authorization": f"Bearer {conn.auth.return_token()}"}
        response = requests.get(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedef/guid/{guid}", headers=urlheaders)
        if response.status_code == 200:
            return cls.getClassByJSON(response.json())
        else:
            raise Exception(response.status_code, response.json())

    @classmethod
    def getClassByJSON(cls, apiresp):
        
        # print(apiresp)
        
        args = dict(apiresp)
        tmpAttributes = []
        tmpRelAttributes = []

        # pp = pprint.PrettyPrinter(indent=4)
        

        for attr in args["attributeDefs"]:
            # pp.pprint(attr)
            tmpAttributes.append(PurviewAttribute(**attr))
        for attr in args["relationshipAttributeDefs"]:
            tmpRelAttributes.append(PurviewRelationshipAttribute(**attr))

        args["attributeDefs"] = tmpAttributes
        args["relationshipAttributeDefs"] = tmpRelAttributes

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(args)

        t = cls(**args, newType=False)
        return t

    def format_for_requests(self):

        attrs = []
        if len(self.attributeDefs) > 0:
            for a in self.attributeDefs:
                attrs.append(vars(a))
        rel_attrs = []
        if len(self.relationshipAttributeDefs) > 0:
            for a in self.relationshipAttributeDefs:
                rel_attrs.append(vars(a))
        new_type_request = vars(self)
        new_type_request["attributeDefs"] = attrs
        new_type_request["relationshipAttributeDefs"] = rel_attrs

        new_type_request.pop('newType', None)

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(requestdata)

        return new_type_request

    def update_def(self):
        pass

        
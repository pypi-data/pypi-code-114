# from purview_py import PurviewType, PurviewEntity, Connection
import pprint, requests


class PurviewController(object):
    """A controller for Purview"""

    def __init__(self):
        pass

    def create_new_types(self, conn, types):
        # Check manditory fields
        # format request
        # post data
        #check response code

        requestdata = {"entityDefs":[], "classificationDefs":[], "structDefs":[], "relationshipDefs":[]}
        pp = pprint.PrettyPrinter(indent=4)
        
        for t in types:
            type_dict = t.format_for_requests()
            type_dict.pop('guid', None)

            pp.pprint(type_dict)

            if type_dict["category"] == "ENTITY":
                requestdata["entityDefs"].append(type_dict)
            if type_dict["category"] == "CLASSIFICATION":
                requestdata["classificationDefs"].append(type_dict)
            if type_dict["category"] == "STRUCT":
                requestdata["structDefs"].append(type_dict)
            if type_dict["category"] == "RELATIONSHIP":
                requestdata["relationshipDefs"].append(type_dict)
            
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(requestdata)

        # Format Request
        r = requests.post(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedefs", headers=conn.headers, json=requestdata)
        print(r.json())
        if r.status_code != 200:
            return f"{r.status_code}: {r.json()}"
        else:
            return r.status_code
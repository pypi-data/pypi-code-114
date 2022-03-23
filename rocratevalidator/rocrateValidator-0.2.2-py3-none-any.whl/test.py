import validate as validate 
import rocrate.rocrate as rocrate
import os
from rocrateValidator.utils import Result as Result
import rocrate.utils as utils
import requests
# v = validate.validate("valid")
# v.validator()

def datetime_valid(dt_str):
    try: 
        datetime.fromisoformat(dt_str)
    except: 
        return False
    return True


def is_downloadable(url):
    """
    Does the url contain a downloadable resourses
    """
    r = requests.get(url,stream=True)
    content_type = r.headers.get('content-type')
    if "text" in content_type.lower(): 
        return False
    if 'html' in content_type.lower(): 
        return False
    return True
def urlFile_updRlt(id_, entity, webbased_result, error_message):
    if is_downloadable(id_):
        try:
            sdDatePublished = utils.get_norm_value(entity, "sdDatePublished")[0]
            if datetime_valid(sdDatePublished):
                webbased_result[id_] = True
            else:
                webbased_result[id_] = [False, error_message["DateError"].format(id_)]
        except IndexError:
            webbased_result[id_] = [False, error_message["DateError"].format(id_)]
    else:
        webbased_result[id_] = [False, error_message["UrlError"].format(id_)]

def dirOnWeb_updRlt(entity, metadata, webbased_result, error_message):
    distribution = utils.get_norm_value(entity, "distribution")
    if distribution != []:
        dis_type = utils.get_norm_value(metadata[distribution[0]], "@type")
        if dis_type[0] !="DataDownload":
            webbased_result[distribution[0]] = [False, error_message["TypeError"].format(distribution[0])]
        else:
            webbased_result[distribution[0]] = True

# def webbased_entity_check(tar_file):
#     """
#     Please check RO-Crate website for more information about web-based data entity.
#     <https://www.researchobject.org/ro-crate/1.1/data-entities.html#web-based-data-entities>
#     """
    
#     NAME = "Web-based data entity check"
#     error_message = {
#         "UrlError": "Semantic Error: Invalid ID at {}. It should be a downloadable url",
#         "DateError": "Semantic Error: Invalid sdDatePublished {} or Not Provided",
#         "TypeError": "Semantic Error: Invalid @type value of {}."
#     }
#     webbased_result = {}
    
#     context, metadata = rocrate.read_metadata(os.path.join(tar_file, "ro-crate-metadata.json"))
    
#     hasPart = utils.get_norm_value(metadata["./"], "hasPart") if utils.get_norm_value(metadata["./"], "@type") == ["Dataset"] else []
#     if hasPart != []:
#     	for entity in hasPart:
#     		try:
#     			type = utils.get_norm_value(metadata[entity], "@type")[0]
#     			id_ = utils.get_norm_value(metadata[entity], "@id")[0]
#     			if type == "File" and utils.is_url(id_):
#     				urlFile_updRlt(id_, metadata[entity], webbased_result, error_message)
#     			elif type == "Dataset":
#     				dirOnWeb_updRlt(metadata[entity], metadata, webbased_result, error_message)
#     		except KeyError:
#     			webbased_result[entity] = [False, error_message["TypeError"].format(entity)]

#     for values in webbased_result.values():
#         if isinstance(values, list):
#             return Result(NAME, code = -1, message = values[1])
    
#     return Result(NAME)
def webbased_entity_check(tar_file):
    """
    Please check RO-Crate website for more information about web-based data entity.
    <https://www.researchobject.org/ro-crate/1.1/data-entities.html#web-based-data-entities>
    """
    
    NAME = "Web-based data entity check"
    error_message = {
        "UrlError": "Semantic Error: Invalid ID at {}. It should be a downloadable url",
        "DateError": "Semantic Error: Invalid sdDatePublished {} or Not Provided",
        "TypeError": "Semantic Error: Invalid @type value of {}."
    }
    webbased_result = {}
    
    context, metadata = rocrate.read_metadata(os.path.join(tar_file, "ro-crate-metadata.json"))
    
    hasPart = utils.get_norm_value(metadata["./"], "hasPart") if utils.get_norm_value(metadata["./"], "@type") == ["Dataset"] else []
    if hasPart != []:
        for entity in hasPart:
            try:
                type = utils.get_norm_value(metadata[entity], "@type")[0]
                id_ = utils.get_norm_value(metadata[entity], "@id")[0]
                if type == "File" and utils.is_url(id_):
                    urlFile_updRlt(id_, metadata[entity], webbased_result, error_message)
                elif type == "Dataset":
                    dirOnWeb_updRlt(metadata[entity], metadata, webbased_result, error_message)
            except KeyError:
                webbased_result[entity] = [False, error_message["TypeError"].format(entity)]

    # for entity in metadata.values():
    #     type = utils.get_norm_value(entity, "@type")[0]
    #     id_ = utils.get_norm_value(entity, "@id")[0]
        
    #     ### update result
    #     if type == "File" and utils.is_url(id_):
    #         urlFile_updRlt(id_, entity, webbased_result, error_message)
    #     elif type == "Dataset":
    #         dirOnWeb_updRlt(entity, metadata, webbased_result, error_message)
    
    for values in webbased_result.values():
        if isinstance(values, list):
            return Result(NAME, code = -1, message = values[1])
    
    return Result(NAME)

# print(datetime_valid("2020-04-09T13:09:21+01:00Z"))
print(webbased_entity_check("valid").message)
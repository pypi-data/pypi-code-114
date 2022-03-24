import validate as validate 
import rocrate.rocrate as rocrate
import os
from rocrateValidator.utils import Result as Result
import rocrate.utils as utils
import requests
# v = validate.validate("valid")
# v.validator()

def url_check(item, entityProp, metadata, result, error_message):
	if utils.is_url(entityProp):
		upd_result(item, entityProp, metadata, result, error_message)
	else:
		if item == "citation":
			result[entityProp] = [False, error_message["IDError"].format(entityProp)]

def get_entity(item, entity, metadata, result, error_message, is_multipleEntity = False, urlVal_required = False):

	"""
	The Boolean is_multipleEntity is to find the further referencing data entity. 
	The urlVal_required is for those data entity requiring the value of specific property is url.
	At this stage, there are only three differnet cases.
	For more generic, more specific situation should be specified.
	"""

	entity_property = utils.get_norm_value(entity, item)
	if entity_property != []:
		for entityProp in entity_property:
			if urlVal_required and not is_multipleEntity:
				url_check(item, entityProp, metadata, result, error_message)
			elif is_multipleEntity:
				upd_result(item, entityProp, metadata, result, error_message, is_multipleEntity = True)
			else:
				upd_result(item, entityProp, metadata, result, error_message)

def upd_result(item, entity_property, metadata, result, error_message, is_multipleEntity = False, urlVal_required = False):
	try:
		referencing_entity = metadata[entity_property]
		type = utils.get_norm_value(referencing_entity, "@type")
		try:
			type = type[0]
			if type == correct_value[item] or type in correct_value[item]:
				result[entity_property] = True
			else:
				result[entity_property] = [False, error_message["TypeError"].format(entity_property)]

			if is_multipleEntity:
				if item == "author" or item == "publisher":
					get_entity("contactPoint", referencing_entity, metadata, result, error_message)
				else:
					get_entity(item, referencing_entity, metadata, result, error_message)

		except IndexError:
			result[entity_property] = [False, error_message["TypeError"].format(entity_property)]
	except KeyError:
		result[entity_property] = [False, error_message["ReferencingError"].format(entity_property)]

def upd_thumbnailRlt(thumbnail, hasFile, thumbnail_result, error_message):
	if thumbnail != []:
		for item in thumbnail:
			if item in hasFile:
				thumbnail_result[item] = True
			else:
				thumbnail_result[item] = [False, error_message["ReferencingError"].format(item)]


def thumbnails_check(tar_file):
	"""

	"""

	NAME =  "Thumbnails check"
	error_message = {
		"ReferencingError": "Semantic Error: Invalid thumbnail {}. The Thumbnail MUST be included in the RO-Crate."
	}
	thumbnail_result = {}

	context, metadata = rocrate.read_metadata(os.path.join(tar_file, "ro-crate-metadata.json"))

	# thumbnails_ = utils.get_norm_value(metadata["https://omeka.uws.edu.au/farmstofreeways/api/items/383"], "thumbnail")
	# print(thumbnails_)
	for entity in metadata.values():
		thumbnail = utils.get_norm_value(entity, "thumbnail")
		hasFile = utils.get_norm_value(entity, "hasFile")
		upd_thumbnailRlt(thumbnail, hasFile, thumbnail_result, error_message)


	for values in thumbnail_result.values():
		if isinstance(values, list):
			return Result(NAME, code = -1, message = values[1])

	return Result(NAME)

# print(datetime_valid("2020-04-09T13:09:21+01:00Z"))
print(thumbnails_check("valid").code)
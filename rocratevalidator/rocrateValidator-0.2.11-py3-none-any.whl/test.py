import rocrate.rocrate as rocrate
import rocrate.utils as utils
from rocrateValidator.utils import Result as Result
import os
import rocrateValidator.workflow_extension as we

def recognisedWkf_upd(extension_set, entity, workflow_result, id_, error_message):
    extension = os.path.splitext(id_)[1]
    if extension in extension_set:
        type = utils.get_norm_value(entity, "@type")
        name = utils.get_norm_value(entity, "name")
        if "File" in type and "SoftwareSourceCode" in type and "ComputationalWorkflow" in type and name != []:
            workflow_result[id_] = True
        else:
            workflow_result[id_] = [False, error_message["TypeError"].format(id_)]

def unrecognisedWfk_upd(type, extension_set, entity, workflow_result, warning_message, error_message):
    extension = os.path.splitext(utils.get_norm_value(entity,"@id")[0])[1]
    if extension not in extension_set:
        if "File" in type and "SoftwareSourceCode" in type:
            workflow_result[utils.get_norm_value(entity, "@id")[0]] = warning_message["UnrecognizedWkf"].format(extension)
        else:
            workflow_result[utils.get_norm_value(entity, "@id")[0]] = [False, error_message["TypeError"].format(utils.get_norm_value(entity, "@id")[0])]

def scripts_and_workflow_check(tar_file):
    
    """
    For workflow RO-Crate, if there is an unrecognised workflow file, the function will return an warning message.
    Please check more details at RO-Crate website:
    <https://www.researchobject.org/ro-crate/1.1/workflow-and-scripts.html>
    """

    NAME = "Scripts and workflow check"
    # wkfext_path = '/Users/xuanqili/Desktop/ro-crate-validator-py/src/workflow_extension.txt'

    error_message = {
        "WorkflowError":"Semantic Error: Scripts and Workflow is Wrong",
        "TypeError": "Semantic Error: Invalid @type value for workflow file {}. It must have File, SoftwareSourceCode and ComputationalWorkflow as value."
    }
    warning_message = {
        "UnrecognizedWkf" : "WARNING: {} is not a recognised workflow extension. Please raise an issue at GitHub: <https://github.com/ResearchObject/ro-crate-validator-py/issues>."
    }
    
    ### dictionary to store checking result
    workflow_result = {}
    
    context, metadata = rocrate.read_metadata(os.path.join(tar_file, "ro-crate-metadata.json"))
    
    ### check if recognised workflow file meets the requirments
    for entity in metadata.values():
        id_ = utils.get_norm_value(entity, "@id")[0]
        extension_set = list(we.get_workflow_extension())
        # with open (wkfext_path, "r") as file:
        #     extension_set = file.read().splitlines()
        recognisedWkf_upd(extension_set, entity, workflow_result, id_, error_message)
    
    ### check unrecognised workflow file with ComputaionalWorkflow in its @type
    for entity in metadata.values():
        type = utils.get_norm_value(entity, "@type")
        if "ComputationalWorkflow" in type:
            unrecognisedWfk_upd(type, extension_set, entity, workflow_result, warning_message, error_message)

    ### fucntion will return True only when the all of the recognised workflow file are correct      
    for values in workflow_result.values():
        if isinstance(values, list):
            return Result(NAME, code = -1, message = values[1])
        elif isinstance(values, str):
            return Result(NAME, code = 1, message = values)
        else:
            return Result(NAME)
    
    return Result(NAME, code = -1, message = error_message["WorkflowError"])

print(scripts_and_workflow_check("valid").message)

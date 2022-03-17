"""A module to decode text strings based on an encoding.

This is typically used by the Data Manager's API instance methods
when launching applications (and Jobs) where text requires decoding,
given a 'template' string and a 'dictionary' of parameters and values.
"""
import enum
import os
from typing import Any, Dict, Optional, Tuple

import jsonschema
import yaml

# The decoding engine implementations.
# The modules are expected to be called 'decode_<TextEncoding.lower()>'
from . import decode_jinja2_3_0

# The (built-in) schemas...
# from the same directory as us.
_JD_SCHEMA_FILE: str = os.path.join(os.path.dirname(__file__),
                                    'job-definition-schema.yaml')
_MANIFEST_SCHEMA_FILE: str = os.path.join(os.path.dirname(__file__),
                                          'manifest-schema.yaml')

# Load the JD schema YAML file now.
# This must work as the file is installed along with this module.
assert os.path.isfile(_JD_SCHEMA_FILE)
with open(_JD_SCHEMA_FILE, 'r', encoding='utf8') as schema_file:
    _JOB_DEFINITION_SCHEMA: Dict[str, Any] =\
        yaml.load(schema_file, Loader=yaml.FullLoader)
assert _JOB_DEFINITION_SCHEMA

# Load the Manifest schema YAML file now.
# This must work as the file is installed along with this module.
assert os.path.isfile(_MANIFEST_SCHEMA_FILE)
with open(_MANIFEST_SCHEMA_FILE, 'r', encoding='utf8') as schema_file:
    _MANIFEST_SCHEMA: Dict[str, Any] =\
        yaml.load(schema_file, Loader=yaml.FullLoader)
assert _MANIFEST_SCHEMA


class TextEncoding(enum.Enum):
    """A general text encoding format, used initially for Job text fields.
    """
    JINJA2_3_0 = 1      # Encoding that complies with Jinja2 v3.0.x


def validate_manifest_schema(manifest: Dict[str, Any]) -> Optional[str]:
    """Checks the Job Definition Manifest (a preloaded job-definition dictionary)
    against the built-in schema. If there's an error the error text is
    returned, otherwise None.
    """
    assert isinstance(manifest, dict)

    # Validate the Manifest against our schema
    try:
        jsonschema.validate(manifest, schema=_MANIFEST_SCHEMA)
    except jsonschema.ValidationError as ex:
        return str(ex.message)

    # OK if we get here
    return None


def validate_job_schema(job_definition: Dict[str, Any]) -> Optional[str]:
    """Checks the Job Definition (a preloaded job-definition dictionary)
    against the built-in schema. If there's an error the error text is
    returned, otherwise None.
    """
    assert isinstance(job_definition, dict)

    # Validate the Job Definition against our schema
    try:
        jsonschema.validate(job_definition, schema=_JOB_DEFINITION_SCHEMA)
    except jsonschema.ValidationError as ex:
        return str(ex.message)

    # OK if we get here
    return None


def decode(template_text: str,
           variable_map: Optional[Dict[str, str]],
           subject: str,
           template_engine: TextEncoding) -> Tuple[str, bool]:
    """Given some text and a 'variable map' (a dictionary of keys and values)
    this returns the decoded text (using the named engine) as a string
    and a boolean set to True. On failure the boolean is False and the returned
    string is an error message.

    The 'subject' is a symbolic reference to the text
    used for error reporting so the client understands what text is
    in error. i.e. if the text is for a 'command'
    the subject might be 'command'.
    """
    assert template_text
    assert subject
    assert template_engine

    # If there are no variables just return the template text
    if variable_map is None:
        return template_text, True

    if template_engine.name.lower() == 'jinja2_3_0':
        return decode_jinja2_3_0.decode(template_text, variable_map, subject)

    # Unsupported engine if we get here!
    return f'Unsupported template engine: {template_engine}', False

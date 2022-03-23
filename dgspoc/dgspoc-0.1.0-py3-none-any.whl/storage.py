"""Module containing the logic for template storage"""

import yaml
from dgspoc.config import Data
from dgspoc.utils import File
from dgspoc.utils import Misc

from dgspoc.exceptions import TemplateStorageError


class TemplateStorage:
    message = ''
    filename = Data.template_storage_filename

    @classmethod
    def get(cls, template_id):
        if cls.check(template_id):
            with open(cls.filename) as stream:
                node = yaml.safe_load(stream)
                template = node.get(template_id)
                return template
        else:
            return ''

    @classmethod
    def check(cls, template_id):
        if File.is_exist(cls.filename):
            with open(cls.filename) as stream:
                content = stream.read().strip()
                if content:
                    node = yaml.safe_load(content)
                    if Misc.is_dict_instance(node):
                        return template_id in node
                    else:
                        fmt = '{} file has invalid template storage format.'
                        raise TemplateStorageError(fmt.format(cls.filename))
                else:
                    fmt = '*** CANT find "{}" template ID because template storage file is empty.'
                    cls.message = fmt.format(template_id)
                    return False
        else:
            fmt = '*** CANT find {} because template storage file is not created.'
            cls.message = fmt.format(template_id)
            return False

    @classmethod
    def upload(cls, template_id, template, replaced=False):
        try:
            if not File.is_exist(cls.filename):
                File.create(cls.filename)
            if not cls.check(template_id):
                node = {template_id: template}
                File.save(cls.filename, yaml.safe_dump(node))
                return True
            else:
                if replaced:
                    content = open(cls.filename).read()
                    node = yaml.safe_load(content)
                    node[template_id] = template
                    File.save(cls.filename, yaml.safe_dump(node))
                    return True
                else:
                    fmt = ('CANT upload generated template because of '
                           'duplicate "{}" template ID.  Use replaced '
                           'flag accordingly.')
                    cls.message = fmt.format(template_id)
                    return False
        except Exception as ex:
            cls.message = '{}: {}'.format(type(ex).__name__, ex)
            return False

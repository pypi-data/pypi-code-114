from abc import abstractmethod, ABCMeta

OBJECT = 'object'
ARRAY = 'array'
FIElD = 'field'


class SchemaConvertor(metaclass=ABCMeta):

    @abstractmethod
    def convert(self, schema: dict, name="", level=0):
        pass

    @staticmethod
    def get_schema_type(schema):
        if schema.get('type') == 'object' and 'properties' in schema.keys():
            return OBJECT
        elif schema.get('type') and 'items' in schema.keys() and schema['items'].get('type') == 'object':
            return ARRAY
        else:
            return FIElD


class UISchemaConvertor(SchemaConvertor):

    def convert(self, schema: dict, name="", level=0):

        # object
        schema['title'] = schema.get('title', name)
        schema['description'] = schema.get('description', '')
        if self.get_schema_type(schema) == OBJECT:
            schema['title'] = schema.get('title', name)
            for p_name, p_schema in schema['properties'].items():
                schema['properties'][p_name] = self.convert(p_schema, p_name, level+1)

        # multiple objects
        elif self.get_schema_type(schema) == ARRAY:
            schema['items'] = self.convert(schema['items'], name, level+1)

        else:
            # TODO: 모델 베이스로 생성 가능한 스키마의 종류를 정리 후에 적용
            schema['x-widget'] = self.get_widget(schema, name)

        return schema

    @staticmethod
    def get_widget(schema, name):
        from ..enums import Widget
        schema_keys = schema.keys()
        schema_type = schema.get('type')

        # text(base)
        widget = Widget.TEXT_INPUT

        # id
        if 'id' in name and schema.get('readOnly'):
            widget = Widget.HIDDEN
        # password
        elif 'password' in name:
            widget = Widget.PASSWORD
        # number
        elif schema_type == 'number':
            widget = Widget.NUMBER
        # integer
        elif schema_type == 'integer':
            widget = Widget.INTEGER
        # boolean
        elif schema_type == 'boolean':
            widget = Widget.TOGGLE
        # single-choice
        elif schema_type == 'string' and 'oneOf' in schema_keys:
            widget = Widget.SELECT
        # multiple choice
        elif schema_type == 'array' and 'items' in schema_keys and 'oneOf' in schema['items'].keys():
            widget = Widget.CHECKBOX
        # long_text
        elif schema_type == 'string' and schema.get('maxLength', 300) >= 300:
            widget = Widget.TEXTAREA
        # json_text
        elif schema_type == 'object' and 'additionalProperties' in schema_keys:
            widget = Widget.TEXTAREA

        return widget.name


class FormConvertMixin:
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)

        not_implement_errors = []

        from ..enums import Widget
        for w in Widget:
            widget_name = w.name.lower()
            method_name = f"get_{widget_name}_schema"
            if not getattr(new_class, method_name, False):
                error = f'"def {method_name}(self, schema)" method must be defined!'
                not_implement_errors.append(error)

        if len(not_implement_errors) > 0:
            error_msg = f'{cls.__name__} Class\n'
            error_msg += '\n'.join(not_implement_errors)
            raise NotImplementedError(error_msg)
        return new_class

    def _get_form_schema(self, schema, widget):
        method_name = f"get_{widget.lower()}_schema"
        return getattr(self, method_name)(schema)

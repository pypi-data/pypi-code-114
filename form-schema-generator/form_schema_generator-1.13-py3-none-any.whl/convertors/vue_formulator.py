from .base import FormConvertMixin, SchemaConvertor, OBJECT, ARRAY


class VueFormulateConvertor(FormConvertMixin, SchemaConvertor):

    def convert(self, schema: dict, name="", level=0):
        converted_schema = []
        schema_type = self.get_schema_type(schema)

        # object
        if schema_type in [OBJECT, ARRAY]:
            label = None
            content = []
            schema_object = schema if schema.get('properties') else schema['items']
            for p_name, p_schema in schema_object['properties'].items():
                converted_property = self.convert(p_schema, p_name, level + 1)
                if p_name in schema_object.get('required', []) and len(converted_property) == 1:
                    self.add_validation(converted_property[0], 'required')

                content.extend(converted_property)

            label_name = schema.get("title") or name

            # top level object
            if level == 0:
                label = self._get_label(label_name, "h2")
                if schema_type == 'array':
                    content = [self._wrap_group(name, content, True)]
            # nested object
            elif schema_type == 'object':
                label = self._get_label(label_name, "h3")
                content = [self._wrap_group(name, content)]

            # nested objects
            elif schema_type == 'array':
                label = self._get_label(label_name, "h3")
                content = [self._wrap_group(name, content, True)]

            converted_schema.append(label)
            converted_schema.extend(content)

        else:
            field_schema = self._get_form_schema(schema, schema.get('x-widget'))
            field_schema['name'] = name
            if field_schema['type'] != 'hidden':
                field_schema['label'] = schema.get('title')
                field_schema['placeholder'] = schema.get('description')
            converted_schema.append(field_schema)

        return converted_schema

    def _wrap_group(self, name: str, properties: list, repeatable=False):
        group = {
            "type": "group",
            "name": name,
            "repeatable": repeatable,
            "children": properties,
          }
        if repeatable:
            group["add-label"] = "+ ADD"

        return group

    def _get_label(self, name, size="h2"):
        return {
            "component": size,
            "children": name
        }


    def add_validation(self, filed_schema, validation):
        validations = []
        if filed_schema.get('validation'):
            validations.extend(filed_schema.get('validation').split("|"))
        validations.append(validation)
        filed_schema['validation'] = "|".join(validations)

    def get_text_input_schema(self, schema):

        form_schema = {
            "type": "text",
        }
        return form_schema

    def get_number_schema(self, schema):
        """
            Example numberschema
            type: "number"
            name: "sample"
            label: "Sample number input"
            placeholder: "Sample number placeholder"
            help: "Sample number help text"
            validation: "required|number|between:10,20"
            min: "0"
            max: "100"
        """
        form_schema = {
            "type": "text",
            "inputmode": "numeric",
            "validation": "matches:/^[0-9]*.[0-9]*$/"
        }
        return form_schema


    def get_integer_schema(self, schema):
        """
            Example numberschema
            type: "number"
            name: "sample"
            label: "Sample number input"
            placeholder: "Sample number placeholder"
            help: "Sample number help text"
            validation: "required|number|between:10,20"
            min: "0"
            max: "100"
        """
        form_schema = {
            "type": "text",
            "inputmode": "numeric",
            "validation": "matches:/^[0-9]*$/",
        }
        return form_schema

    def get_date_schema(self, schema):
        form_schema = {
            "type": "date",
        }
        return form_schema

    def get_checkbox_schema(self, schema):
        options = {}
        for option in schema['items']['oneOf']:
            options[option['const']] = option['title']

        form_schema = {
            "type": "checkbox",
            "options": options
        }
        return form_schema

    def get_select_schema(self, schema):
        options = {}
        for option in schema['oneOf']:
            options[option['const']] = option['title']

        form_schema = {
            "type": "select",
            "options": options
        }
        return form_schema

    def get_textarea_schema(self, schema):
        form_schema = {
            "type": "textarea",
        }
        return form_schema

    def get_json_schema(self, schema):
        form_schema = {
            "type": "textarea",
        }
        return form_schema

    def get_hidden_schema(self, schema):
        form_schema = {
            "type": "hidden",
        }
        return form_schema

    def get_toggle_schema(self, schema):
        form_schema = {
            "type": "checkbox",
        }
        return form_schema

    def get_password_schema(self, schema):
        form_schema = {
            "type": "password",
        }
        return form_schema

    # 최악의 case
    # def get_text_input

        # if widget == Widget.TEXT_INPUT:
        #
        # elif widget == Widget.NUMBER:
        #
        # elif widget == Widget.URI:
        #
        # elif widget == Widget.DATE:
        #
        # elif widget == Widget.CHECKBOX:
        #
        # elif widget == Widget.SELECT:
        #
        # elif widget == Widget.TEXTAREA:
        #
        # elif widget == Widget.JSON:
        #
        # elif widget == Widget.HIDDEN:
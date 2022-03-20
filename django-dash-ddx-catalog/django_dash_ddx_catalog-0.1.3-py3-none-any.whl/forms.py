import dash_html_components as html

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from django.contrib.admin.utils import lookup_field  #, display_for_value, display_for_field

from .fields import ddx_widgets, ddx_table_columns, display_for_value, display_for_field


__all__ = (
    'DashDDXForm',
    'DashDDXModelForm',
)


class DashDDXBaseForm(object):
    def as_ddx_div(self):
        tags = []
        # print('initial', self.initial)
        for f_name, f in self.base_fields.items():
            c = ddx_widgets[f.widget.__class__]

            label = str(f.label)
            is_required = f.required

            extra_attrs = f.widget_attrs(f.widget) or {}
            attrs = f.widget.attrs.copy()
            attrs.update(extra_attrs)

            ddx_attrs = {}
            ddx_widget_attr = getattr(self.Meta, 'ddx_widget_attrs', {}).get(f_name, {})
            if isinstance(ddx_widget_attr, dict):
                ddx_attrs = ddx_widget_attr.copy()
            if isinstance(ddx_widget_attr, str):
                ddx_widget_method = getattr(self, ddx_widget_attr, None)
                if callable(ddx_widget_method):
                    ddx_attrs = ddx_widget_method()

            if 'maxlength' in attrs:
                ddx_attrs['maxLength'] = attrs['maxlength']
            if 'min' in attrs:
                ddx_attrs['min'] = attrs['min']
            if 'max' in attrs:
                ddx_attrs['max'] = attrs['max']

            if c.__name__ == 'NumberBox':
                ddx_attrs['showSpinButtons'] = True
                ddx_attrs['showClearButton'] = True
                ddx_attrs['showSpinButtons'] = True
                ddx_attrs['step'] = 1
                if f.__class__.__name__ == 'FloatField':
                    ddx_attrs['format'] = '#0.##'
                else:
                    ddx_attrs['format'] = '#0'

            # print(f, f.__class__.__name__, f.label)
            # print(attrs)

            try:
                f, attr, value = lookup_field(f_name, self.instance)  # , cl.model_admin)
            except (ObjectDoesNotExist, AttributeError):
                value = None

            # print(f_name, value, type(value))

            if f.__class__.__name__ in ('DateTimeField', 'DateField'):
                if is_required:
                    v = (value or timezone.now()).isoformat()
                elif value:
                    v = value.isoformat()
                else:
                    v = None

                tags.append(
                    html.Div(className='option', children=[
                        html.Span(label),
                        c(name=f_name, type='datetime' if f.__class__.__name__ == 'DateTimeField' else 'date',
                          value=v,
                          displayFormat='dd.MM.yyyy HH:mm:ss', dateSerializationFormat='yyyy-MM-ddTHH:mm:ssZ',
                          openOnFieldClick=True, applyValueMode='useButtons', acceptCustomValue=True, **ddx_attrs),
                    ])
                )
            elif f.__class__.__name__ in ('ForeignKey', 'ModelChoiceField'):
                related_objects = lambda obj: dict(id=obj.pk, name=str(obj))
                if hasattr(f, 'related_model'):
                    values = list(map(related_objects, f.related_model.objects.all()))
                else:
                    values = list(map(related_objects, f.queryset))

                if not is_required:
                    values.insert(0, dict(id=None, name=''))
                if is_required:
                    v = self.instance and value and value.pk or values and values[0]['id'] or None
                elif value:
                    v = value.pk
                else:
                    v = None

                tags.append(
                    html.Div(className='option', children=[
                        html.Span(label),
                        c(
                          dataSource={'store': values, 'key': 'id'}, name=f_name,
                          displayExpr='name', valueExpr='id', value=v,
                          searchEnabled=True, searchMode='contains', searchExpr='name',
                          searchTimeout=200,  # showDataBeforeSearchOption=True,
                          **ddx_attrs
                        ),
                    ]),
                )
            elif f.__class__.__name__ == 'BooleanField':
                tags.append(
                    html.Div(className='option', children=[
                        html.Span(label, style=dict(marginRight=4)),
                        c(name=f_name, value=bool(value), **ddx_attrs),
                    ])
                )
            elif c.__name__ == 'TextArea':
                value = display_for_field(value, f, None)
                tags.append(
                    html.Div(className='option', children=[
                        html.Span(label),
                        c(name=f_name, value=value, height=48, **ddx_attrs),
                    ])
                )
            else:
                value = display_for_field(value, f, None)
                tags.append(
                    html.Div(className='option', children=[
                        html.Span(label),
                        c(name=f_name, value=value, **ddx_attrs),
                    ])
                )
        return tags

    @staticmethod
    def get_form_values(dash_form_children):
        data = {}
        while dash_form_children:
            elem = dash_form_children.pop(0)
            if 'children' in elem['props'] and elem['props']['children']:
                if isinstance(elem['props']['children'], list):
                    for c in elem['props']['children']:
                        dash_form_children.append(c)
                elif isinstance(elem['props']['children'], dict):
                    dash_form_children.append(elem['props']['children'])
            else:
                if elem['type'] in (
                        'Autocomplete', 'Calendar', 'CheckBox', 'ColorBox',
                        'DateBox', 'DropDownBox', 'HtmlEditor',
                        'Lookup', 'NumberBox', 'RadioGroup', 'RangeSlider',
                        'SelectBox', 'Slider', 'Switch',
                        'TagBox', 'TextArea', 'TextBox', 'Textarea', 'Input'
                ):
                    data[elem['props']['name']] = (
                        elem['props']['value']['value']
                        if isinstance(elem['props'].get('value'), dict)
                        else elem['props'].get('value')
                    )
        return data


class DashDDXForm(DashDDXBaseForm, forms.Form):
    ...


class DashDDXModelForm(DashDDXBaseForm, forms.ModelForm):
    @staticmethod
    def items_for_result(columns, result, form=None):
        for field_index, field_name in enumerate(columns):
            empty_value_display = None  #cl.model_admin.get_empty_value_display()
            # row_classes = ['field-%s' % _coerce_field_name(field_name, field_index)]
            try:
                f, attr, value = lookup_field(field_name, result)#, cl.model_admin)
            except ObjectDoesNotExist:
                result_repr = empty_value_display
            else:
                empty_value_display = getattr(attr, 'empty_value_display', empty_value_display)
                if f is None or f.auto_created:
                    # if field_name == 'action_checkbox':
                    #     row_classes = ['action-checkbox']
                    boolean = getattr(attr, 'boolean', False)
                    result_repr = display_for_value(value, empty_value_display, boolean)
                    # if isinstance(value, (datetime.date, datetime.time)):
                    #     row_classes.append('nowrap')
                else:
                    if isinstance(f.remote_field, models.ManyToOneRel):
                        field_val = getattr(result, f.name)
                        if field_val is None:
                            result_repr = empty_value_display
                        else:
                            result_repr = field_val
                    else:
                        result_repr = display_for_field(value, f, empty_value_display)
                    # if isinstance(f, (models.DateField, models.TimeField, models.ForeignKey)):
                    #     row_classes.append('nowrap')
            yield str(result_repr) if isinstance(result_repr, models.Model) else result_repr

    @classmethod
    def ddx_table_columns(cls):
        columns = []
        for f_name, f in cls.base_fields.items():
            Column = ddx_table_columns[f.__class__]
            columns.append(Column(f_name, str(f.label)))
        return columns

    @classmethod
    def ddx_table_rows(cls, *args, **kwargs):
        rows = []
        columns = ['id'] + [name for name in cls.base_fields.keys()]
        objects = cls._meta.model.objects.all().filter(*args, **kwargs)
        for obj in objects:
            values = cls.items_for_result(columns, obj)
            rows.append(dict(zip(columns, values)))
        return rows

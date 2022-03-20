import datetime
import decimal

import dash_devextreme as ddx
import dash_core_components as dcc

from django import forms
from django.db import models
from django.utils import timezone


__all__ = (
    'ddx_table_columns',
    'ddx_widgets',
    'display_for_field',
    'display_for_value',
)


def column_bool(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='boolean', **kwargs)


def column_str(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='string', **kwargs)


def column_int(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='number', format='#0', **kwargs)


def column_float(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='number',
                format=kwargs.pop('format', '#0.###'), **kwargs)


def column_dt(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='datetime',
                format=kwargs.pop('format', 'dd.MM.yyyy HH:mm:ss'), **kwargs)


def column_d(data_field, caption, **kwargs):
    return dict(dataField=data_field, caption=caption, dataType='date',
                format=kwargs.pop('format', 'dd.MM.yyyy'), **kwargs)


ddx_table_columns = {
    forms.ModelChoiceField: column_str,
    # forms.BigIntegerField: column_int,  # IntegerField with min_value set to -9223372036854775808 and max_value set to 9223372036854775807.
    # forms.BinaryField: column_str,  # CharField, if editable is set to True on the model field, otherwise not represented in the form.
    forms.BooleanField: column_bool,  # BooleanField, or NullBooleanField if null=True.
    forms.CharField: column_str,  # CharField with max_length set to the model field’s max_length and empty_value set to None if null=True.
    forms.DateField: column_d,  # DateField
    forms.DateTimeField: column_dt,  # DateTimeField
    forms.DecimalField: column_float,  # DecimalField
    forms.DurationField: column_int,  # DurationField
    forms.EmailField: column_str,  # EmailField
    forms.FileField: column_str,  # FileField
    forms.FilePathField: column_str,  # FilePathField
    forms.FloatField: column_float,  # FloatField
    # forms.ForeignKey: column_str,  # ModelChoiceField (see below)
    forms.ImageField: column_str,  # ImageField
    forms.IntegerField: column_int,  # IntegerField
    # forms.IPAddressField: column_str,  # IPAddressField
    forms.GenericIPAddressField: column_str,  # GenericIPAddressField
    forms.JSONField: column_str,  # JSONField
    forms.ModelMultipleChoiceField: column_str,  # ModelMultipleChoiceField (see below)
    forms.NullBooleanField: column_bool,  # NullBooleanField
    # forms.PositiveBigIntegerField: column_int,  # IntegerField
    # forms.PositiveIntegerField: column_int,  # IntegerField
    # forms.PositiveSmallIntegerField: column_int,  # IntegerField
    forms.SlugField: column_str,  # SlugField
    # forms.SmallIntegerField: column_int,  # IntegerField
    # forms.TextField: column_str,  # CharField with widget=forms.Textarea
    forms.TimeField: column_float,  # TimeField
    forms.URLField: column_str,  # URLField
    forms.UUIDField: column_str,  # UUIDField
}


ddx_widgets = {
    forms.TextInput: ddx.TextBox,
    forms.URLInput: ddx.TextBox,
    forms.PasswordInput: ddx.TextBox,
    forms.HiddenInput: dcc.Input,
    forms.Textarea: ddx.TextArea,
    forms.DateInput: ddx.DateBox,
    forms.DateTimeInput: ddx.DateBox,
    forms.TimeInput: ddx.NumberBox,
    forms.CheckboxInput: ddx.CheckBox,
    forms.Select: ddx.SelectBox,
    forms.NumberInput: ddx.NumberBox,

    forms.ModelChoiceField: ddx.SelectBox,
    # forms.BigIntegerField: ddx.NumberBox,  # IntegerField with min_value set to -9223372036854775808 and max_value set to 9223372036854775807.
    # forms.BinaryField: ddx.TextBox,  # CharField, if editable is set to True on the model field, otherwise not represented in the form.
    forms.BooleanField: ddx.CheckBox,  # BooleanField, or NullBooleanField if null=True.
    forms.CharField: ddx.TextBox,  # CharField with max_length set to the model field’s max_length and empty_value set to None if null=True.
    forms.DateField: ddx.DateBox,  # DateField
    forms.DateTimeField: ddx.DateBox,  # DateTimeField
    forms.DecimalField: ddx.NumberBox,  # DecimalField
    forms.DurationField: ddx.NumberBox,  # DurationField
    forms.EmailField: ddx.TextBox,  # EmailField
    forms.FileField: ddx.TextBox,  # FileField
    forms.FilePathField: ddx.TextBox,  # FilePathField
    forms.FloatField: ddx.NumberBox,  # FloatField
    # forms.ForeignKey: ddx.SelectBox,  # ModelChoiceField (see below)
    forms.ImageField: ddx.TextBox,  # ImageField
    forms.IntegerField: ddx.NumberBox,  # IntegerField
    # forms.IPAddressField: ddx.TextBox,  # IPAddressField
    forms.GenericIPAddressField: ddx.TextBox,  # GenericIPAddressField
    forms.JSONField: ddx.TextArea,  # JSONField
    forms.ModelMultipleChoiceField: ddx.SelectBox,  # ModelMultipleChoiceField (see below)
    forms.NullBooleanField: ddx.CheckBox,  # NullBooleanField
    # forms.PositiveBigIntegerField: ddx.NumberBox,  # IntegerField
    # forms.PositiveIntegerField: ddx.NumberBox,  # IntegerField
    # forms.PositiveSmallIntegerField: ddx.NumberBox,  # IntegerField
    forms.SlugField: ddx.TextBox,  # SlugField
    # forms.SmallIntegerField: ddx.NumberBox,  # IntegerField
    # forms.TextField: ddx.TextBox,  # CharField with widget=forms.Textarea
    forms.TimeField: ddx.NumberBox,  # TimeField
    forms.URLField: ddx.TextBox,  # URLField
    forms.UUIDField: ddx.TextBox,  # UUIDField

    models.BigIntegerField: ddx.NumberBox,  # IntegerField with min_value set to -9223372036854775808 and max_value set to 9223372036854775807.
    models.BinaryField: ddx.TextBox,  # CharField, if editable is set to True on the model field, otherwise not represented in the form.
    models.BooleanField: ddx.CheckBox,  # BooleanField, or NullBooleanField if null=True.
    models.CharField: ddx.TextBox,  # CharField with max_length set to the model field’s max_length and empty_value set to None if null=True.
    models.DateField: ddx.DateBox,  # DateField
    models.DateTimeField: ddx.DateBox,  # DateTimeField
    models.DecimalField: ddx.NumberBox,  # DecimalField
    models.DurationField: ddx.NumberBox,  # DurationField
    models.EmailField: ddx.TextBox,  # EmailField
    models.FileField: ddx.TextBox,  # FileField
    models.FilePathField: ddx.TextBox,  # FilePathField
    models.FloatField: ddx.NumberBox,  # FloatField
    models.ForeignKey: ddx.SelectBox,  # ModelChoiceField (see below)
    models.ImageField: ddx.TextBox,  # ImageField
    models.IntegerField: ddx.NumberBox,  # IntegerField
    models.IPAddressField: ddx.TextBox,  # IPAddressField
    models.GenericIPAddressField: ddx.TextBox,  # GenericIPAddressField
    models.JSONField: ddx.TextArea,  # JSONField
    models.ManyToManyField: ddx.SelectBox,  # ModelMultipleChoiceField (see below)
    models.NullBooleanField: ddx.CheckBox,  # NullBooleanField
    models.PositiveBigIntegerField: ddx.NumberBox,  # IntegerField
    models.PositiveIntegerField: ddx.NumberBox,  # IntegerField
    models.PositiveSmallIntegerField: ddx.NumberBox,  # IntegerField
    models.SlugField: ddx.TextBox,  # SlugField
    models.SmallIntegerField: ddx.NumberBox,  # IntegerField
    models.TextField: ddx.TextArea,  # CharField with widget=forms.Textarea
    models.TimeField: ddx.NumberBox,  # TimeField
    models.URLField: ddx.TextBox,  # URLField
    models.UUIDField: ddx.TextBox,  # UUIDField
}


def display_for_field(value, field, empty_value_display):
    # from django.contrib.admin.templatetags.admin_list import _boolean_icon

    if getattr(field, 'flatchoices', None):
        return dict(field.flatchoices).get(value, empty_value_display)
    # BooleanField needs special-case null-handling, so it comes before the
    # general null test.
    elif isinstance(field, models.BooleanField):
        # return _boolean_icon(value)
        return value
    elif value is None:
        return empty_value_display
    elif isinstance(field, models.DateTimeField):
        # return formats.localize(timezone.template_localtime(value))
        return timezone.template_localtime(value)
    elif isinstance(field, (models.DateField, models.TimeField)):
        # return formats.localize(value)
        return value
    elif isinstance(field, models.DecimalField):
        # return formats.number_format(value, field.decimal_places)
        return value
    elif isinstance(field, (models.IntegerField, models.FloatField)):
        # return formats.number_format(value)
        return value
    # elif isinstance(field, models.FileField) and value:
    #     return format_html('<a href="{}">{}</a>', value.url, value)
    # elif isinstance(field, models.JSONField) and value:
    #     try:
    #         return json.dumps(value, ensure_ascii=False, cls=field.encoder)
    #     except TypeError:
    #         return display_for_value(value, empty_value_display)
    else:
        return display_for_value(value, empty_value_display)


def display_for_value(value, empty_value_display, boolean=False):
    # from django.contrib.admin.templatetags.admin_list import _boolean_icon

    if boolean:
        # return _boolean_icon(value)
        return value
    elif value is None:
        return empty_value_display
    elif isinstance(value, bool):
        # return str(value)
        return value
    elif isinstance(value, datetime.datetime):
        # return formats.localize(timezone.template_localtime(value))
        return timezone.template_localtime(value)
    elif isinstance(value, (datetime.date, datetime.time)):
        # return formats.localize(value)
        return value
    elif isinstance(value, (int, decimal.Decimal, float)):
        # return formats.number_format(value)
        return value
    elif isinstance(value, (list, tuple)):
        return ', '.join(str(v) for v in value)
    else:
        return str(value)

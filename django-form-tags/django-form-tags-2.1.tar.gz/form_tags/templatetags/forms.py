import re
from typing import Dict, Optional, Tuple, Type

from django import template
from django.forms import BaseFormSet, BoundField, Widget, forms, widgets
from django.template.loader import render_to_string
from django.utils.html import format_html, strip_tags
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from ..conf import settings

register = template.Library()

TEXT_INPUT_WIDGETS: Tuple[Type[Widget], ...] = (
    widgets.TextInput,
    widgets.NumberInput,
    widgets.EmailInput,
    widgets.URLInput,
    widgets.PasswordInput,
    widgets.TimeInput,
)


def _add_error_class(classes: str, field: BoundField, suppress_errors: bool):
    classes = (classes or "").strip()
    if not suppress_errors and len(field.errors):
        return (classes + " error").strip()
    return classes


def _get_field_kwargs(k: int, **kwargs):
    regex = re.compile(r"field{}_".format(k))
    return {
        regex.sub("", key): value for key, value in kwargs.items() if regex.match(key)
    }


def _unit_text(left: str, right: str, fieldwrapper_class="") -> Dict:
    format_kwargs = {}
    if "fieldwrapper--icon" not in fieldwrapper_class:
        fieldwrapper_class = fieldwrapper_class.strip()
        # left unit icon
        if left:
            format_kwargs["fieldwrapper_class"] = (
                "fieldwrapper--unit " + fieldwrapper_class
            ).strip()
            format_kwargs["before_field"] = format_html(
                '<i class="input-unit input-unit--left">{}</i>\n', left
            )
        # right unit icon
        if right:
            format_kwargs["fieldwrapper_class"] = (
                "fieldwrapper--unit " + fieldwrapper_class
            ).strip()
            format_kwargs["after_field"] = format_html(
                '<i class="input-unit input-unit--right">{}</i>\n', right
            )
    return format_kwargs


@register.simple_tag
def hidden_fields(form: forms.BaseForm):
    return mark_safe("\n".join([field.as_widget() for field in form.hidden_fields()]))


@register.simple_tag
def non_field_errors(form: forms.BaseForm):
    if len(form.non_field_errors()):
        return render_to_string(
            "form_tags/inline_validation.html",
            {"errors": mark_safe(form.non_field_errors())},
        )
    return ""


@register.simple_tag
def non_form_errors(formset: BaseFormSet):
    if len(formset.non_form_errors()):
        return render_to_string(
            "form_tags/inline_validation.html",
            {"errors": mark_safe(formset.non_form_errors())},
        )
    return ""


@register.simple_tag(name="field")
def field_tag(field, suppress_errors=False, **kwargs):
    if isinstance(field.field.widget, TEXT_INPUT_WIDGETS):
        kwargs.update(
            {"class": ("input-field " + kwargs.get("class", "").strip()).strip()}
        )
    classes = _add_error_class(kwargs.get("class", ""), field, suppress_errors)

    kwargs["class"] = (
        field.field.widget.attrs.get("class", "") + " " + classes
    ).strip()

    for attr in settings.FIELD_BOOLEAN_ATTRS:
        if attr in kwargs:
            if not kwargs[attr]:
                kwargs.pop(attr)
            else:
                kwargs[attr] = attr

    if "name" in kwargs:
        html_name = kwargs.pop("name")
        render = field.field.widget.render
        field.field.widget.render = lambda name, *args, **render_kwargs: render(
            html_name, *args, **render_kwargs
        )

    attrs = {k.replace("_", "-"): v for k, v, in kwargs.items()}
    return field.as_widget(attrs=attrs)


@register.simple_tag
def fieldwrapper(
    field: BoundField,
    fieldwrapper_class="",
    before_field="",
    after_field="",
    control_label: Optional[str] = None,
    unit_text_left="",
    unit_text_right="",
    **kwargs
) -> str:
    suppress_errors = kwargs.get("suppress_errors", False)
    classes = _add_error_class(fieldwrapper_class, field, suppress_errors)

    context = {
        "fieldwrapper_class": classes,
        "field_type": field.field.__class__.__name__.lower(),
        "widget_type": field.field.widget.__class__.__name__.lower(),
        "before_field": before_field,
        "after_field": after_field,
        "errors": mark_safe(field.errors) if not suppress_errors else "",
        "help_text": field.help_text,
    }

    if isinstance(field.field.widget, widgets.Select) and not isinstance(
        field.field.widget, widgets.RadioSelect
    ):
        field_wrapper_template = "form_tags/fieldwrapper_select.html"

    elif isinstance(field.field.widget, widgets.CheckboxInput):
        field_wrapper_template = "form_tags/fieldwrapper_checkbox.html"
        if control_label is not None:
            context["control_label"] = control_label
        elif field.help_text:
            context["control_label"] = field.help_text
            context["help_text"] = ""
        else:
            context["control_label"] = field.label

    elif isinstance(field.field.widget, widgets.PasswordInput):
        field_wrapper_template = "form_tags/fieldwrapper.html"
        context["fieldwrapper_class"] = (
            "fieldwrapper--icon " + context.get("fieldwrapper_class", "")
        ).strip()
        context["after_field"] = render_to_string("form_tags/button_password.html")

    elif isinstance(field.field.widget, (widgets.DateInput, widgets.DateTimeInput)):
        field_wrapper_template = "form_tags/fieldwrapper.html"
        context["fieldwrapper_class"] = (
            "fieldwrapper--icon " + context.get("fieldwrapper_class", "")
        ).strip()
        context["after_field"] = render_to_string(
            "form_tags/label_inline_edit_date.html",
            {
                "for": field.id_for_label,
                "title": _("Edit {}").format(strip_tags(field.label)),
            },
        )

    else:
        field_wrapper_template = "form_tags/fieldwrapper.html"

    if isinstance(field.field.widget, TEXT_INPUT_WIDGETS):
        context.update(
            _unit_text(unit_text_left, unit_text_right, context["fieldwrapper_class"])
        )

    if "input-unit--right" in context["after_field"]:
        kwargs["class"] = ("input-field--unit-right " + kwargs.get("class", "")).strip()
    if "input-unit--left" in context["before_field"]:
        kwargs["class"] = ("input-field--unit-left " + kwargs.get("class", "")).strip()

    context["field"] = field_tag(field, **kwargs)

    return render_to_string(field_wrapper_template, context)


@register.simple_tag(takes_context=True)
def fieldholder(
    context: Dict,
    field: BoundField,
    fieldholder_class="",
    horizontal: Optional[bool] = None,
    label_tag: Optional[str] = None,
    label: Optional[str] = None,
    **kwargs
):
    fieldholder_class = fieldholder_class.strip()
    if horizontal is None and context.get("horizontal") or horizontal:
        fieldholder_class = ("fieldholder--horizontal " + fieldholder_class).strip()

    suppress_errors = kwargs["suppress_errors"] = kwargs.get(
        "suppress_errors", context.get("suppress_errors", False)
    )
    classes = _add_error_class(fieldholder_class, field, suppress_errors)

    if label_tag is None and label is not None:
        label_tag = format_html(
            '<label for="{id_for_label}" title="{title_label}">{label}</label>',
            id_for_label=field.id_for_label,
            title_label=strip_tags(label),
            label=label,
        )
    return render_to_string(
        "form_tags/fieldholder.html",
        {
            "field": fieldwrapper(field, **kwargs),
            "label": label_tag
            if label_tag is not None
            else field.label_tag(attrs={"title": strip_tags(field.label)}),
            "fieldholder_class": classes,
        },
    )


@register.simple_tag(takes_context=True)
def fieldholder_inline(
    context: Dict,
    field: BoundField,
    fieldholder_class="",
    label_tag: Optional[str] = None,
    **kwargs
) -> str:
    kwargs.pop("unit_text_left", None)
    kwargs.pop("unit_text_right", None)
    fieldholder_class = fieldholder_class.strip()

    if isinstance(field.field.widget, widgets.ChoiceWidget):
        kwargs.update(
            {
                "fieldwrapper_class": (
                    "select--inline-edit " + kwargs.get("fieldwrapper_class", "")
                ).strip()
            }
        )
    elif isinstance(field.field.widget, TEXT_INPUT_WIDGETS):
        kwargs.update(
            {
                "fieldwrapper_class": (
                    "fieldwrapper--inline-edit " + kwargs.get("fieldwrapper_class", "")
                ).strip(),
                "class": (
                    "input-field--inline-edit " + kwargs.get("class", "")
                ).strip(),
                "after_field": render_to_string(
                    "form_tags/label_inline_edit.html",
                    {
                        "for": field.id_for_label,
                        "title": _("Edit {}").format(strip_tags(field.label)),
                    },
                )
                if label_tag is None
                else label_tag,
                "placeholder": kwargs.get("placeholder", field.label),
            }
        )

    suppress_errors = kwargs["suppress_errors"] = kwargs.get(
        "suppress_errors", context.get("suppress_errors", False)
    )
    classes = _add_error_class(fieldholder_class, field, suppress_errors)

    return render_to_string(
        "form_tags/fieldholder_inline.html",
        {"field": fieldwrapper(field, **kwargs), "fieldholder_class": classes},
    )


def field_tags(*fields: BoundField, **kwargs) -> str:
    suppress_errors = kwargs.pop("suppress_errors", False)

    def get_context():
        for k, field in enumerate(fields):
            field_kwargs = _get_field_kwargs(k, **kwargs)
            before_field = field_kwargs.pop("before_field", "")
            after_field = field_kwargs.pop("after_field", "")
            unit_text_left = field_kwargs.pop("unit_text_left", "")
            unit_text_right = field_kwargs.pop("unit_text_right", "")

            context = {
                "fieldwrapper_class": _add_error_class("", field, suppress_errors),
                "field_type": field.field.__class__.__name__.lower(),
                "widget_type": field.field.widget.__class__.__name__.lower(),
                "before_field": before_field,
                "after_field": after_field,
            }

            if isinstance(field.field.widget, widgets.ChoiceWidget):
                context["fieldwrapper_class"] = (
                    "select " + context.get("fieldwrapper_class", "")
                ).strip()

            elif isinstance(field.field.widget, widgets.PasswordInput):
                context["fieldwrapper_class"] = (
                    "fieldwrapper--icon " + context.get("fieldwrapper_class", "")
                ).strip()
                context["after_field"] = render_to_string(
                    "form_tags/button_password.html"
                )

            elif isinstance(
                field.field.widget, (widgets.DateTimeInput, widgets.DateInput)
            ):
                context["fieldwrapper_class"] = (
                    "fieldwrapper--icon " + context.get("fieldwrapper_class", "")
                ).strip()
                context["after_field"] = render_to_string(
                    "form_tags/label_inline_edit_date.html",
                    {
                        "for": field.id_for_label,
                        "title": _("Edit {}").format(strip_tags(field.label)),
                    },
                )

            if (
                isinstance(field.field.widget, TEXT_INPUT_WIDGETS)
                and "placeholder" not in field.field.widget.attrs
            ):
                field_kwargs["placeholder"] = field_kwargs.get(
                    "placeholder", field.label
                )

                context.update(
                    _unit_text(
                        unit_text_left, unit_text_right, context["fieldwrapper_class"]
                    )
                )

            if "input-unit--right" in context["after_field"]:
                field_kwargs["class"] = (
                    "input-field--unit-right " + field_kwargs.get("class", "")
                ).strip()
            if "input-unit--left" in context["before_field"]:
                field_kwargs["class"] = (
                    "input-field--unit-left " + field_kwargs.get("class", "")
                ).strip()

            context["field"] = field_tag(
                field, suppress_errors=suppress_errors, **field_kwargs
            )

            yield context

    return mark_safe(
        "\n".join(
            render_to_string("form_tags/fieldwrapper_combined_field.html", context)
            for context in get_context()
        )
    )


@register.simple_tag
def fieldwrapper_combined(*fields: BoundField, **kwargs) -> str:
    suppress_errors = kwargs.get("suppress_errors", False)

    format_kwargs = {
        "fieldwrapper_class": kwargs.pop("fieldwrapper_class", "").strip(),
        "fields": field_tags(*fields, **kwargs),
        "errors": (
            mark_safe("\n".join([str(x.errors) for x in fields]))
            if not suppress_errors
            else ""
        ),
        "help_texts": [x.help_text for x in fields if x.help_text],
    }

    return render_to_string("form_tags/fieldwrapper_combined.html", format_kwargs)


@register.simple_tag(takes_context=True)
def fieldholder_combined(context: Dict, *fields: BoundField, **kwargs) -> str:
    fieldholder_class = kwargs.pop("fieldholder_class", "").strip()
    horizontal = kwargs.pop("horizontal", None)
    label_tag = kwargs.pop("label_tag", None)
    label = kwargs.pop("label", None)

    if horizontal is None and context.get("horizontal") or horizontal:
        fieldholder_class = ("fieldholder--horizontal " + fieldholder_class).strip()

    kwargs["suppress_errors"] = kwargs.get(
        "suppress_errors", context.get("suppress_errors", False)
    )

    if label_tag is None and label is not None:
        label_tag = format_html(
            '<label for="{id_for_label}" title="{title_label}">{label}</label>',
            id_for_label=fields[0].id_for_label,
            title_label=strip_tags(label),
            label=label,
        )

    return render_to_string(
        "form_tags/fieldholder.html",
        {
            "field": fieldwrapper_combined(*fields, **kwargs),
            "label": label_tag
            if label_tag is not None
            else fields[0].label_tag(attrs={"title": strip_tags(fields[0].label)}),
            "fieldholder_class": fieldholder_class,
        },
    )

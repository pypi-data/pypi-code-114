import dash_html_components as html
import dash_devextreme as ddx

from django.test import TestCase
from django import forms

from dash_ddx_catalog.forms import DashDDXForm


class SimpleForm(DashDDXForm):
    name = forms.CharField(label='Test label', max_length=255)
    slug = forms.CharField(label='Test slug', max_length=155)

    class Meta:
        ddx_widget_attrs = {
            'name': dict(disabled=True),
            'slug': '_ddx_widget_slug',
        }

    def _ddx_widget_slug(self):
        return dict(disabled=True)


class TestDashDDXForm(TestCase):
    def test_simple(self):
        fields = SimpleForm(initial=dict(name='Test', slug='Slug')).as_ddx_div()

        self.assertTrue(fields[0].__class__ is html.Div)
        self.assertTrue(fields[0].children[0].__class__ is html.Span)
        self.assertTrue(fields[0].children[1].__class__ is ddx.TextBox)
        self.assertTrue(fields[0].children[1].name == 'name')
        self.assertTrue(fields[0].children[1].disabled is True)
        # self.assertTrue(fields[0].children[1].value == 'Test')
        # self.assertTrue(fields[0].children[1].maxLength == 255)

        self.assertTrue(fields[1].__class__ is html.Div)
        self.assertTrue(fields[1].children[0].__class__ is html.Span)
        self.assertTrue(fields[1].children[1].__class__ is ddx.TextBox)
        self.assertTrue(fields[1].children[1].name == 'slug')
        self.assertTrue(fields[1].children[1].disabled is True)

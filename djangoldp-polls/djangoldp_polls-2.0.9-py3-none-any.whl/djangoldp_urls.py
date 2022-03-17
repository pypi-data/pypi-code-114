"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from djangoldp_polls.models.poll import QuestionScale
from djangoldp_polls.views import QuestionScaleTotal, QuestionCheckboxesTotal, QuestionRadioTotal, \
    QuestionSingleChoiceTotal, QuestionMultipleChoiceTotal, poll_export_csv

"""djangoldp project URL Configuration"""
from django.conf.urls import url,include
from djangoldp.models import Model

urlpatterns = [
    url(r'^polls_question_scale/(?P<pk>[0-9]+)/total/', QuestionScaleTotal.as_view(
        {'get': 'retrieve'},
        lookup_field='pk'
    )),
    url(r'^polls_question_checkboxes/(?P<pk>[0-9]+)/total/', QuestionCheckboxesTotal.as_view(
        {'get': 'retrieve'},
        lookup_field='pk'
    )),
    url(r'^polls_question_radio/(?P<pk>[0-9]+)/total/', QuestionRadioTotal.as_view(
        {'get': 'retrieve'},
        lookup_field='pk'
    )),
    url(r'^polls_question_singlechoice/(?P<pk>[0-9]+)/total/', QuestionSingleChoiceTotal.as_view(
            {'get': 'retrieve'},
            lookup_field='pk'
        )),
    url(r'^polls_question_multiplechoices/(?P<pk>[0-9]+)/total/', QuestionMultipleChoiceTotal.as_view(
            {'get': 'retrieve'},
            lookup_field='pk'
        )),
    url(r'^polls/(?P<pk>[0-9]+)/csv/', poll_export_csv, name='export'),
]

from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import serializers
from djangoldp.serializers import LDPSerializer
from djangoldp.views import LDPViewSet, JSONLDRenderer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import csv

from djangoldp_polls.models.poll import QuestionScale, ResponseItemScale, QuestionCheckboxes, ResponseItemCheckboxes, \
    ResponseItemRadio, QuestionRadio, ResponseItemSingleChoice, QuestionSingleChoice, ResponseItemMultipleChoice, \
    QuestionMultipleChoice, Poll, ResponseItemFreeText, ResponseItemWithPropositions


class QuestionScaleTotalSerializer(LDPSerializer):
    mean = serializers.SerializerMethodField()

    class Meta:
        model = QuestionScale
        fields = ['urlid', 'name', 'mean']

    def calculate_mean(self, obj):
        responses = ResponseItemScale.objects.filter(relatedQuestion=obj)

        total = 0
        nb_responses = 0
        for response in responses:
            if response.scale is not None:
                total += response.scale
                nb_responses += 1

        if nb_responses == 0:
            return 0
        return total / nb_responses

    def get_mean(self, obj):
        return json.dumps({
            'scale': obj.scale,
            'mean': self.calculate_mean(obj),
        })


class QuestionScaleTotal(LDPViewSet):
    serializer_class = QuestionScaleTotalSerializer
    model = QuestionScale

    def get_serializer_class(self):
        return QuestionScaleTotalSerializer


class QuestionWithProposition(LDPSerializer):
    responses = serializers.SerializerMethodField()

    class Meta:
        fields = ['urlid', 'name', 'responses']

    def get_responses(self, obj):
        responses = self.item_class.objects.filter(relatedQuestion=obj)
        propMap = {}
        for proposition in obj.propositions.all():
            propMap[proposition.urlid] = {
                'name': proposition.name,
                'count': 0
            }

        total = 0
        for response in responses:
            for proposition in response.relatedPropositions.all():
                propMap[proposition.urlid]['count'] = propMap[proposition.urlid]['count'] + 1
                total = total + 1

        for id in propMap:
            if total == 0:
                propMap[id]['count'] = 0
            else:
                propMap[id]['count'] = propMap[id]['count'] / total
        return json.dumps(propMap)

class QuestionCheckboxesTotalSerializer(QuestionWithProposition):
    item_class = ResponseItemCheckboxes

    class Meta:
        model = QuestionCheckboxes
        fields = ['urlid', 'name', 'responses']

class QuestionCheckboxesTotal(LDPViewSet):
    serializer_class = QuestionCheckboxesTotalSerializer
    model = QuestionCheckboxes

    def get_serializer_class(self):
        return QuestionCheckboxesTotalSerializer

class QuestionRadioTotalSerializer(QuestionWithProposition):
    item_class = ResponseItemRadio

    class Meta:
        model = QuestionRadio
        fields = ['urlid', 'name', 'responses']

class QuestionRadioTotal(LDPViewSet):
    serializer_class = QuestionRadioTotalSerializer
    model = QuestionRadio

    def get_serializer_class(self):
        return QuestionRadioTotalSerializer

class QuestionSingleChoiceTotalSerializer(QuestionWithProposition):
    item_class = ResponseItemSingleChoice

    class Meta:
        model = QuestionSingleChoice
        fields = ['urlid', 'name', 'responses']

class QuestionSingleChoiceTotal(LDPViewSet):
    serializer_class = QuestionSingleChoiceTotalSerializer
    model = QuestionSingleChoice

    def get_serializer_class(self):
        return QuestionSingleChoiceTotalSerializer

class QuestionMultipleChoiceTotalSerializer(QuestionWithProposition):
    item_class = ResponseItemMultipleChoice

    class Meta:
        model = QuestionMultipleChoice
        fields = ['urlid', 'name', 'responses']

class QuestionMultipleChoiceTotal(LDPViewSet):
    serializer_class = QuestionMultipleChoiceTotalSerializer
    model = QuestionMultipleChoice

    def get_serializer_class(self):
        return QuestionMultipleChoiceTotalSerializer


def poll_export_csv(request, pk):
    poll = Poll.objects.filter(author=request.user, id=pk).first()
    if poll is None:
        return HttpResponseNotFound()

    response = HttpResponse(content_type='text/csv', charset='iso-8859-1')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response, delimiter=";")

    header = ['user']
    for question in poll.questions.all():
        header.append(question.name)
    writer.writerow(header)

    for question_response in poll.responses.all():
        line = []
        line.append(question_response.author.email)
        for item in question_response.items.all():
            itemChildInstance = item.get_child_instance()
            if isinstance(itemChildInstance, ResponseItemScale):
                line.append(str(itemChildInstance.scale))
            elif isinstance(itemChildInstance, ResponseItemFreeText):
                line.append(itemChildInstance.content)
            elif isinstance(itemChildInstance, ResponseItemWithPropositions):
                propositions = [pro.name for pro in itemChildInstance.relatedPropositions.all()]
                line.append(','.join(propositions))
            else:
                raise Exception('Unable to manage question type')

        writer.writerow(line)


    return response
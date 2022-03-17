from django.conf import settings

from djangoldp.models import Model
from django.db import models, transaction
from djangoldp.permissions import LDPPermissions
from djangoldp.serializers import LDListMixin, LDPSerializer, ContainerSerializer
from djangoldp_circle.models import Circle

from django.utils.timezone import localdate, timedelta

from djangoldp.views import LDPViewSet, LDPNestedViewSet
from rest_framework import serializers
import datetime

from djangoldp_polls.models.utils import get_child_instance


def onMonthLater():
    return localdate() + timedelta(days=30)


class QuestionPropositionRecorder:
    def record(self, question, choices):
        for k in choices:
            proposition = QuestionProposition(name=choices[k])
            proposition.question = question
            proposition.save()


class QuestionRecorder:
    def record(self, request, poll):
        propositionRecorder = QuestionPropositionRecorder()

        if request['type'] == 'free-text':
            question = QuestionFreeText(
                name=request['name'],
                required=request['required']
            )
            question.poll = poll
            question.save()
        elif request['type'] == 'scale':
            question = QuestionScale(
                name=request['name'],
                scale=request['scale'],
                required=request['required']
            )
            question.poll = poll
            question.save()
        elif request['type'] == 'radio':
            question = QuestionRadio(name=request['name'], required=request['required'])
            question.poll = poll
            question.save()
            propositionRecorder.record(question, request['choices'])
        elif request['type'] == 'checkboxes':
            question = QuestionCheckboxes(name=request['name'], required=request['required'])
            question.poll = poll
            question.save()
            propositionRecorder.record(question, request['choices'])
        elif request['type'] == 'singlechoice':
            question = QuestionSingleChoice(name=request['name'], required=request['required'])
            question.poll = poll
            question.save()
            propositionRecorder.record(question, request['choices'])
        elif request['type'] == 'multiplechoice':
            question = QuestionMultipleChoice(name=request['name'], required=request['required'])
            question.poll = poll
            question.save()
            propositionRecorder.record(question, request['choices'])

        else:
            raise AttributeError('Invalid field type')

        return question


class PollSerializer(LDPSerializer):
    with_cache = False

    def to_representation(self, obj):
        res = super().to_representation(obj)
        res['response_count'] = obj.responses.count()
        res['open'] = obj.is_open()
        res['sort_key'] = "{open}_{date}".format(
            open=(0 if obj.is_open() else 1),
            date=('' if obj.startDate is None else obj.startDate)
        )
        return res


# Here to avoid circular dependencies problem
class PollViewSet(LDPViewSet):
    serializer_class = PollSerializer

    def perform_create(self, serializer, **kwargs):
        instance = super().perform_create(serializer, **kwargs)

        recorder = QuestionRecorder()

        if('type' in self.request.data['questionsUnmaped']['ldp:contains']): #single queston
            questions = [self.request.data['questionsUnmaped']['ldp:contains']]
        else:
            questions = self.request.data['questionsUnmaped']['ldp:contains']

        for questionRequest in questions:
            recorder.record(questionRequest, instance)
        return instance

class PollPermissions(LDPPermissions):

    # Remove add permissions on nested poll properties to allow it to be manged by related model permissions
    def get_container_permissions(self, request, view, obj=None):
        perms = super().get_container_permissions(request, view, obj)
        if hasattr(view, 'parent_model') and 'add' in perms: #hasattr used to test if container nested
            perms.remove('add')
        return perms

class Poll(Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdVotes', null=True, blank=True,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=250, verbose_name="Title", null=True, blank=True)
    startDate = models.DateField(verbose_name="Start date", blank=True, null=True)
    endDate = models.DateField(verbose_name="End data", default=onMonthLater, null=True, blank=True)
    description = models.TextField(verbose_name="description", null=True, blank=True)
    circle = models.ForeignKey(Circle, blank=True, null=True, related_name="polls", on_delete=models.SET_NULL)

    def is_open(self):
        if self.startDate is None or self.endDate is None:
            return False
        now = datetime.datetime.now().date()

        return self.startDate <= now <= self.endDate

    class Meta(Model.Meta):
        auto_author = 'author'
        serializer_fields = ['@id', 'created_at', 'author', 'title', 'circle', 'startDate', 'endDate', 'description']
        nested_fields = ["questions"]
        anonymous_perms = []
        authenticated_perms = ['view', 'add']
        owner_field = 'author'
        rdf_type = 'sib:poll'
        view_set = PollViewSet
        container_path = 'polls/'
        permission_classes = [PollPermissions]

    def __str__(self):
        return self.title or ''

class QuestionContainerSerializer(ContainerSerializer):
    @property
    def with_cache(self):
        return False

class QuestionSerializer(LDPSerializer):
    with_cache: False

    # Force serialization of child instead of parent
    def to_representation(self, obj):
        child = obj.get_child_instance()

        class childSerializerClass(LDPSerializer):
            with_cache: False

            class Meta:
                model = child
                fields = Model.get_meta(child, 'serializer_fields')
                depth = 1


        childSerializer = childSerializerClass(context={
            'request': self.context['request'],
            'view': self.context['view'],
            'format': self.context['format']
        })

        res = childSerializer.to_representation(child)

        return res

class QuestionViewSet(LDPViewSet):
    serializer_class = QuestionSerializer

    def build_serializer(self, meta_args, name_prefix):
        meta_args['list_serializer_class'] = QuestionContainerSerializer

        return super(QuestionViewSet, self).build_serializer(meta_args, name_prefix)

class Question(Model):
    name = models.CharField(max_length=250, verbose_name="Name of the question")
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    required = models.BooleanField(default=False, verbose_name="Question required")

    class Meta(Model.Meta):
        serializer_fields = ['@id', 'name', 'required']
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question'
        container_path = 'polls_question/'
        view_set = QuestionViewSet

    # resolve inherance and get direct child instance
    def get_child_instance(self):
        return get_child_instance(self, Question)

    def __str__(self):
        return self.name


class QuestionWithPropositions(Question):
    class Meta(Model.Meta):
        serializer_fields = ['@id', 'name', 'required', 'propositions']
        container_path = 'polls_question_with_propositions/'


class QuestionProposition(Model):
    name = models.CharField(max_length=250, verbose_name="Title", null=True, blank=True)
    question = models.ForeignKey(QuestionWithPropositions, related_name='propositions', on_delete=models.CASCADE)

    class Meta(Model.Meta):
        container_path = 'polls_question_proposition/'
        serializer_fields = ['@id', 'name']
        rdf_type = 'sib:question_proposition'


class QuestionFreeText(Question):
    class Meta(Model.Meta):
        serializer_fields = ['@id', 'name', 'required']
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_free_text'
        container_path = 'polls_question_free_text/'


class QuestionScale(Question):
    scale = models.IntegerField()

    class Meta(Model.Meta):
        serializer_fields = ['@id', 'name', 'scale', 'required']
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_scale'
        container_path = 'polls_question_scale/'


class QuestionRadio(QuestionWithPropositions):
    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_radio'
        container_path = 'polls_question_radio/'
        serializer_fields = ['@id', 'name', 'propositions', 'required']


class QuestionCheckboxes(QuestionWithPropositions):
    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_checkboxes'
        container_path = 'polls_question_checkboxes/'
        serializer_fields = ['@id', 'name', 'propositions', 'required']


class QuestionSingleChoice(QuestionWithPropositions):
    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_singlechoice'
        container_path = 'polls_question_singlechoice/'
        serializer_fields = ['@id', 'name', 'propositions', 'required']


class QuestionMultipleChoice(QuestionWithPropositions):
    class Meta(Model.Meta):
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add', 'delete', 'change']
        rdf_type = 'sib:question_multiplechoices'
        container_path = 'polls_question_multiplechoices/'
        serializer_fields = ['@id', 'name', 'propositions', 'required']

class ResponseItemRecorder(LDListMixin):
    with_cache = False

    def addPropositions(self, responseWithPropositions, choices):
        # user selected no choices
        if choices == '':
            return

        if 'ldp:contains' in choices and len(choices['ldp:contains']) == 1:
            choices['ldp:contains'] = [choices['ldp:contains']]

        if '@id' in choices: # single question
            choices['ldp:contains'] = [choices]

        for choice in choices['ldp:contains']:
            proposition = QuestionProposition.objects.filter(urlid=choice['@id'], question=responseWithPropositions.relatedQuestion).first()
            responseWithPropositions.relatedPropositions.add(proposition)
        responseWithPropositions.save()

    def record(self, request, response):

        if request['type'] == 'free-text':
            related_question = QuestionFreeText.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemFreeText(
                response=response,
                content=request['content'],
                relatedQuestion=related_question
            )
            item.save()

        elif request['type'] == 'scale':
            related_question = QuestionScale.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemScale(
                response=response,
                relatedQuestion=related_question,
                scale=None if request['scale'] == '' else request['scale']
            )
            item.save()

        elif request['type'] == 'checkboxes':
            related_question = QuestionCheckboxes.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemCheckboxes(
                response=response,
                relatedQuestion=related_question
            )
            item.save()
            self.addPropositions(item, request['choices'])

        elif request['type'] == 'radio':
            related_question = QuestionRadio.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemRadio(
                response=response,
                relatedQuestion=related_question
            )
            item.save()
            self.addPropositions(item, request['choices'])

        elif request['type'] == 'multiplechoices':
            related_question = QuestionMultipleChoice.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemMultipleChoice(
                response=response,
                relatedQuestion=related_question
            )
            item.save()
            self.addPropositions(item, request['choices'])

        elif request['type'] == 'singlechoice':
            related_question = QuestionSingleChoice.objects.filter(
                urlid=request['relatedQuestionId'],
                poll=response.poll
            ).first()

            item = ResponseItemSingleChoice(
                response=response,
                relatedQuestion=related_question
            )
            item.save()
            self.addPropositions(item, request['choices'])

        else:
            raise AttributeError('Invalid field type')

        return item

class ResponseContainerSerializer(ContainerSerializer):
    @property
    def with_cache(self):
        return False

class ResponseSerializer(LDPSerializer):
    with_cache: False

class ResponseViewSet(LDPViewSet):
    serializer_class = ResponseSerializer

    def build_serializer(self, meta_args, name_prefix):
        meta_args['list_serializer_class'] = ResponseContainerSerializer

        return super(ResponseViewSet, self).build_serializer(meta_args, name_prefix)

    def perform_create(self, serializer, **kwargs):
        instance = super().perform_create(serializer, **kwargs)

        recorder = ResponseItemRecorder()

        if ('type' in self.request.data['responses']['ldp:contains']):  # single queston
            responses = [self.request.data['responses']['ldp:contains']]
        else:
            responses = self.request.data['responses']['ldp:contains']

        for responseRequest in responses:
            recorder.record(responseRequest, instance)
        return instance


class ResponsePermissions(LDPPermissions):

    def get_container_permissions(self, request, view, obj=None):
        perms = super().get_container_permissions(request, view, obj)

        poll = Model.resolve_parent(request.path)
        user_has_responded = request.user.is_authenticated and poll.responses.filter(author=request.user).exists()
        if (user_has_responded or not poll.is_open()) and 'add' in perms:
            perms.remove('add')

        return perms


class Response(Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdVotesResponses', null=True, blank=True,
                               on_delete=models.SET_NULL)
    poll = models.ForeignKey(Poll, related_name='responses', on_delete=models.CASCADE)

    class Meta(Model.Meta):
        auto_author = 'author'
        anonymous_perms = []
        authenticated_perms = ['add']
        owner_perms = ['view']
        owner_field = 'author'
        serializer_fields = ['@id', 'created_at', 'author', 'poll', 'items']
        rdf_type = 'sib:poll_response'
        container_path = 'polls_response/'
        view_set = ResponseViewSet
        permission_classes = [ResponsePermissions]

class ResponseItem(Model):
    response = models.ForeignKey(Response, related_name='items', on_delete=models.CASCADE)

    class Meta(Model.Meta):
        serializer_fields = ['@id', 'response']
        rdf_type = 'sib:poll_response_item'
        container_path = 'polls_response_item/'

    # resolve inherance and get direct child instance
    def get_child_instance(self):
        return get_child_instance(self, ResponseItem)

class ResponseItemFreeText(ResponseItem):
    content = models.TextField()
    relatedQuestion = models.ForeignKey(QuestionFreeText, related_name='responses', on_delete=models.CASCADE)

    class Meta(Model.Meta):
        serializer_fields = ['@id', 'response', 'content']
        rdf_type = 'sib:poll_response_item_free_text'
        container_path = 'polls_response_item_free_text/'

class ResponseItemWithPropositions(ResponseItem):
    relatedPropositions = models.ManyToManyField(QuestionProposition)

    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_with_propositions'
        container_path = 'polls_response_item_with_propositions/'


class ResponseItemCheckboxes(ResponseItemWithPropositions):
    relatedQuestion = models.ForeignKey(QuestionCheckboxes, on_delete=models.CASCADE)  # Add related question to manage case with no responses

    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_checkboxes'
        container_path = 'polls_response_item_checkboxes/'

class ResponseItemRadio(ResponseItemWithPropositions):
    relatedQuestion = models.ForeignKey(QuestionRadio,
                                        on_delete=models.CASCADE)  # Add related question to manage case with no responses

    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_radio'
        container_path = 'polls_response_item_radio/'

class ResponseItemMultipleChoice(ResponseItemWithPropositions):
    relatedQuestion = models.ForeignKey(QuestionMultipleChoice,
                                        on_delete=models.CASCADE)  # Add related question to manage case with no responses

    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_multiplechoice'
        container_path = 'polls_response_item_multiplechoice/'

class ResponseItemSingleChoice(ResponseItemWithPropositions):
    relatedQuestion = models.ForeignKey(QuestionSingleChoice,
                                        on_delete=models.CASCADE)  # Add related question to manage case with no responses

    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_singlechoice'
        container_path = 'polls_response_item_singlechoice/'

class ResponseItemScale(ResponseItem):
    relatedQuestion = models.ForeignKey(QuestionScale,
                                        on_delete=models.CASCADE)  # Add related question to manage case with no responses
    scale = models.IntegerField(null=True)
    class Meta(Model.Meta):
        rdf_type = 'sib:polls_response_item_scale'
        container_path = 'polls_response_item_scale/'


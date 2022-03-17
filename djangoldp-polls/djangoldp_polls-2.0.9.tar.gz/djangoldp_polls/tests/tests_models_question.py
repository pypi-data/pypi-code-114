from djangoldp_account.models import LDPUser
from djangoldp_circle.models import Circle
from rest_framework.test import APITestCase, APIClient

from djangoldp_polls.models import Poll
from djangoldp_polls.models.poll import QuestionFreeText, QuestionScale, QuestionRadio, QuestionProposition


class TestModelsQuestion(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def buildUser(self, username):
        user = LDPUser(email=username + '@test.startinblox.com', first_name='Test', last_name='Mactest',
                       username=username,
                       password='glass onion')
        user.save()
        return user

    def test_list_questions_type_scale(self):
        user1 = self.buildUser('user1')
        self.client.force_authenticate(user1)

        circle = Circle.objects.create(status='Public')
        poll = Poll.objects.create(title='poll name', circle=circle)
        QuestionScale.objects.create(poll=poll, name='question name', scale=2)

        response = self.client.get("/polls/{}/questions/".format(poll.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual('question name', response.data['ldp:contains'][0]['name'])
        self.assertEqual('sib:question_scale', response.data['ldp:contains'][0]['@type'])
        self.assertEqual(2, response.data['ldp:contains'][0]['scale'])

    def test_list_questions_type_radio(self):
        user1 = self.buildUser('user1')
        self.client.force_authenticate(user1)

        circle = Circle.objects.create(status='Public')
        poll = Poll.objects.create(title='poll name', circle=circle)
        radio = QuestionRadio.objects.create(poll=poll, name='question name')
        QuestionProposition.objects.create(question=radio, name="radio 1")
        QuestionProposition.objects.create(question=radio, name="radio 2")

        response = self.client.get("/polls/{}/questions/".format(poll.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual('question name', response.data['ldp:contains'][0]['name'])
        self.assertEqual('sib:question_radio', response.data['ldp:contains'][0]['@type'])
        self.assertEqual('radio 1', response.data['ldp:contains'][0]['propositions']['ldp:contains'][0]['name'])

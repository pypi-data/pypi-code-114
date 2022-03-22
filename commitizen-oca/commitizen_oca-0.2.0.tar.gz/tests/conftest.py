import pytest
from commitizen import defaults
from commitizen.config import BaseConfig
from commitizen.cz.base import BaseCommitizen


@pytest.fixture()
def config():
    _config = BaseConfig()
    _config.settings.update({"name": defaults.name})
    return _config


@pytest.fixture(params=[
    # anwsers, expected
    (
        {
            "prefix": "IMP",
            "scope": "models",
            "subject": "person was undocumented",
            "body": "When no plant of the field was yet in the image of God he created them; male and female he created them.",
            "closes": "",
            "tasks": "",
            "is_breaking_change": False,
        }, "[IMP] models: person was undocumented\n\nWhen no plant of the field was yet in the image of God he created them; male and female he created them."
    ),
    (
        {
            "prefix": "FIX",
            "scope": "dto",
            "subject": "bla bla",
            "body": "The woman said to him, Where are you?",
            "closes": "",
            "tasks": "145 4567",            
            "is_breaking_change": False,
        }, "[FIX] dto: bla bla\n\nThe woman said to him, Where are you? >>> Related Tasks: #145 #4567"
    ),
    (
        {
            "prefix": "REF",
            "scope": "controllers",
            "subject": "xpto",
            "body": "So out of the heavens and the earth and the woman, and between your offspring and hers; he will strike his heel.",
            "is_breaking_change": True,
            "closes": "",
            "tasks": "",
        }, "[REF] controllers: xpto\n\nBREAKING CHANGE: So out of the heavens and the earth and the woman, and between your offspring and hers; he will strike his heel."
    ),(
        {
            "prefix": "ADD",
            "scope": "docker",
            "subject": "xpto",
            "body": "He drove out the man; and at the east of the garden at the time of the evening breeze, and the man and put him in the garden of Eden, to till the ground the LORD God walking in the image of God he created them; male and female he created them.",
            "closes": "174 25",
            "tasks": "",
            "is_breaking_change": False,

        }, "[ADD] docker: xpto\n\nHe drove out the man; and at the east of the garden at the time of the evening breeze, and the man and put him in the garden of Eden, to till the ground the LORD God walking in the image of God he created them; male and female he created them. Closes #174  Closes #25"
    ),
])
def messages(request):
    return request.param

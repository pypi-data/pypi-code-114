from commitizen_oca.cz_commitizen_oca import CommitizenOcaCz


def test_answer(config, messages):
    cz = CommitizenOcaCz(config)
    answers, expected = messages
    message = cz.message(answers)
    assert message == expected

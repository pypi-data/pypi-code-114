from logntime.validation.assertions.assert_similarities import assert_similarities

sequence = list | tuple


def assert_sequence_similarities(reference: sequence, subject: sequence, custom_message: str = "", accumulator: list = None):
    if reference is subject: return
    if reference == subject: return

    if len(reference) != len(subject):
        message = f"{custom_message}Result is not equal to reference. The size of the result does not match the reference.\n    Reference [{len(reference)}]: {reference}\n    Result [{len(subject)}]: {subject}"
        error = Exception(message)

        if accumulator is None:
            raise error
        else:
            accumulator.append(message)

    assert_similarities(
        list(reference),
        list(subject)
    )

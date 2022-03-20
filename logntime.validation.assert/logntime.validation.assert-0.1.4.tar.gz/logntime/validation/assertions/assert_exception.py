from typing import Type


def add_indentation(text: str, indentation_in_spaces: int = 4):
    """
    Adds indentation to all the lines in the text

    :param text:
    :param indentation_in_spaces:
    :return: The text with indentation added
    """
    indentation = " " * indentation_in_spaces
    return indentation + f"\n{indentation}".join(text.split("\n"))


def assert_exception(reference_type: Type[BaseException], subject: BaseException, original_message_indentation=8):
    """
    Asserts the subject exception is an instance of the reference_type.
    If it fails throws an exception. The error message includes the original exception message with extra indentation to facilitate reading.

    :param reference_type: A subclass of BaseException
    :param subject: exception under examination
    :param original_message_indentation: Extra indentation added to the exception under examination to facilitate reading in case of failure.
    """
    if not isinstance(subject, reference_type):
        original_message = add_indentation(str(subject), original_message_indentation)

        message = f"Unexpected exception.\n    Reference: {IndexError.__name__}\n    Result: {type(subject).__name__}\n\n    Original message:\n{original_message}"
        raise Exception(message)

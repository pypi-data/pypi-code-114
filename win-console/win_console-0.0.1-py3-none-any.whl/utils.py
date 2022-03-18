from .core import stdin
def getpass(prompt: str = 'Password: ', echoChar: str = '*') -> str:
    """
    Read what password user typed.
    :param prompt: Show the prompt.
    :type prompt: str
    :param echoChar: The echo char when user typed.
    :type echoChar: str
    :return: The password that the user typed.
    """
    return stdin(prompt, echoChar)
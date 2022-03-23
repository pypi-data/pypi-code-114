import traceback


def exc_traceback():
    ex_msg = '{exception}'.format(exception=traceback.format_exc())
    print(ex_msg)

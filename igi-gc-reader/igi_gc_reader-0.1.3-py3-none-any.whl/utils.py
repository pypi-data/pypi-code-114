import logging


logging.basicConfig()
gc_logger = logging.getLogger("GC")
gc_logger.setLevel(logging.INFO)


def get_ordinal(n: int) -> str:
    """
    Convert an integer into its ordinal representation::

        get_ordinal(0)   => '0th'
        get_ordinal(3)   => '3rd'
        get_ordinal(11)  => '11th'
        get_ordinal(21)  => '21st'
        get_ordinal(92)  => '92nd'
        get_ordinal(112) => '112th'
        get_ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

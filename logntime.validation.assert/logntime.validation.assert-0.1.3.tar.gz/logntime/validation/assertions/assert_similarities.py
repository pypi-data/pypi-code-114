from logntime.validation.assertions.compare import basic_built_in_types, compare, comparison_to_report


def assert_similarities(reference: basic_built_in_types, subject: basic_built_in_types, custom_message: str = "", accumulator: list = None) -> None:
    """
    Validates that two basic objects have the same values instead of instance equality.

    Can compare instances' pair of: dict, list, tuple, int, float, bool, complex, range, bytes, set, frozenset, None.

    * **Useful** two compare two dict instances that are supposed to have the same keys and values.

    * **Useful** two compare two lists instances that are supposed to have the elements.

    :param reference: Source of truth to compare similarities
    :param subject: Object under analysis
    :param custom_message: Clarification sentence at the beginning of the error message thrown if the validation fails.
    :param accumulator: List used to aggregate error messages. If not None and the validation fails, no exception is thrown.

    :raises Exception: If the reference and the subject are not similar
    """
    if reference is subject: return
    if reference == subject: return

    differences = compare(reference, subject)

    if len(differences) == 0:
        return

    message = f"{custom_message}Subject is not equal to reference. Differences:"

    report = comparison_to_report(differences)
    message += "\n" + report
    error = Exception(message)

    if accumulator is None:
        raise error
    else:
        accumulator.append(message)




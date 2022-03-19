import dictdiffer


def build_path_string(path, root_name="ROOT"):
    result = root_name

    for p in path:
        if isinstance(p, str):
            result += "." + p

        if isinstance(p, int):
            result += "[" + str(p) + "]"

    return result


basic_built_in_types = dict | list | tuple | int | float | bool | complex | range | bytes | set | frozenset | None


def compare(reference: basic_built_in_types, subject: basic_built_in_types):
    comparison = []
    differences = dictdiffer.diff(reference, subject)

    for difference_type, path, details in differences:
        path = list(path)

        match difference_type:
            case "change":
                path_str = build_path_string(path)
                reference, result = details

                comparison.append(
                    (path_str, reference, result)
                )

            case "add":
                for detail in details:
                    sub_path, result = detail
                    if not isinstance(sub_path, list):
                        sub_path = [sub_path]

                    path_str = build_path_string(path + sub_path)

                    comparison.append(
                        (path_str, None, result)
                    )

            case "remove":
                for detail in details:
                    sub_path, reference = detail
                    if not isinstance(sub_path, list):
                        sub_path = [sub_path]
                    path_str = build_path_string(path + sub_path)

                    comparison.append(
                        (path_str, reference, None)
                    )

    return comparison


def comparison_to_report(differences):
    result = ""
    separator = ""

    for difference in differences:
        path, reference, subject = difference
        result += f"{separator}{path}:\n    Reference: {reference}\n    Subject: {subject}"
        separator = "\n"

    return result

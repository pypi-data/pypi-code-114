from collections import OrderedDict
from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import multiple_line_breaker, required_validator
from commitizen.defaults import MAJOR, MINOR, PATCH


def parse_scope(text):
    if not text:
        return ""

    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]

    return "-".join(scope)


def parse_subject(text):
    if isinstance(text, str):
        text = text.strip(".").strip()

    return required_validator(text, msg="Subject is required.")


class CommitizenOcaCz(BaseCommitizen):
    bump_pattern = r"^(BREAKING[\-\ ]CHANGE|\[REL\]|^\[IMP\]|^\[FIX\]|^\[REF\]\|^\[REV\]|^\[MERGE\]|^\[I18N\])(\(.+\))?(!)?"
    bump_map = OrderedDict(
        (
            (r"^.+!$", MAJOR),
            (r"^BREAKING[\-\ ]CHANGE", MAJOR),
            (r"^\[REL\]", MAJOR),
            (r"^\[REL\]", MINOR),
            (r"^\[IMP\]", PATCH),
            (r"^\[FIX\]", PATCH),
            (r"^\[REF\]", PATCH),
            (r"^\[REV\]", PATCH),
            (r"^\[MERGE\]", PATCH),
            (r"^\[I18N\]", PATCH),
        )
    )
    
    def questions(self) -> list:
        questions: List[Dict[str, Any]] = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Select the type of change you are committing",
                "choices": [
                    {
                        "value": "IMP",
                        "name": (
                            "[IMP]: for improvements"
                            " most of the changes done in development version"
                            " are incremental improvements"
                        )
                    },                    
                    {
                        "value": "FIX",
                        "name": "[FIX]: for bug fixes",
                    },
                    {
                        "value": "REF",
                        "name": (
                            "[REF]: for refactoring:"
                            " when a feature is heavily rewritten"
                        ),
                    },

                    {
                        "value": "ADD",
                        "name": "[ADD]: for adding new modules",
                    },
                    {
                        "value": "REM",
                        "name": (
                            "[REM]: for removing of resources"
                            " removing dead code, removing views, removing modules, …"
                        ),
                    },
                    {
                        "value": "REV",
                        "name": (
                            "[REV]: if a commit causes issues or is not wanted"
                            " reverting it is done using this tag"
                        ),
                    },
                   {
                        "value": "MOV",
                        "name": (
                            "[MOV]: for moving files and code"
                            " use git move and do not change content of moved file"
                        ),
                    },
                   {
                        "value": "REL",
                        "name": (
                            "[REL]: for release commits"
                            " new major or minor stable versions"
                        ),
                    },
                   {
                        "value": "MERGE",
                        "name": "[MERGE]: for merge commits"
                    },
                    {
                        "value": "I18N",
                        "name": "[I18N]: for changes in translation files"
                    },                    
                    {
                        "value": "CLA",
                        "name": "[CLA]: for signing the Odoo Individual Contributor License;"
                    },
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": (
                    "Scope. Could be anything specifying place of the "
                    "commit change (module,model,view,...):\n"
                ),
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": (
                    "Subject. Concise description of the changes. "
                    "Imperative, lower case and no final dot:\n"
                ),
            },
            {
                "type": "confirm",
                "message": "Is this a BREAKING CHANGE?",
                "name": "is_breaking_change",
                "default": False,
            },
            {
                "type": "input",
                "name": "body",
                "message": (
                    "Body. Motivation for the change and contrast this "
                    "with previous behavior:\n"
                ),
                "filter": multiple_line_breaker,
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        prefix = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        body = answers["body"]
        is_breaking_change = answers["is_breaking_change"]
        if scope:
            scope = f"{scope}"
        if is_breaking_change:
            body = f"BREAKING CHANGE: {body}"
        if body:
            body = f"\n\n{body}"

        message = f"[{prefix}] {scope}: {subject}{body}"

        return message


discover_this = CommitizenOcaCz

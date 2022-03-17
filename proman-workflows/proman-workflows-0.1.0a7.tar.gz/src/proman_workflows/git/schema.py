"""Provide git schema objecst."""

from typing import Any, List, Tuple

from marshmallow import ValidationError
from marshmallow.fields import Field


class ClientSideHook(Field):
    """Provide validation for client-side git-hooks."""

    hooks: Tuple[str, ...] = (
        'applypatch-msg',
        'pre-applypatch',
        'post-applypatch',
        'pre-commit',
        'pre-merge-commit',
        'prepare-commit-msg',
        'post-commit',
        'pre-rebase',
        'post-checkout',
        'post-merge',
        'pre-push',
        'post-update',
        'reference-transaction',
        'push-to-checkout',
        'pre-auto-gc',
        'post-rewrite',
        'rebase',
        'sendemail-validate',
        'fsmonitor-watchman',
        'p4-changelist',
        'p4-prepare-changelist',
        'p4-post-changelist',
        'p4-pre-submit',
        'post-index-change',
    )

    def _serialize(
        self, value: str, attr: str, obj: object, **kwargs: Any
    ) -> str:
        if value is None:
            return ''
        return ''.join(str(d) for d in value)

    def _deserialize(
        self, value: str, attr: str, data: Any, **kwargs: Any
    ) -> List[int]:
        try:
            return [int(c) for c in value]
        except ValueError as error:
            raise ValidationError(
                'Pin codes must contain only digits.'
            ) from error


class ServerSideHook(Field):
    """Provide validation for client-side git-hooks."""

    hooks: Tuple[str, ...] = (
        'pre-recieve',
        'post-recieve',
        'update',
    )

    def _serialize(
        self, value: str, attr: str, obj: object, **kwargs: Any
    ) -> str:
        if value is None:
            return ''
        return ''.join(str(d) for d in value)

    def _deserialize(
        self, value: str, attr: str, data: Any, **kwargs: Any
    ) -> List[int]:
        try:
            return [int(c) for c in value]
        except ValueError as error:
            raise ValidationError(
                'Pin codes must contain only digits.'
            ) from error

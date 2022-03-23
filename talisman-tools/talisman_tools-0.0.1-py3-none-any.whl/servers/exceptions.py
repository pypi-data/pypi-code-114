import logging
from logging import Logger
from typing import Any, Dict, Generator, Sequence, Tuple, Union

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.errors import PydanticTypeError

_logger = logging.getLogger(__name__)

Loc = Tuple[Union[int, str], ...]


def register_exception_handlers(app: FastAPI, logger: Logger = _logger):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc: RequestValidationError):
        error_content = jsonable_encoder({"detail": list(unwrap(exc.raw_errors))})
        logger.error("Pydantic validation error", extra=error_content)
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=error_content,
        )

    def unwrap(errors: Sequence[Any]) -> Generator[Dict[str, Any], None, None]:
        for error in errors:
            if isinstance(error, ErrorWrapper):
                yield wrap_description(error)
            elif isinstance(error, list):
                yield from unwrap(error)
            else:
                logging.error(f'Unknown error object: {error}')
                raise RuntimeError(f'Unknown error object: {error}')

    def wrap_description(wrap: ErrorWrapper) -> Dict[str, Any]:
        loc = wrap.loc_tuple()  # validated parameter
        if isinstance(wrap.exc, ValidationError):
            model, errors = validation_error(wrap.exc)
        elif isinstance(wrap.exc, PydanticTypeError):
            model, errors = type_error(wrap.exc)
        else:
            model, errors = type(wrap.exc).__name__, []
        return {'model': model, 'loc': loc, 'errors': errors}

    def validation_error(exc: ValidationError) -> Tuple[str, list]:
        return exc.model.__name__, exc.errors()

    def type_error(exc: PydanticTypeError) -> Tuple[str, str]:
        return type(exc).__name__, exc.msg_template

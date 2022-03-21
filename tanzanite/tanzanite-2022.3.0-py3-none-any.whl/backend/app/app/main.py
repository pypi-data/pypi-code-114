# -*- coding: utf-8 -*-

"""
Main FastAPI app definition.
"""

# Standard imports
import logging
import os
import sys

from typing import Callable

# External imports
from dotenv import load_dotenv
from fastapi import (
    Depends,
    FastAPI,
    Request,
)
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

# Local imports
try:
    from tanzanite import (
        FAVICON_PATH,
        LOCALHOST,
        SPHINX_DOCS_HTML,
        STATIC_FILES,
        TANZANITE_BASE_DIR,
    )
    from tanzanite.backend.app.app.api import deps
    from tanzanite.backend.app.app.api.v1.api import api_router
    from tanzanite.backend.app.app.db.tasks import (  # noqa
        close_db_connection,
        connect_to_db,
        prepare_database,
    )
    from tanzanite.core import app_logger
    from tanzanite.core.config import settings
    from tanzanite.webapps.base import api_router as web_app_router
except RuntimeError as err:
    sys.stderr.write(f'{str(err)}\n')
    sys.exit(
        "[-] make sure you have a valid environment configured")


# Ensure .env file is loaded for consistency in behavior with `tz` CLI.
# See `tanzanite/__main__.py`.
load_dotenv()
logger = logging.getLogger(__name__)


def include_routers(app: FastAPI = None):
    """
    Include routers for application.
    """
    logger.debug('[+] including api_router')
    app.include_router(api_router)
    logger.debug('[+] including web_app_router')
    app.include_router(web_app_router)


def configure_static(app: FastAPI = None):
    """
    Mount static content for access by the application.
    """
    logger.debug('[+] configure_static()')
    app.mount("/static", STATIC_FILES, name="static")
    if SPHINX_DOCS_HTML.exists():
        app.mount(
            "/sphinx",
            StaticFiles(
                directory=str(SPHINX_DOCS_HTML),
                html=True
            ),
            name="sphinx"
        )


def custom_openapi():
    """
    Produce a customized OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description=f"This is the {settings.PROJECT_NAME} OpenAPI schema.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/images/d2-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def create_start_app_handler(app: FastAPI) -> Callable:
    """
    Get FastAPI app start handler.
    """
    async def start_app() -> None:
        if os.environ.get('TANZANITE_STARTED_UVICORN') is None:
            app_logger.global_configure_logging(
                log_file='tanzanite-api.log',
            )
        await app_startup(app)
        # await connect_to_db(app)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    """
    Get FastAPI app stop handler.
    """
    async def stop_app() -> None:
        await app_shutdown(app)
        await close_db_connection(app)
    return stop_app


def get_application(debug=True):
    """
    Returns the FastAPI application.

    Customization of the app for branding and other purposes
    is done following the methods described at:

    https://fastapi.tiangolo.com/advanced/extending-openapi/
    https://fastapi.tiangolo.com/tutorial/metadata/
    https://fastapi.tiangolo.com/tutorial/cors/
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        docs_url=None,
        redoc_url=None,
        debug=debug,
    )
    # Add Cross-Origin Resource Sharing middleware.
    if (
        settings.SERVER_NAME not in LOCALHOST
        and settings.BACKEND_CORS_ORIGINS
    ):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                str(origin)
                for origin in settings.BACKEND_CORS_ORIGINS
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    app.add_event_handler(
        "startup",
        create_start_app_handler(app)
    )
    app.add_event_handler(
        "shutdown",
        create_stop_app_handler(app)
    )
    include_routers(app=app)
    configure_static(app=app)
    return app


app = get_application()
app.openapi = custom_openapi


# @app.exception_handler(traceback.TracebackException)
# async def tanzanite_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


# @app.on_event("startup")
async def app_startup(app: FastAPI):
    """
    Ensure the database is initialized and connected.
    """
    logger.debug('[+] app_startup()')
    # app_logger.configure_logging()
    await connect_to_db(app)
    prepare_database()


# @app.on_event("shutdown")
async def app_shutdown(app: FastAPI):
    """
    Ensure the database is disconnected.
    """
    logger.debug('[+] app_shutdown()')
    await close_db_connection(app)


@app.get("/ping", dependencies=[Depends(deps.get_current_user)])
def read_root(
    request: Request,
    # current_user: models.User = Depends(deps.get_current_user),
):
    """
    Return simple data from root path for checking API readiness, etc.
    """
    return {
        "project": settings.PROJECT_NAME,
        "source_ip": request.client.host,
    }


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    favicon_file = TANZANITE_BASE_DIR / FAVICON_PATH
    return FileResponse(favicon_file)


@app.get("/apidocs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Serve local copy of Swagger UI page.
    """
    swagger_ui_html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        # oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/js/swagger-ui-bundle.js",
        swagger_css_url="/static/css/swagger-ui.css",
        swagger_favicon_url=f"/{FAVICON_PATH}"
    )
    return swagger_ui_html


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    """
    Redirect Swagger UI for OAuth2 authentication.
    """
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """
    Serve local copy of ReDoc page.
    """
    redoc_html = get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/js/redoc-standalone.js",
        redoc_favicon_url="/static/images/d2-logo.png"
    )
    return redoc_html


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :

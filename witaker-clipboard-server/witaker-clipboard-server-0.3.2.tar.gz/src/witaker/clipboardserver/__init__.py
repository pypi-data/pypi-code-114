name = "Witaker Clipboard Server"
version = "0.3.2"

from witaker.clipboardserver.clipboard_model import (
    clipboard_content_response,
    clipboard_error_response,
    ClipboardContent,
    ClipboardCopyRequest,
    ClipboardRequestBody,
    ClipboardResponseBody,
    ClipboardText,
    PingResponseBody,
    PingErrorBody,
)

from witaker.clipboardserver.clipboard_util import (
    AuthorizedClipboardUtil,
    AuthorizedClipboardUtilException,
    get_auth_marker,
    get_auth_marker_color,
)

from witaker.clipboardserver.clipboard_server import app

from witaker.clipboardserver.clipboard_server_run import (
    DEFAULT_SERVER_PORT,
    start_flask_webserver,
    start_server_process,
    stop_server_process,
)

from witaker.clipboardserver.clipboard_server_main import (
    add_program_arguments,
    if_version_print_version_and_exit,
    get_port_or_default_port,
    get_auth_key_or_generate_auth_key,
    clipboard_server_cli_main,
    program_version,
    program_version_color
)

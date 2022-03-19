from http.server import HTTPServer, BaseHTTPRequestHandler
from math import ceil
from typing import Optional, List, Union

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import six
from PIL import Image
from plotly.io._base_renderers import ExternalRenderer
from plotly.io._renderers import config
from plotly.subplots import make_subplots

__all__ = ["show_images"]


def show_images(images: List[Union[str, np.ndarray]], cols: Optional[int] = None, imheight: Optional[int] = None):
    """Show images in a Web Browser page.

    Args:
        images: list of str paths to images or numpy array images.
        cols: number of columns of the images grid (if None all images are plotted in a row).
        imheight: force an image height for the plot.
    """
    if cols is None:
        cols = len(images)
    if all([isinstance(i, str) for i in images]):
        titles = [i.split('/')[-1] for i in images]
    else:
        titles = None
    rows = ceil(len(images) / cols)
    fig: go.Figure = make_subplots(rows=rows, cols=cols,
                                   subplot_titles=titles,
                                   horizontal_spacing=min(0.05, (1 / max(1, cols - 1))),
                                   vertical_spacing=min(0.05, (1 / max(1, rows - 1))))
    for i, im in enumerate(images):
        if isinstance(im, str):
            im = Image.open(im)
        elif isinstance(im, np.ndarray):
            im = Image.fromarray(im).convert('RGB')
        else:
            raise NotImplementedError
        if imheight is not None:
            _r = max(im.height, im.width) / im.height
            im.thumbnail((int(imheight * _r), int(imheight * _r)))
        fig.add_trace(px.imshow(im).data[0], row=(i // cols) + 1, col=(i % cols) + 1)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    if imheight is not None:
        fig.update_layout(
            autosize=True,
            width=None,
            height=imheight * rows
        )
    fig.show(renderer="browser-fix")


def open_html_in_browser(html):
    """
    Display html in a web browser without creating a temp file.

    Instantiates a trivial http server and uses the webbrowser module to
    open a URL to retrieve html from that server.

    Parameters
    ----------
    html: str
        HTML string to display
    using, new, autoraise:
        See docstrings in webbrowser.get and webbrowser.open
    """
    if isinstance(html, six.string_types):
        html = html.encode("utf8")

    class OneShotRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            bufferSize = 1024 * 1024
            for i in range(0, len(html), bufferSize):
                self.wfile.write(html[i: i + bufferSize])

        def log_message(self, format, *args):
            # Silence stderr logging
            pass

    server = HTTPServer(("127.0.0.1", 54700), OneShotRequestHandler)
    print(f"Open: http://127.0.0.1:{server.server_port}")
    server.handle_request()


class BrowserRenderer(ExternalRenderer):
    """
    Renderer to display interactive figures in an external web browser.
    This renderer will open a new browser window or tab when the
    plotly.io.show function is called on a figure.

    This renderer has no ipython/jupyter dependencies and is a good choice
    for use in environments that do not support the inline display of
    interactive figures.

    mime type: 'text/html'
    """

    def __init__(
            self,
            config=None,
            auto_play=False,
            using=None,
            new=0,
            autoraise=True,
            post_script=None,
            animation_opts=None,
    ):
        self.config = config
        self.auto_play = auto_play
        self.using = using
        self.new = new
        self.autoraise = autoraise
        self.post_script = post_script
        self.animation_opts = animation_opts

    def render(self, fig_dict):
        from plotly.io import to_html

        html = to_html(
            fig_dict,
            config=self.config,
            auto_play=self.auto_play,
            include_plotlyjs=True,
            include_mathjax="cdn",
            post_script=self.post_script,
            full_html=True,
            animation_opts=self.animation_opts,
            default_width="100%",
            default_height="100%",
            validate=False,
        )
        open_html_in_browser(html)


pio.renderers['browser-fix'] = BrowserRenderer(config=config)

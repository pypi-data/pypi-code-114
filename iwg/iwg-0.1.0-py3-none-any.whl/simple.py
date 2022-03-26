"""
Simple, no configuration site generator module
"""

import logging
import os
import subprocess
from markdown.extensions import wikilinks

from . import _vars
from .errors import InvalidTemplate
from .template import engine, build

logger = logging.getLogger(__name__)
_markdown_extensions = [
    "fenced_code", "footnotes", "tables",
    wikilinks.WikiLinkExtension(base_url="/", end_url=".html")
]


def generate_site(src_dir, dst_dir, template):
    logger.info("Source dir `%s`" % src_dir)
    logger.info("Destination dir `%s`" % dst_dir)
    logger.info("Template name `%s`" % template)

    template_dir = (
        _vars.template_dirs[template]
        if template in _vars.template_dirs
        else template)
    
    if not os.path.exists(template_dir):
        raise FileNotFoundError("Cannot locate template diretory")
    
    if not _is_template_valid(template_dir):
        raise InvalidTemplate()
    
    logger.info(f"Template directory : `{template_dir}`")
    os.makedirs(dst_dir, exist_ok=True)

    # NOTE(bora): Build SCSS files
    # TODO(bora): Make this a feature of theme conf file
    logging.info("Compiling SCSS files...")
    _compile_sass(template_dir, dst_dir)

    template_conf = build.load_tmpl_conf(template_dir)
    if template_conf and "include" in template_conf:
        build.prepare_tmpl(template_dir, dst_dir, template_conf["include"])

    for dirpath, dirnames, filenames in os.walk(src_dir):
        relativepath = os.path.relpath(dirpath, src_dir)
        for it in filenames:
            if it.endswith(".md"):
                filepath = os.path.join(dirpath, it)
                logger.info("Parsing", filepath)
                os.makedirs(os.path.join(dst_dir, relativepath), exist_ok=True)
                infile = filepath
                engine.render(
                    filepath, os.path.join(dst_dir, relativepath),
                    template_dir, labels={"field_2": "BOŞ BIRAKIN"},
                    markdown_ext=_markdown_extensions)
    # TODO: process metadata and content. put them into templates when
    # generating HTML files


def _is_template_valid(template_dir) -> bool:
    """At least an `index` and a `post` layout must be present"""

    index_tmp = os.path.join(template_dir, "views", "index.html")
    post_tmp = os.path.join(template_dir, "views", "post.html")
    return (os.path.exists(index_tmp) and os.path.exists(post_tmp))

def _compile_sass(template_dir: str, dst_dir: str):
    sass_args = r'{SASSCMD} {SASSFLAGS} {SOURCEDIR}\scss:{BUILDDIR}\css'
    sass_flags = r"--style compressed --no-source-map --load-path={BOOTSTRAP}\scss"

    proc_args = sass_args.format(
        SASSCMD=_vars.sass_cmd,
        SOURCEDIR=os.path.abspath(template_dir),
        BUILDDIR=os.path.abspath(dst_dir),
        SASSFLAGS=sass_flags.format(
            BOOTSTRAP=os.path.abspath(
                os.path.join(template_dir, "..", "opt", "bootstrap-5.1.3")))
        ).split()
    returncode = subprocess.call(proc_args)
    if returncode != 0:
        logging.error("SASS command failed!")
        return
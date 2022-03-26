"""
Simple, no configuration site generator module
"""

import re
import os

from . import _vars
from . import parsing
from .errors import InvalidTemplate


def generate(src_dir, dst_dir, template):
    print("Source dir `%s`" % src_dir)
    print("Destination dir `%s`" % dst_dir)
    print("Template name `%s`" % template)
    print()

    template_dir = (
        _vars.template_dirs[template]
        if template in _vars.template_dirs
        else template)
    
    if not os.path.exists(template_dir):
        raise FileNotFoundError("Cannot locate template diretory")
    
    if not _is_template_valid(template_dir):
        raise InvalidTemplate()
    
    print(f"Template directory : `{template_dir}`")

    os.makedirs(dst_dir, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(src_dir):
        relativepath = os.path.relpath(dirpath, src_dir)
        
        for it in filenames:
            if it.endswith(".md"):
                filepath = os.path.join(dirpath, it)
                print("Parsing", filepath)
                
                os.makedirs(os.path.join(dst_dir, relativepath), exist_ok=True)
                parsing._markdown_file_to_html(
                    infile=filepath,
                    outfile=(
                        os.path.splitext(
                            os.path.join(dst_dir, relativepath, it)
                        )[0] + ".html"))
    # TODO: process metadata and content. put them into templates when
    # generating HTML files



def _is_template_valid(template_dir) -> bool:
    index_tmp = os.path.join(template_dir, "views", "index.html")
    post_tmp = os.path.join(template_dir, "views", "post.html")
    return (os.path.exists(index_tmp)
        and os.path.exists(post_tmp))

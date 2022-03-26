import logging
import os
import re
from pathlib import Path

from .. import parsing
from ..errors import LabelWithoutValue
from . import simple_template_layout
from .util import update_dict

logger = logging.getLogger(__name__)


def render(
    document: str,
    out_dir: str,
    template_dir: str,
    labels: dict=None,
    markdown_ext: list=None
) -> None:
    """Builds a single document"""

    if not labels:
        labels = {}
        
    doc_path = Path(document)
    tmpl_path = Path(template_dir).resolve()
    out_path = Path(out_dir).resolve()
    if tmpl_path == out_path:
        raise ValueError("Cannot build in the template directory")
    
    # determine the layout file

    with open(doc_path, encoding="utf-8") as fp:
        metadata, doc_md = parsing.extract_front_matter(fp.read())
        if not metadata:
            metadata = {}
    
    layout = (metadata["layout"]
        if "layout" in metadata
        else "post")
    
    doc_name = os.path.splitext(os.path.basename(doc_path))[0]
    labels = update_dict(labels, {
        "title": (metadata["title"]
            if "title" in metadata
            else doc_name),
        "content": parsing.markdown_to_html(doc_md, markdown_ext)
    })

    if layout == "simple":
        template = simple_template_layout
    else:
        layout_file = tmpl_path / "views" / f"{layout}.html"
        with open(layout_file, encoding="utf-8") as fp:
            template = fp.read()

    def labelrepl(matchobj):
        label = matchobj.group(1) 
        if label in labels:
            return labels[label]
        raise LabelWithoutValue(f"Value for '{label}' label is missing."
            f" (in document '{doc_name}')")

    label_re = re.compile(r"\{\{\s*(.*?)\s*\}\}")

    logger.info("Processing document {doc_path}...")
    
    result = label_re.sub(labelrepl, template)
    outfile = "{}.html".format(
        os.path.splitext(out_path / os.path.basename(doc_path))[0])
    with open(outfile, "w", encoding="utf-8") as fp:
        fp.write(result)

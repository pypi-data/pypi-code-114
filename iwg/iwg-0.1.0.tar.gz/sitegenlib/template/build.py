"""
Tools for building a preview of the template without actual data
"""
import collections.abc
import copy
import logging
import os
import re
import shutil
import pytoml as toml
from pathlib import Path

from ..errors import LabelWithoutValue
from .util import update_dict

logger = logging.getLogger(__name__)


def build_preview(
    template_dir: str,
    output_dir: str,
    labels: dict=None
) -> None:
    template_dir = Path(template_dir).resolve()
    output_dir = Path(output_dir).resolve()
    if template_dir == output_dir:
        raise ValueError("Cannot build in the template directory")
        
    template_conf = load_tmpl_conf(
        template_dir,
        defaults={
            "preview": {
                "index": { "content": "PLACEHOLDER CONTENT" },
                "post": { "content": "PLACEHOLDER CONTENT" }}
        })

    # NOTE(bora): Copy static assets to the destination
    if "include" in template_conf:
        prepare_tmpl(template_dir, output_dir, template_conf["include"])

    # NOTE(bora): Copy views to destination, replacing labels in them
    #   if there are unused labels in configuration give a warning
    #   if value for a label is missing, raise an error

    if labels:
        labels = update_dict(template_conf["preview"], labels)
    else:
        labels = copy.deepcopy(template_conf["preview"])
    
    label_re = re.compile(r"\{\{\s*(.*?)\s*\}\}")
    def labelrepl(matchobj, page):
        label = matchobj.group(1) 
        if page in labels:
            if label in labels[page]:
                return labels[page][label]
        raise LabelWithoutValue(f"Value for '{label}' label is missing. (in page '{page}')")

    for dirpath, _, filenames in os.walk(template_dir / "views"):
        for it in filenames:
            filepath = Path(dirpath) / it
            logger.info(f"Processing template {filepath}...")

            with open(filepath, encoding="utf-8") as fp:
                content = fp.read()
            
            page_name = os.path.splitext(it)[0]
            result = label_re.sub(
                lambda matchobj: labelrepl(matchobj, page_name),
                content)

            destpath = output_dir / it
            with open(destpath, "w", encoding="utf-8") as fp:
                fp.write(result)


def load_tmpl_conf(template_dir: str, defaults: dict=None) -> dict:
    template_dir = Path(template_dir)
    
    conf_path = template_dir / "blogbuster.toml"
    if os.path.exists(conf_path):
        with open(conf_path, encoding="utf-8") as fp:
            template_conf = toml.load(fp)
    else:
        logger.warning(f"Configuration not found in{str(conf_path)}.")
    
    return (update_dict(defaults, template_conf)
            if defaults
            else template_conf)


def prepare_tmpl(
    template_dir: str,
    build_dir: str,
    conf_include: list
) -> None:
    """Basically, copy static assets to the destination"""
    assert (conf_include and isinstance(conf_include, collections.abc.Sequence),
        'Empty "include" config of template')
    
    template_dir = Path(template_dir)
    build_dir = Path(build_dir)

    for incl in conf_include:
        logger.info(f"Copying {incl.get('desc', 'asset')}...")
        cp_from = (template_dir / incl["from"]).resolve()
        cp_to = (build_dir / incl["to"]).resolve()

        if os.path.isdir(cp_from):
            shutil.copytree(cp_from, cp_to, dirs_exist_ok=True)
        elif os.path.exists(cp_from):
            os.makedirs(cp_to, exist_ok=True)
            shutil.copy2(cp_from, cp_to)
        else:
            incl_name = (f"'{incl.get('desc')}'"
                if "desc" in incl
                else "NO DESC")
            logger.warning(f"`{cp_from}` path couldn't resolved "
                f" while processing {incl_name}.")

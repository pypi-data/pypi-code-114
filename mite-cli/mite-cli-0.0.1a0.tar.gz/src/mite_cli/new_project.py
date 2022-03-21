from git import Repo
import os
import logging

logger = logging.getLogger(__name__)


def new_project(project_dir: str):
    if os.path.isdir(project_dir):
        logger.error("Directory already exists, please choose a new directory path")
        return
    Repo.clone_from("https://github.com/ryanlinnit-sky/mite-demo.git", project_dir)

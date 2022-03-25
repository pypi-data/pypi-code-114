import os
import uuid
import yaml
import json
import kubernetes as k
import fire
import subprocess
import hashlib
import bcrypt
import profile
from .log import logger
from .cap_util import get_name_by_email, write_yaml


DEX_CONFIG_FILE = "dex-config.yaml"


def get_yaml_after_append_user(email, hash, user_id, username):
    config_file = DEX_CONFIG_FILE
    with open(config_file) as f:
        docs = yaml.safe_load(f)
        l = docs["staticPasswords"]
        exist = any(r["email"] == email for r in l)
        exist_username = any(r["username"] == username for r in l)
        if exist or exist_username:
            # logger.error(f"{email} already exist in dex. skip it")
            logger.error(f"{email} or {username} is already exist in dex. Delete first")
            # assert not (
            #     exist or exist_username
            # ), f"[{email} or {username}] exist! delete first"
            return None
        item = {
            "email": email,
            "hash": hash,
            "userID": user_id,
            "username": username,
        }
        l.append(item)
        return docs


def get_yaml_after_delete_user(email):
    config_file = DEX_CONFIG_FILE
    with open(config_file) as f:
        docs = yaml.safe_load(f)
        l = docs["staticPasswords"]
        nl = [item for item in l if item["email"] != email]
        docs["staticPasswords"] = nl
        return docs


class DexCommand(object):
    def save_dex_configmap_to_file(self):
        cmd = (
            "kubectl get configmap dex -n auth -o jsonpath='{.data.config\.yaml}' > %s"
            % DEX_CONFIG_FILE
        )
        logger.debug(cmd)
        ret = subprocess.call(cmd, shell=True)

    def _ready_dex_after_append_user(self, email, password, username):
        logger.debug("ready_dex_after_append_user")
        self.save_dex_configmap_to_file()
        password = str(password)
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
        user_id = str(uuid.uuid4())
        body = get_yaml_after_append_user(email, hashed, user_id, username)
        if body:
            write_yaml(body, DEX_CONFIG_FILE)
            return True
        return False

    def _ready_dex_after_delete_user(self, email, username):
        logger.debug("ready_dex_after_delete_user")
        self.save_dex_configmap_to_file()
        body = get_yaml_after_delete_user(email)
        if body:
            write_yaml(body, DEX_CONFIG_FILE)
            return True
        return False

    def apply(self):
        logger.debug("apply")
        cmd = (
            """kubectl create configmap dex --from-file=config.yaml=%s -nauth --dry-run -oyaml | kubectl apply -f -  && kubectl rollout restart deployment dex -nauth"""
            % DEX_CONFIG_FILE
        )
        logger.debug(cmd)
        ret = subprocess.call(cmd, shell=True)
        logger.debug(f"kubectl apply result: {ret}")

    def add(self, email, password, username):
        logger.debug("add")
        success = self._ready_dex_after_append_user(email, password, username)
        if success:
            self.apply()
            self.delete_yaml()
            return True
        else:
            logger.error("Add dex fail")
            return False

    def delete(self, email, username=None):
        logger.debug("delete")
        if not username:
            username = get_name_by_email(email)
        success = self._ready_dex_after_delete_user(email, username)
        if success:
            self.apply()
            self.delete_yaml()
            return True
        else:
            logger.error("Delete dex fail")
            return False

    def change_password(self, email, password):
        logger.debug("change_password")
        username = get_name_by_email(email)
        if not username:
            logger.error(f"User {email} is not found. Please check the email")
            return
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
        user_id = str(uuid.uuid4())

        self.save_dex_configmap_to_file()
        docs = get_yaml_after_delete_user(email)
        l = docs["staticPasswords"]
        item = {
            "email": email,
            "hash": hash,
            "userID": user_id,
            "username": username,
        }
        l.append(item)
        write_yaml(docs, DEX_CONFIG_FILE)
        self.apply()

    def delete_yaml(self):
        os.remove(DEX_CONFIG_FILE)

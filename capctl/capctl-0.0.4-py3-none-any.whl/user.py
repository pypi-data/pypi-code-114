import subprocess
from terminaltables import AsciiTable

from capctl.kfp_proxy import KfpProxyCommand
from .log import logger
from .cap_util import (
    get_sumup,
    get_name_by_email,
)
from .profile import ProfileCommand
from .dex import DexCommand
from .cap_util import run_command


class UserCommand(object):
    """
    Manage Users. You can create, list, change password, and delete users
    """

    def ls(self):
        sumup = get_sumup()
        rows = [
            [
                x["email"],
                x["dex"],
                ",".join(x["owners"]),
                ",".join(x["members"]),
            ]
            for k, x in sumup.items()
        ]
        header = [["email", "dex", "owners", "members"]]
        table = AsciiTable(header + rows)
        print(table.table)

    def add(self, email, password, username):
        if DexCommand().add(email, password, username):
            ProfileCommand().add(email, username)
            KfpProxyCommand().add(email, username)
            cmd = ["kubectl", "label", "ns", username, "cap-credential=sync"]
            _, err, ret = run_command(cmd)
            if ret != 0:
                logger.error(err)
        else:
            logger.error("Failed to add user")

    def password(self, email, password):
        DexCommand().change_password(email, password)

    def delete(self, email):
        username = get_name_by_email(email)
        if not username:
            logger.error(f"Failed to delete user: {email} not exist.")
            return
        if DexCommand().delete(email, username):
            ProfileCommand().delete(username)
            KfpProxyCommand().delete(username)
        else:
            logger.error(f"Failed to delete user {email}")
        # if email:
        #     kebab_email = email.replace("@", "-").replace(".", "-")
        #     name = f"user-{kebab_email}-clusterrole-edit"
        #     cmd = f"kubectl delete rolebinding --all-namespaces --field-selector metadata.name={name}"
        #     logger.debug(cmd)
        #     ret = subprocess.call(cmd, shell=True)
        #     logger.debug(f"kubectl result: {ret}")
        #     cmd = f"kubectl delete servicerolebinding --all-namespaces --field-selector metadata.name={name}"
        #     logger.debug(cmd)
        #     ret = subprocess.call(cmd, shell=True)
        #     cmd = f"kubectl delete servicerolebinding --all-namespaces --field-selector metadata.name={name}"
        #     logger.debug(f"kubectl result: {ret}")

import os
from sanic import Sanic
from sanic.response import json, file

import pyusermanager
from pyusermanager import *
from pyusermanager.Config import *
from pyusermanager.Config.db_providers import *
import pyusermanager.Token as Token


async def version(request):
    return json({"version": pyusermanager.__version__})


async def is_logged_in(app, token: str, ip="127.0.0.1"):
    """This Function checks if a user is logged in"""

    try:
        auth_token = Token.Auth(app.ctx.cfg, token)
        success = auth_token.verify(ip)
        return success, auth_token.username
    except Exception as err:
        print(err)
        return False, ""


async def is_in_group_by_name(app, username: str, group: str):
    """checks if a user is in the specified group"""

    try:
        found_user = user(app.ctx.cfg, username)
        userinfo = found_user.info_extended()
        if group in userinfo["perms"]:
            return True
    except Exception as err:
        pass

    return False


async def is_in_group(app, token: str, group: str):
    """checks if a user is in the specified group"""

    try:
        auth_token = Token.Auth(app.ctx.cfg, token)
        auth_token.get_user()
        user_dict = user(app.ctx.cfg, auth_token.username).info_extended()
        print(user_dict)
        if group in user_dict["perms"]:
            return True
    except Exception as err:
        return False

    return False


async def get_avatar(request, avatarname):
    app = request.app

    avatarlist = os.listdir(app.ctx.cfg.avatar_folder)

    if avatarname in avatarlist:
        return await file(f"{app.ctx.cfg.avatar_folder}/{avatarname}")
    else:
        return await file(f"{app.ctx.cfg.avatar_folder}/404.png")


async def create_user(app, password, username, email):
    user(app.ctx.cfg, username).create(password, email=email)

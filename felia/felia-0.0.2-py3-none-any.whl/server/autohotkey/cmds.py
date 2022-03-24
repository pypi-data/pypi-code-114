import logging

from django.conf import settings
from .constant import KEYBOARD_KEYS


class Cmd:
    """所有ahk命令的基类"""
    name = None
    ahk = None

    def __str__(self):
        return self.render()

    def render(self):
        raise NotImplemented("渲染结果实现")

    def contribute_to_class(self, cls, name):
        """注册ahk命令行到AHK类"""
        self.ahk = cls
        self.name = name
        cls._meta.add_field(self)


class HotKey(Cmd):
    def __new__(cls, *args, **kwargs):
        if len(args) > 1:
            action = args[1]
        else:
            action = kwargs['action']
        if callable(action):
            from server.autohotkey.registry import files
            # 使用logging打印注册的函数名称
            files.register_func(action)
        return super().__new__(cls)

    def __init__(self, key, action, linebreak=False, help_text=None):
        self.key = key
        self.action = action() if isinstance(action, type) else action
        self.linebreak = linebreak
        self.help_text = help_text
        self.text = None

    def setup(self):
        self.text = self.render()

    @property
    def to_readable_key(self):
        if isinstance(self.key, list | tuple):
            return ' + '.join(self.key)
        else:
            new_dict = {k: v for k, v in zip(KEYBOARD_KEYS.values(), KEYBOARD_KEYS.keys())}
            key = []
            for s in self.key:
                if s == "&":
                    continue
                key.append(new_dict.get(s, s))
        return ' + '.join(key)

    @property
    def to_ahk_key(self):
        if isinstance(self.key, list | tuple):
            key = ""
            for k in self.key:
                key += str(KEYBOARD_KEYS.get(k, k))
        else:
            key = self.key
        return key

    @property
    def to_ahk_action(self):
        if callable(self.action):
            exe = (settings.BASE_DIR / 'autohotkey' / 'bin' / 'client.exe').as_posix()
            return f"Run, {exe} callpython {self.action.__name__}"
        return self.action

    def render(self):
        return f"{self.to_ahk_key}::{self.to_ahk_action}"


class Run(Cmd):
    def __init__(self, target):
        self.target = target

    def render(self):
        return f"Run, {self.target}"


class Send(Cmd):
    def __init__(self, keys):
        self.keys = keys

    def render(self):
        return f"Send, {self.keys}"


class Pause(Cmd):
    """暂停脚本"""
    def render(self):
        return "Pause"


class Reload(Cmd):
    """重新加载脚本"""
    def render(self):
        return "Reload"

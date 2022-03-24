from django.db.models.base import _has_contribute_to_class

from server.autohotkey.options import Options
from server.autohotkey.registry import files


class AHKBase(type):
    """所有.ahk的元类, 该实现模仿Django的ModelBase"""
    def __new__(mcs, name, bases, attrs, **kwargs):
        # 只对AHK的子类执行初始化
        super_new = super().__new__
        parents = [b for b in bases if isinstance(b, AHKBase)]
        if not parents:
            return super_new(mcs, name, bases, attrs)

        attr_meta = attrs.pop('Meta', None)

        new_class = super_new(mcs, name, bases, attrs, **kwargs)

        meta = attr_meta or getattr(new_class, 'Meta', None)
        # 处理ahk文件的可选项
        new_class.add_to_class('_meta', Options(meta))

        setattr(new_class, 'hotkeys', [])
        new_class.add_hotkeys()
        for obj in new_class.hotkeys:
            obj.contribute_to_class(new_class, None)

        files.register_file(new_class)
        return new_class

    def add_to_class(cls, name, value):
        if _has_contribute_to_class(value):
            value.contribute_to_class(cls, name)
        else:
            setattr(cls, name, value)


class AHK(metaclass=AHKBase):
    """.ahk文件，默认在cli.ahk中将被#Include指令导入


    :Example:

    def showinfo():
        from tkinter import messagebox
        messagebox.showinfo("callpython测试", ".ahk调用python函数!")


    class Example(AHK):

        @classmethod
        def add_hotkeys(cls):
            cls.add_hotkey(["Ctrl", "j"], cmds.Send("My First Script"))
            cls.add_hotkey(["Ctrl", "p"], showinfo)
    """

    def __init__(self):
        self.opts: Options = self._meta

    @classmethod
    def add_hotkey(cls, key, action, linebreak=False, help_text=None):
        from server.autohotkey import cmds
        cls.hotkeys.append(cmds.HotKey(key,
                                       action,
                                       linebreak=linebreak,
                                       help_text=help_text)
                           )

    @classmethod
    def add_hotkeys(cls):
        """自定义hotkey"""
        pass



import logging

from django.conf import settings

from server.autohotkey import cmds, AHK
from server.autohotkey.constant import Mode_Switch

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


_document = settings.BASE_DIR.parent / 'doc' / 'build' / 'hotkey.list.html'


class Default(AHK):

    class Meta:
        help_text = "pyhotkey内置的热键"

    @classmethod
    def add_hotkeys(cls):
        cls.add_hotkey("!1",
                       cmds.Run("https://wyagd001.github.io/zh-cn/docs/AutoHotkey.htm"),
                       help_text="autohotkey文档")
        cls.add_hotkey("!2",
                       cmds.Run("https://docs.python.org/zh-cn/3/"),
                       help_text="Python文档")
        cls.add_hotkey("!3",
                       cmds.Run("https://v3.cn.vuejs.org/"),
                       help_text="Vue3文档")
        cls.add_hotkey("!4", cmds.Run("https://www.typescriptlang.org/zh/docs/"),
                       help_text="TypeScript文档")
        cls.add_hotkey("!5", cmds.Run("https://docs.docker.com/"),
                       help_text="Docker")
        cls.add_hotkey("!6",
                       cmds.Run("https://golang.google.cn/"),
                       help_text="Golang文档")
        cls.add_hotkey("!7", cmds.Run("https://commonmark.org/help/"),
                       help_text="markdown语法学习")
        cls.add_hotkey("!8",
                       cmds.Run("https://github.com/jobbole/awesome-python-cn"),
                       help_text="awesome python")
        cls.add_hotkey("!9",
                       cmds.Run("https://github.com/jobbole/awesome-go-cn"),
                       help_text="awesome go")
        cls.add_hotkey("!0", cmds.Run("https://oschina.gitee.io/learn-git-branching/"),
                       help_text="Git命令学习")


class Python(AHK):
    class Meta:
        help_tet = "Python拓展"

    @classmethod
    def add_hotkeys(cls):
        cls.add_hotkey("!1",
                       cmds.Run("https://docs.djangoproject.com/zh-hans/4.0/"),
                       help_text="django文档")
        cls.add_hotkey("!2",
                       cmds.Run("https://www.sphinx-doc.org/en/master/contents.html"),
                       help_text="sphinx文档")
        cls.add_hotkey("!3",
                       cmds.Run("http://supervisord.org/"),
                       help_text="supervisor文档")


class Golang(AHK):
    class Meta:
        help_text = "Go拓展"

    @classmethod
    def add_hotkeys(cls):
        cls.add_hotkey("!1",
                       cmds.Run("https://pkg.go.dev/github.com/spf13/cobra@v1.4.0"),
                       help_text="cobra(命令行接口)")
        cls.add_hotkey("!2",
                       cmds.Run("https://github.com/chromedp/chromedp"),
                       help_text="chromedp(web自动化)")
        cls.add_hotkey("!3",
                       cmds.Run("https://www.grpc.io/docs/languages/go/quickstart/"),
                       help_text="gRPC")


class Vue(AHK):
    class Meta:
        help_text = "Vue拓展"

    @classmethod
    def add_hotkeys(cls):
        cls.add_hotkey("!1", cmds.Run("https://v2.vuepress.vuejs.org/zh/"),
                       help_text="VuePress文档")










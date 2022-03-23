import json
import os
from pathlib import Path
from typing import Iterable, List
from collections import OrderedDict

import typer
import click
from click import Context

import questionary
from questionary import Style
import pydoc

from git import Git
import pyperclip
import subprocess
from git.repo import Repo

# 理论上应该搞个模板来解析，为了方便直接硬编码了
# <type>: <subject>
# <BLANK LINE>
# <body>
# <BLANK LINE>
# <doc>

TYPE: OrderedDict = OrderedDict({
    "feat": "增加新的Feature",
    "fix": "修复Bug",
    "pref": "提高性能的代码更改",
    "refactor": "既不是修复bug也不是增加新Feature的代码重构",
    "style": "不影响代码含义的修改, 比如空格、格式化、缺失的分号等",
    "test": "增加确实的测试或者矫正已存在的测试",
    "docs": "仅对注释的修改",
    "build": "对构建系统或者外部依赖项进行了修改",
    "ci": "对CI配置文件或脚本进行了修改",
    "chore": "不修改 src 或者 test 的其余修改（一些苦力活），例如辅助工具的变动",
    "revert": "回滚到某个 commit 的提交"
})

# 缓存路径

CACHE_FILE_PATH = str(Path.home()) + '/Library/Caches/awemecommit'
CACHE_NAME = '/awemecommit_cache.json'

# 缓存
DEFAULT_CACHE = {
    'type': '',
    'scope': '',
    'subject': '',
    'body': '',
    'doc': ''
}


class OrderedCommands(click.Group):
    def list_commands(self, ctx: Context) -> Iterable[str]:
        # 修改command默认顺序
        return ['commit', 'owncommit']


app = typer.Typer(cls=OrderedCommands, help='commit message 辅助工具')


def avoid_keyboard_interrupts(ret):
    if ret is None:
        raise typer.Abort()


def safe_run_git(lambda_expr):
    try:
        lambda_expr()
    except Exception as e:
        typer.secho(e.stdout,
                    fg=typer.colors.RED, err=True)
        typer.secho(e.stderr,
                    fg=typer.colors.RED, err=True)
        typer.secho("git 出错, 请查看以上报错信息",
                    fg=typer.colors.RED, err=True)
        raise typer.Abort()


@app.command(help='用规范的 message 提交 commit')
def commit(message: str = typer.Option('', '--message', '-m', hidden=True),
           multi: bool = typer.Option(
               False, '--gits', '-g', help='多仓创建 commit'),
           clipboard: bool = typer.Option(
               False, '--clipboard', '-c', help='将 commit message 复制到剪切板'),
           push: bool = typer.Option(
               False, '--push', '-p', help='创建 commit 后直接push')
           ):
    if message != '':
        typer.secho('禁止使用 --message 提交消息, 请使用本工具生成 commit message!',
                    fg=typer.colors.RED, err=True)
        raise typer.Abort()

    gits: List[Git] = []
    parent_folder = os.getcwd()
    current_branch: str = None

    top_git_path = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'], capture_output=True).stdout.decode().strip()
    # git 相关
    if not multi:
        if top_git_path == '':
            typer.secho('不在 git 目录中!',
                        fg=typer.colors.RED, err=True)
            raise typer.Abort()
        gits = [Repo(top_git_path).git]

        os.chdir(top_git_path)
        os.chdir('..')
        parent_folder = os.getcwd()

        current_branch = Repo(top_git_path).git.branch('--show-current')
        if current_branch == '':
            typer.secho(f'{top_git_path} HEAD is Detected, 请检查后操作',
                        fg=typer.colors.GREEN)
            raise typer.Abort()
    else:
        # 在子仓目录下
        if top_git_path != '':
            os.chdir(top_git_path)
            os.chdir('..')
        parent_folder = os.getcwd()
        # 可能在多仓文件夹中
        paths: List[str] = []
        for path in [f.path for f in os.scandir(os.getcwd()) if f.is_dir()]:
            os.chdir(path)
            if subprocess.run(
                    ['git', 'rev-parse', '--show-toplevel'], capture_output=True).stdout.decode().strip() == path:
                paths.append(path)

        if len(paths) == 0:
            typer.secho('无法找到 Git 仓库', fg=typer.colors.RED, err=True)
            raise typer.Abort()
        os.chdir(parent_folder)

        for path in paths:
            if Repo(path).git.branch('--show-current') == '':
                typer.secho(f'{path} HEAD is Detected, 请单独操作!',
                            fg=typer.colors.YELLOW)
            else:
                gits.append(Repo(path).git)

        # 检查多仓 branch 是否同步
        for git in gits:
            possible_branch = git.branch('--show-current')
            if current_branch is None:
                current_branch = possible_branch
            elif current_branch != possible_branch:
                typer.secho('多仓分支不一致, 请检查',
                            fg=typer.colors.RED, err=True)
                raise typer.Abort()

    # 缓存输入过的信息
    cached_json = DEFAULT_CACHE
    cached_file_path = CACHE_FILE_PATH + CACHE_NAME

    if not os.path.exists(CACHE_FILE_PATH):
        os.mkdir(CACHE_FILE_PATH)

    if not os.path.exists(cached_file_path):
        open(cached_file_path, 'w+').close()

    try:
        all_cached_json = json.load(open(cached_file_path, 'r'))
    except json.decoder.JSONDecodeError:
        all_cached_json = {}

    def save_cached_json():
        with open(cached_file_path, 'w+') as f:
            if parent_folder not in all_cached_json:
                all_cached_json[parent_folder] = {}
            all_cached_json[parent_folder][current_branch] = cached_json
            json.dump(all_cached_json, f)

    if os.path.exists(cached_file_path) and parent_folder in all_cached_json and current_branch in all_cached_json[parent_folder]:
        cached_json = all_cached_json[parent_folder][current_branch]
        for key in DEFAULT_CACHE.keys():
            if key not in cached_json:
                cached_json[key] = ''
    else:
        save_cached_json()

    # 查看此时是否有 changes added to commit
    working_git = []
    for git in gits:
        if git.diff('--name-only', '--cached').strip() != '':
            working_git.append(git)
    if len(working_git) == 0:
        typer.secho('nothing to commit, working tree clean',
                    fg=typer.colors.RED, err=True)
        raise typer.Abort()

    for git in working_git:
        typer.secho(f'即将 Commit 的仓库:{git.rev_parse("--show-toplevel")}',
                    fg=typer.colors.GREEN)
    # 生成 commit_message

    def get_commit_message():
        commit_type_str = cached_json['type'] + ':' + \
            TYPE[cached_json['type']
                 ] if cached_json['type'] != '' else ''
        scope = cached_json['scope']
        subject = cached_json['subject']
        body = cached_json['body']
        doc = cached_json['doc']
        commit_message = ''
        while True:
            commit_type_str: str = questionary.select('请选择你的 commit 类型:', choices=[f'{k}:{v}' for k, v in TYPE.items()],
                                                      qmark='', instruction='使用↑↓选择', style=Style([
                                                          ('highlighted',
                                                           f'fg:{typer.colors.GREEN} bold'),
                                                          ('instruction', 'bold'),
                                                          ('answer',
                                                              f'fg:{typer.colors.YELLOW} bold'),
                                                      ]), default=(None if commit_type_str == '' else commit_type_str)).ask()
            avoid_keyboard_interrupts(commit_type_str)
            commit_type = commit_type_str.split(':')[0]
            cached_json['type'] = commit_type
            save_cached_json()

            scope: str = questionary.text('请输入改动的范围, 如上线预期版本等信息, 用 - 分割, 可省略\n e.g. 20.0.0-信息流:', qmark='', style=Style([
                ('answer',
                 f'fg:{typer.colors.YELLOW} bold')
            ]), default=scope).ask()
            avoid_keyboard_interrupts(scope)
            cached_json['scope'] = scope
            save_cached_json()

            subject = questionary.text('请输入本次修改的简洁描述, 如需求名, 修复的Bug等\n e.g. 抖音图文广告:', qmark='', style=Style([
                ('answer',
                 f'fg:{typer.colors.YELLOW} bold'),
            ]), default=subject, validate=lambda val: len(val) > 0).ask()
            avoid_keyboard_interrupts(subject)
            cached_json['subject'] = subject
            save_cached_json()

            body_confirm = questionary.confirm(
                '是否有额外信息需要补充, 如修改了哪些组件, 有哪些不兼容的修改, 遗留了哪些问题:', qmark='', default=False, style=Style([
                    ('answer',
                     f'fg:{typer.colors.YELLOW} bold'),
                ])).ask()
            avoid_keyboard_interrupts(body_confirm)

            if body_confirm:
                body = questionary.text('补充额外信息:', qmark='', multiline=True, instruction='(结束请输入 Esc 然后输入 Enter)\n', style=Style([
                    ('answer',
                        f'fg:{typer.colors.YELLOW} bold'),
                ]), default=body).ask().strip()
                avoid_keyboard_interrupts(body)
                cached_json['body'] = body
                save_cached_json()

            doc = questionary.text('技术文档、Meego链接或Bug链接:', qmark='', style=Style([
                ('answer',
                 f'fg:{typer.colors.YELLOW} bold'),
            ]), default=doc).ask().strip()
            avoid_keyboard_interrupts(doc)
            cached_json['doc'] = doc
            save_cached_json()

            commit_message = commit_type + ('' if scope == '' else f'({scope})') + ': ' + subject
            if body != '':
                commit_message += f'\n\n{body}\n'
            if doc != '':
                commit_message += f'\ndoc: {doc}'
            all_confirm = questionary.confirm('确认以上 commit message?', qmark='', default=True, style=Style([
                ('answer',
                 f'fg:{typer.colors.YELLOW} bold'),
            ])).ask()
            avoid_keyboard_interrupts(all_confirm)
            if all_confirm:
                break
        return commit_message
    commit_message = get_commit_message()

    # copy 到剪切板
    if clipboard:
        pyperclip.copy(commit_message)
        typer.secho('commit 信息已复制到剪切板!',
                    fg=typer.colors.GREEN)
        continue_commit = questionary.confirm(
            '是否要继续提交此commit', qmark='', default=True, style=Style([
                ('answer',
                 f'fg:{typer.colors.YELLOW} bold'),
            ])).ask()
        avoid_keyboard_interrupts(continue_commit)
        if not continue_commit:
            raise typer.Exit()

    for git in working_git:
        try:
            safe_run_git(lambda: git.commit('-m', commit_message))
        except typer.Abort():
            continue
        typer.secho(
            f'{git.rev_parse("--show-toplevel")} commit 完成!', fg=typer.colors.GREEN)

    if push:
        for git in working_git:
            try:
                safe_run_git(lambda: git.push())
            except typer.Abort():
                continue
            typer.secho(
                f'{git.rev_parse("--show-toplevel")} push 完成!', fg=typer.colors.GREEN)


@ app.command(help='查看目前分支上所有新增的 commit, 但不包含 merge 来的')
def owncommit(branch: str = typer.Option('develop', '--branch', '-b', help='作比较的分支')):
    top_git_path = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'], capture_output=True).stdout.decode().strip()
    if top_git_path == '':
        typer.secho('不在 git 目录中!',
                    fg=typer.colors.RED, err=True)
        raise typer.Abort()
    git = Repo(top_git_path).git
    current_branch = git.branch('--show-current')
    safe_run_git(lambda: pydoc.pager(git.log(f'{branch}..{current_branch}',
                                             '--first-parent', '--no-merges')))


if __name__ == '__main__':
    app()


from PyQt5 import QtWidgets, uic

from PyQt5.QtCore import QObject, QThread, pyqtSignal

from lyberry_qt import helpers
from lyberry_api import settings
from lyberry_qt.comment_screen import CommentWidget, WriteCommentWidget

from datetime import datetime
import re

def open_external(pub):
    file_type = pub.media_type.split('/')[0]
    if file_type == 'video' or file_type == 'audio':
        helpers.make_chapter_file(pub)
        settings.media_player(pub.streaming_url)
    elif file_type == 'text':
        settings.text_viewer(pub.streaming_url)

class PubScreen(QtWidgets.QDialog):
    change_url = pyqtSignal(str)
    def __init__(self, window, pub):
        super(PubScreen, self).__init__()
        uic.loadUi(helpers.relative_path('designer/pub.ui'), self)
        self._window = window
        self.pub = pub
        self._lbry = pub._LBRY_api
        self.title_label.setText(self.pub.title)
        self.url = pub.url
        self.license_label.setText(f"License: {pub.license}")
        timestamp = datetime.fromtimestamp(pub.timestamp)
        self.date_label.setText(f"Date: {timestamp}")
        desc = helpers.fix_markdown(self.pub.description)
        self.description_label.setText(desc)
        self.description_label.linkActivated.connect(self.change_url.emit)
        self.channel_button.setText(self.pub.channel.name)
        self.channel_button.clicked.connect(lambda: self.change_url.emit(self.pub.channel.url))
        self.amt = 1
        self.comments = []
        self.comments_button.clicked.connect(self.more_comments)
        self.write_comment_button.clicked.connect(self.write_comment)
        self.open_button.clicked.connect(self.open)
        self.finished.connect(self.pub.refresh_comments_feed)
        self.play_thread = QThread()

    def write_comment(self):
        self.writing_section = WriteCommentWidget(self)
        self.write_comment_section.addWidget(self.writing_section)
        self.write_comment_button.setEnabled(False)
        self.writing_section.finished.connect(lambda: 
            self.write_comment_button.setEnabled(True))
    
    def open(self):
        self.play_thread.exit()
        self.opener = helpers.Loader()
        self.opener.set_func(lambda: open_external(self.pub))
        self.opener.moveToThread(self.play_thread)
        self.play_thread.started.connect(self.opener.run)
        self.opener.finished.connect(self.opener.deleteLater)
        self.play_thread.start()

    def show_comment(self, comment):
        item = CommentWidget(comment)
        item.channel_button.clicked.connect(lambda: self.change_url.emit(comment.channel.url))
        item.change_url.connect(self.change_url.emit)
        self.comments.append(item)
        self.comments_section.addWidget(item, self.amt, 0, 1, 1)
        self.amt += 1
    
    def list_comments(self, comments):
        for comment in comments:
            self.show_comment(comment)
        self.fix_comment_button()

    def fix_comment_button(self):
        self.comments_section.addWidget(self.comments_button)
        self.comments_button.setEnabled(True)

    def more_comments(self):
        self.comments_button.setEnabled(False)
        self.comment_worker = helpers.FeedUpdater()
        self.comment_worker.set_feed(self.pub.comments_feed)
        self.comment_worker.moveToThread(self._window.comment_thread)
        self._window.comment_thread.started.connect(self.comment_worker.run)
        self.comment_worker.progress.connect(self.show_comment)
        self.comment_worker.finished.connect(self.fix_comment_button)
        self.comment_worker.finished.connect(self.comment_worker.deleteLater)
        self.comment_worker.finished.connect(self._window.comment_thread.quit)
        self.scrollArea.ensureWidgetVisible(self.comments_button)
        self._window.comment_thread.start()


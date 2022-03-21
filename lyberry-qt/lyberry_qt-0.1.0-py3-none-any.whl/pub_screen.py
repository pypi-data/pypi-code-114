
from PyQt5 import QtWidgets, uic

from PyQt5.QtCore import QObject, QThread, pyqtSignal

from lyberry_qt import helpers
from lyberry_api import settings
from lyberry_qt.comment_screen import CommentWidget, WriteCommentWidget

from datetime import datetime

def open_external(pub):
    file_type = pub.media_type.split('/')[0]
    if file_type == 'video' or file_type == 'audio':
        helpers.make_chapter_file(pub)
        settings.media_player(pub.streaming_url)
    elif file_type == 'text':
        settings.text_viewer(pub.streaming_url)

class PubScreen(QtWidgets.QDialog):
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

        self.description_label.setText(self.pub.description.replace('\n', '\n\n'))

        self.channel_button.setText(self.pub.channel.name)
        self.channel_button.clicked.connect(lambda: self._window.show_channel(self.pub.channel))

        self.amt = 1
        self.comments = []
        self.comments_button.clicked.connect(self.more_comments)

        self.write_comment_button.clicked.connect(self.write_comment)

        self.open_thread = QThread()
        self.open_on(self.open_thread)
        self.open_button.clicked.connect(self.open_thread.start)

        self.comment_thread = QThread()
        self.finished.connect(self.pub.refresh_comments_feed)

    def write_comment(self):
        self.writing_section = WriteCommentWidget(self)
        self.write_comment_section.addWidget(self.writing_section)
        self.write_comment_button.setEnabled(False)
        self.writing_section.finished.connect(lambda: 
            self.write_comment_button.setEnabled(True)
            )
    
    def open_on(self, play_thread):
        self.opener = Loader()
        self.opener.set_func(self.open)
        self.opener.moveToThread(play_thread)
        play_thread.started.connect(self.opener.run)
        self.opener.finished.connect(self.opener.deleteLater)

    def open(self):
        open_external(self.pub)

    def show_comment(self, comment):
        item = CommentWidget(comment)
        item.channel_button.clicked.connect(lambda: self._window.show_channel(comment.channel))
        self.comments.append(item)
        self.comments_section.addWidget(item, self.amt, 0, 1, 1)
        self.amt += 1
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    
    def list_comments(self, comments):
        for comment in comments:
            self.show_comment(comment)
        self.fix_comment_button()

    def fix_comment_button(self):
        self.comments_section.addWidget(self.comments_button)
        self.scrollArea.ensureWidgetVisible(self.comments_button)

    def more_comments(self):
        self.comments_button.setEnabled(False)
        self.comment_worker = helpers.FeedUpdater()
        self.comment_worker.set_feed(self.pub.comments_feed)
        self.comment_worker.moveToThread(self.comment_thread)
        self.comment_thread.started.connect(self.comment_worker.run)
        self.comment_worker.finished.connect(self.list_comments)
        self.comment_worker.finished.connect(self.comment_worker.deleteLater)
        self.comment_worker.finished.connect(self.comment_thread.quit)
        self.comment_thread.finished.connect(
                lambda: self.comments_button.setEnabled(True)
        )
        self.comment_thread.start()

class Loader(QObject):
    finished = pyqtSignal()
    def set_func(self, func):
        self.func = func
    def run(self):
        self.func()
        self.finished.emit()


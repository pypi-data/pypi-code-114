from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from lyberry_qt import helpers

class CommentWidget(QtWidgets.QDialog):
    change_url = pyqtSignal(str)
    def __init__(self, comment):
        super(CommentWidget, self).__init__()
        uic.loadUi(helpers.relative_path('designer/comment.ui'), self)
        self.comment = comment
        self.pub = comment.pub
        self._lbry = comment._LBRY_api
        self.message.setText(helpers.fix_markdown(self.comment.msg))
        self.message.linkActivated.connect(self.change_url.emit)
        self.channel_button.setText(comment.channel.name)
        self.show_replies_button.setText(str(comment.replies_amt) + " Replies")
        self.show_replies_button.clicked.connect(self.show_replies)
        self.show_replies_button.setEnabled(comment.replies_amt > 0)
        self.write_comment_button.clicked.connect(self.write_comment)

    def write_comment(self):
        self.writing_section = WriteCommentWidget(self, self.comment)
        self.write_comment_section.addWidget(self.writing_section)
        self.write_comment_button.setEnabled(False)
        self.writing_section.finished.connect(lambda: 
            self.write_comment_button.setEnabled(True)
            )
    
    def show_replies(self):
        for comment in self.comment.replies:
            item = CommentWidget(comment)
            self.replies_section.addWidget(item)
        self.show_replies_button.setEnabled(False)

class WriteCommentWidget(QtWidgets.QDialog):
    def __init__(self, parent, comment=None):
        super(WriteCommentWidget, self).__init__()
        uic.loadUi(helpers.relative_path('designer/write_comment.ui'), self)
        self.create_comment_button.clicked.connect(self.create_comment)
        self.parent = parent
        self.comment = comment
        self.add_my_channels_as_comment_options()
    
    def add_my_channels_as_comment_options(self):
        my_channels = self.parent._lbry.my_channels
        for channel in my_channels:
            self.channel_select.addItem(channel.name)

    def create_comment(self):
        channel_name = self.channel_select.currentText()
        channel = self.parent._lbry.channel_from_uri(channel_name)
        message = self.comment_box.toPlainText()
        self.parent._lbry.make_comment(channel, message, self.parent.pub, self.comment)
        self.comment_box.clear()
        self.close()


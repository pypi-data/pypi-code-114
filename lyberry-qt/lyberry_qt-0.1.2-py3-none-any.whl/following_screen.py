from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from lyberry_qt import helpers
import lyberry_api.channel

class ListScreen(QtWidgets.QDialog):
    change_url = pyqtSignal(str)
    def __init__(self, window):
        super(ListScreen, self).__init__()
        self._window = window

    def setup(self):
        self.title_label.setText(self.title)
        self.load_more_button.clicked.connect(self.more)
        self.amt = 2
        self.width = 2
        self.items = []
        self.more()

    def new_pub(self, pub):
        item = PubWidget(pub)
        if type(pub) == lyberry_api.channel.LBRY_Channel:
            item.title.clicked.connect(lambda: self.change_url.emit(pub.url))
            item.channel.clicked.connect(lambda: self.change_url.emit(pub.url))
        else:
            item.title.clicked.connect(lambda: self.change_url.emit(pub.url))
            item.channel.clicked.connect(lambda: self.change_url.emit(pub.channel.url))
        self._window.img_url_to_label(pub.thumbnail, item.thumbnail)
        self.items.append(item)

        self.pub_thumb_grid_layout.addWidget(item, self.amt // self.width, self.amt % self.width, 1, 1)
        self.amt += 1
        return item.pub_grid
    
    def get_images_and_fix_button(self, pubs):
        for thread in self._window.img_threads:
            thread.start()
        self.pub_thumb_grid_layout.addWidget(self.load_more_button, self.amt // self.width +1, 0, 1, 2)
        self.load_more_button.setEnabled(True)

    def more(self):
        self.load_more_button.setEnabled(False)
        self.worker = helpers.FeedUpdater()
        self.worker.set_feed(self.feed)
        self.worker.moveToThread(self._window.load_thread)
        self._window.load_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.new_pub)
        self.worker.finished.connect(self.get_images_and_fix_button)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self._window.load_thread.quit)
        self.scroll_area.ensureWidgetVisible(self.load_more_button)
        self._window.load_thread.start()

class FollowingScreen(ListScreen):
    def __init__(self, window, feed):
        self.feed = feed
        self.title = 'Following'
        self.url = 'about:following'
        super(FollowingScreen, self).__init__(window)
        uic.loadUi(helpers.relative_path('designer/following.ui'), self)
        self.setup()

class ChannelScreen(ListScreen):
    def __init__(self, window, channel):
        self.title = channel.name
        self.channel = channel
        self.feed = channel.pubs_feed
        self.url = channel.url
        super(ChannelScreen, self).__init__(window)
        uic.loadUi(helpers.relative_path('designer/channel.ui'), self)
        self.setup()
        self.description_label.setText(helpers.fix_markdown(self.channel.description))
        self.description_label.linkActivated.connect(self.change_url.emit)
        if channel.is_followed:
            self.set_to_unfollow()
        else:
            self.set_to_follow()
        self.finished.connect(self.channel.refresh_feed)

    def follow(self):
        self.channel.follow()
        self.set_to_unfollow()
    
    def set_to_follow(self):
        self.follow_button.clicked.connect(self.follow)
        self.follow_button.setText('Follow')
    
    def set_to_unfollow(self):
        self.follow_button.clicked.connect(self.unfollow)
        self.follow_button.setText('Following')

    def unfollow(self):
        self.channel.unfollow()
        self.set_to_follow()

class PubWidget(QtWidgets.QDialog):
    def __init__(self, pub):
        super(PubWidget, self).__init__()
        uic.loadUi(helpers.relative_path('designer/pub_thumb.ui'), self)
        self.loaders = []
        self.pub = pub
        self.title.setText(pub.title)
        if type(pub) == lyberry_api.channel.LBRY_Channel:
            self.channel.setText(pub.name)
        else:
            self.channel.setText(pub.channel.name)


from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from lyberry_qt import helpers
import lyberry_api.channel

class ListScreen(QtWidgets.QDialog):
    def __init__(self, window):
        super(ListScreen, self).__init__()
        self._window = window

    def setup(self):
        self.title_label.setText(self.title)
        self.load_more_button.clicked.connect(self.more)
        self.amt = 2
        self.width = 2
        self.items = []
        self.img_threads = [QThread() for i in range(4)]
        self.img_thread_no = 0
        self.thread = QThread()

    def new_pub(self, pub):
        item = PubWidget(pub, self.img_threads[self.img_thread_no])
        if type(pub) == lyberry_api.channel.LBRY_Channel:
            item.title.clicked.connect(lambda: self._window.show_channel(pub))
            item.channel.clicked.connect(lambda: self._window.show_channel(pub))
        else:
            item.title.clicked.connect(lambda: self._window.show_pub(pub))
            item.channel.clicked.connect(lambda: self._window.show_channel(pub.channel))
        self.img_thread_no = (self.img_thread_no + 1) % len(self.img_threads)
        self.items.append(item)

        self.pub_thumb_grid_layout.addWidget(item, self.amt // self.width, self.amt % self.width, 1, 1)
        self.amt += 1
        return item.pub_grid
    
    def pubs_to_list(self, pubs):
        for pub in pubs:
            self.new_pub(pub)
        self.pub_thumb_grid_layout.addWidget(self.load_more_button, self.amt // self.width +1, 0, 1, 2)
        for thread in self.img_threads:
            thread.start()
        self.scroll_area.ensureWidgetVisible(self.load_more_button)

    def more(self):
        self.load_more_button.setEnabled(False)

        self.worker = helpers.FeedUpdater()
        self.worker.set_feed(self.feed)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.pubs_to_list)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.quit)
        self.thread.start()
        self.thread.finished.connect(
            lambda: self.load_more_button.setEnabled(True)
        )

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
        self.description_label.setText(self.channel.description)
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
    def __init__(self, pub, img_thread):
        super(PubWidget, self).__init__()
        uic.loadUi(helpers.relative_path('designer/pub_thumb.ui'), self)
        self.loaders = []
        self.img_thread = img_thread
        self.pub = pub
        self.title.setText(pub.title)
        self.img_url_to_label(pub.thumbnail, self.thumbnail)
        if type(pub) == lyberry_api.channel.LBRY_Channel:
            self.channel.setText(pub.name)
        else:
            self.channel.setText(pub.channel.name)

    def img_url_to_label(self, url, label):
        label.setText('Loading image')
        img_loader = helpers.ImageLoader()
        img_loader.set_url(url)
        self.loaders.append(img_loader)
        img_loader.moveToThread(self.img_thread)
        self.img_thread.started.connect(img_loader.run)
        img_loader.finished.connect(self.img_thread.quit)
        img_loader.finished.connect(img_loader.deleteLater)
        img_loader.finished.connect(label.setPixmap)


"""
Level Meter (VU) for QT5
========================

Usage:
from qt5_levelmeter import QLevelMeter

meter = QLevelMeter(parent)

call periodically:
meter.levelChanged(levelInDb)
"""

import math
from PyQt5.QtCore import Qt, QTime, QRect, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QFont
from PyQt5.QtWidgets import QWidget, QSizePolicy


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


class QLevelMeter(QWidget):

    REDRAW_INTERVAL = 50 # ms
    PEAK_DECAY_FACTOR_FAST = 0.025 # dB/ms. 25dB/1s, my own preferred rolloff
    PEAK_DECAY_FACTOR = 0.011764 # dB/ms. 20dB/1.7s as per DIN and IEC 60268-10/17/18 recommendation
    PEAK_DECAY_FUZZYNESS = 1 # dB - only show decayed value if it's this much lower than peak
    PEAK_HOLD_DURATION = 2000 # ms - reset peak level bar after this long
    MIN_DB = -48.0
    # colors & fonts
    BG_COLOR = QColor(50, 50, 50)
    BAR_BG_COLOR = QColor(20, 20, 20)
    BAR_FRAME_COLOR = QColor(100, 100, 100)
    TEXT_COLOR = QColor(200, 200, 200)
    LEVEL_COLOR_GREEN = QColor(0, 175, 0)
    LEVEL_COLOR_ORANGE = QColor(255, 100, 0)
    LEVEL_COLOR_YELLOW = QColor(255, 200, 0)
    LEVEL_COLOR_RED = QColor(255, 0, 0)
    PEAK_COLOR = QColor(130, 255, 255)
    PEAK_COLOR_0 = QColor(130, 0, 0)
    COLOR_RED = QColor(255, 0, 0)
    COLOR_ORANGE = QColor(255, 150, 0)
    COLOR_YELLOW = QColor(205, 205, 0)
    COLOR_GREEN = QColor(0, 255, 0)
    TEXT_FONT = QFont('DejaVu Sans', 10)
    # dimensions
    MINIMUM_WIDTH = 60
    TEXT_LEFT_MARGIN = 3
    PEAK_MAX_TOP_MARGIN = 5
    BAR_TOP_MARGIN = 20
    BAR_RIGHT_MARGIN = 2
    BAR_LEFT_MARGIN = 30
    BAR_BOTTOM_MARGIN = 5
    PEAKHOLD_BAR_HEIGHT = 3


    _signal_update = pyqtSignal()


    def __init__(self, parent, fastRolloff=False):
        super().__init__(parent)
        self._peakLevelMax = -1000.0
        self._peakLevel = -1000.0
        self._decayedPeakLevel = -1000.0
        self._peakHoldLevel = -1000.0
        self._peakLevelChanged = QTime()
        self._peakHoldLevelChanged = QTime()
        self.levelChanged(-1000.0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.setMinimumWidth(self.MINIMUM_WIDTH)
        self._barRect = None
        if fastRolloff:
            self._peakDecayFactor = self.PEAK_DECAY_FACTOR_FAST
        else:
            self._peakDecayFactor = self.PEAK_DECAY_FACTOR
        # noinspection PyUnresolvedReferences
        self._signal_update.connect(self.update)


    def levelChanged(self, peakLevel):
        self._peakLevelMax = max(self._peakLevelMax, peakLevel)
        if peakLevel > self._decayedPeakLevel - self.PEAK_DECAY_FUZZYNESS:
            self._peakLevel = peakLevel
            self._decayedPeakLevel = peakLevel
            self._peakLevelChanged.start()
        else:
            elapsed = self._peakLevelChanged.elapsed()
            self._decayedPeakLevel = max(self.MIN_DB, self._peakLevel - self._peakDecayFactor * elapsed)
        if peakLevel > self._peakHoldLevel:
            self._peakHoldLevel = peakLevel
            self._peakHoldLevelChanged.start()
        elif self._peakHoldLevelChanged.elapsed() > self.PEAK_HOLD_DURATION:
            self._peakHoldLevel = self.MIN_DB
        # noinspection PyUnresolvedReferences
        self._signal_update.emit()


    def paintEvent(self, event):
        # draw widget background
        qp = QPainter(self)
        qp.fillRect(self.rect(), self.BG_COLOR)
        # draw bar background and frame
        bar_rect = QRect(self.rect())
        bar_rect.setLeft(self.BAR_LEFT_MARGIN)
        bar_rect.setTop(self.BAR_TOP_MARGIN)
        bar_rect.setBottom(self.rect().height() - self.BAR_BOTTOM_MARGIN)
        bar_rect.setRight(self.rect().right() - 1)
        qp.setPen(self.BAR_FRAME_COLOR)
        qp.setBrush(self.BAR_BG_COLOR)
        qp.drawRect(bar_rect)
        # draw text labels
        db = 0
        steps = -1 * int(self.MIN_DB / 6)
        qp.setPen(self.TEXT_COLOR)
        qp.setFont(self.TEXT_FONT)
        metrics = qp.fontMetrics()
        fontHeight = metrics.height()
        spacing = (bar_rect.height() - 2) / steps
        # draw 0dB label
        qp.drawText(self.TEXT_LEFT_MARGIN, self.BAR_TOP_MARGIN, metrics.width("0dB") + 2, fontHeight, Qt.AlignLeft | Qt.AlignBaseline, "0dB")
        db -= 6
        # draW rest of label strings
        top = self.BAR_TOP_MARGIN - fontHeight / 2
        while db >= self.MIN_DB:
            top += spacing
            s = str(db)
            db -= 6
            width = metrics.width(s)
            qp.drawText(self.TEXT_LEFT_MARGIN,
                        top,
                        width+2,
                        fontHeight,
                        Qt.AlignLeft | Qt.AlignVCenter,
                        s)
        # bar helper variables
        x = bar_rect.x() + 1
        y = bar_rect.y() + 1
        h = bar_rect.height() - 2
        w = bar_rect.width() - 2
        # draw level bar
        if self._decayedPeakLevel > 0:
            color = self.LEVEL_COLOR_RED
        else:
            color = self.LEVEL_COLOR_GREEN
        qp.setPen(color)
        qp.setBrush(color)
        decayedPeakLevel = max(self.MIN_DB, min(0.0, self._decayedPeakLevel))
        my_h = round((1 - (decayedPeakLevel / self.MIN_DB)) * h) - 3
        if decayedPeakLevel > self.MIN_DB:
            qp.drawRect(x, y + (h - my_h), w, max(0, my_h))
        # draw yellow and orange parts of level bar if appliccable
        if self._decayedPeakLevel <= 0:
            if self._decayedPeakLevel > -12:
                qp.setPen(self.LEVEL_COLOR_YELLOW)
                qp.setBrush(self.LEVEL_COLOR_YELLOW)
                my_h = round((-12 - decayedPeakLevel) / self.MIN_DB * h) - 2
                my_y = y + round(-12 / self.MIN_DB * h) - my_h
                qp.drawRect(x, my_y, w, my_h)
            if self._decayedPeakLevel > -6:
                qp.setPen(self.LEVEL_COLOR_ORANGE)
                qp.setBrush(self.LEVEL_COLOR_ORANGE)
                my_h = round((-6 - decayedPeakLevel) / self.MIN_DB * h) - 1
                my_y = y + round(-6 / self.MIN_DB * h) - my_h
                qp.drawRect(x, my_y, w, my_h)
        # draw peakhold bar
        peak = max(self._peakHoldLevel, decayedPeakLevel)
        color = self._peakHoldLevel > self.MIN_DB and self.PEAK_COLOR or self.PEAK_COLOR_0
        qp.setPen(color)
        qp.setBrush(color)
        my_h = round((1 - (min(0.0, peak) / self.MIN_DB)) * h)
        qp.drawRect(x, y + (h - max(self.PEAKHOLD_BAR_HEIGHT, my_h)), w, self.PEAKHOLD_BAR_HEIGHT)
        # draw max level text
        if self._peakLevelMax > 0.0:
            color = self.COLOR_RED
        elif self._peakLevelMax > -6.0:
            color = self.COLOR_ORANGE
        elif self._peakLevelMax > -12.0:
            color = self.COLOR_YELLOW
        else:
            color = self.COLOR_GREEN
        if self._peakLevelMax < -999.8:
            s = "-∞ dB"
        else:
            s = "%0.2fdB" % round_up(self._peakLevelMax, 2)
        qp.setPen(color)
        qp.drawText(0, 0, self.width(), fontHeight, Qt.AlignRight | Qt.AlignTop, s)


    def resetPeakLevelMax(self):
        self._peakLevelMax = -1000.0

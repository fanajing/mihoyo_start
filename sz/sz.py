from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton
from PyQt6.QtWidgets import QTabWidget, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtCore import QByteArray
from PyQt6.QtCore import QSize, QCoreApplication
import configparser
import os
import sys
import base64
import base64a
from base64a import bg
base64_image = base64.b64decode(bg)
class sz(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(''))
        data = base64_image
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(data))
        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

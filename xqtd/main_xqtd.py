from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
import os
from PyQt6.QtWidgets import QApplication, QTabWidget, QLabel, QTabBar
from PyQt6.QtGui import QPixmap, QIcon,QImageReader, QGuiApplication, QPalette, QBrush

xqtd_bg=os.path.join('bg/xqtd')
class xqtd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(''))
        # 构建背景图像文件路径
        bg = xqtd_bg + '/' + 'bg.png'

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap(image)

        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
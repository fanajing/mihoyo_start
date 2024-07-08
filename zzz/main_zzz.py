from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QApplication, QTabWidget, QLabel, QTabBar
import os
from PyQt6.QtGui import QPixmap, QIcon,QImageReader, QGuiApplication, QPalette, QBrush
zzz_bg=os.path.join('bg/zzz')
class zzz(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(''))

        bg = zzz_bg + '/' + 'bg.png'

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap(image)

        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
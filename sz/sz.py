from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton,QLineEdit
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
        # 添加图片
        pixmap_ys = QPixmap("image/ys.png")  # 这里替换为实际图像文件的名字
        pixmap_ys = pixmap_ys.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel(self)
        image_label.setPixmap(pixmap_ys)
        image_label.setGeometry(10, 100, pixmap_ys.width(), pixmap_ys.height())  # （x位置，y位置，宽度，高度）

        # 添加文本框
        # 读取 'x.ini' 中的 'ys_ml' 值
        config = configparser.ConfigParser()
        config.read('start_config.ini')
        default_text_ys = config.get('DEFAULT', 'ys_ml')
        txt_input_ys = QLineEdit(self)
        txt_input_ys.setGeometry(130, 160, 380, 30)  # 设置文本框的位置和大小
        txt_input_ys.setText(default_text_ys)  # 设置默认值
        txt_input_ys.setReadOnly(True)
        icon_data = base64.b64decode(base64a.cz)  # 使用cz解码base64
        pixmap_cz = QPixmap()
        pixmap_cz.loadFromData(icon_data)  # 从数据加载Pixmap
        # 创建按钮
        scaled_pixmap = pixmap_cz.scaled(160, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao.move(500, 110)
        self.chazhao.clicked.connect(self.button_click)
        # 设置按钮的大小为图片的大小
        self.chazhao.setIcon(QIcon(scaled_pixmap))
        self.chazhao.setFixedSize(pixmap_cz.width(), pixmap_cz.height())

        # 将图标设置为按钮的背景
        self.chazhao.setIcon(QIcon(pixmap_cz))
        self.chazhao.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小

        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def button_click(self):
        # 这里填写按钮被点击后应该执行的操作
        pass

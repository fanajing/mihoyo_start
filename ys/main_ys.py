from PyQt6.QtWidgets import QTabWidget,QMessageBox, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout,QApplication, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt,QByteArray,QSize, QCoreApplication
import configparser
import os
import sys
import base64
import base64a
from base64a import bg
from base64a import cz
base64_image = base64.b64decode(bg)
config = configparser.ConfigParser()
config.read('start_config.ini')
ys_ml = config.get('DEFAULT', 'ys_ml')
ys_config = os.path.join(ys_ml, 'config.ini')
ys_config = ys_config.replace('\\', '/')
ys_bg=os.path.join(ys_ml,'bg')
ys_bg = ys_bg.replace('\\', '/')
xzlj = "https://fs-im-kefu.7moor-fs1.com/29397395/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1708161130394/PCGameSDK.dll"


G = """cps=mihoyo
channel=1
"""
B = """cps=bilibili
channel=14
"""


class ys(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        #官服
        icon_data_guan = base64.b64decode(base64a.guan1)  # 使用guan1解码base64
        pixmap_guan = QPixmap()
        pixmap_guan.loadFromData(icon_data_guan)  # 从数据加载Pixmap

        scaled_pixmap = pixmap_guan.scaled(160, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.guanfu = QPushButton('', self)  # 注意，按钮的文字为空
        self.guanfu.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.guanfu.move(750, 600)
        self.guanfu.clicked.connect(self.on_button_clicked)
        # 设置按钮的大小为图片的大小
        self.guanfu.setIcon(QIcon(scaled_pixmap))
        self.guanfu.setFixedSize(pixmap_guan.width(), pixmap_guan.height())

        # 将图标设置为按钮的背景
        self.guanfu.setIcon(QIcon(pixmap_guan))
        self.guanfu.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小

        #b服
        icon_data_b = base64.b64decode(base64a.b1)  # 使用guan1解码base64
        pixmap_b = QPixmap()
        pixmap_b.loadFromData(icon_data_b)  # 从数据加载Pixmap

        scaled_pixmap = pixmap_b.scaled(160, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.bfu = QPushButton('', self)  # 注意，按钮的文字为空
        self.bfu.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.bfu.move(950, 600)
        self.bfu.clicked.connect(self.on_button_clicked)
        # 设置按钮的大小为图片的大小
        self.bfu.setIcon(QIcon(scaled_pixmap))
        self.bfu.setFixedSize(pixmap_b.width(), pixmap_b.height())

        # 将图标设置为按钮的背景
        self.bfu.setIcon(QIcon(pixmap_b))
        self.bfu.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小


        if os.path.exists(ys_config):
            with open(ys_config, 'r') as file:
                for line in file:
                    if 'game_dynamic_bg_name=' in line:
                        game_dynamic_bg_name = line.split('=')[1].strip()
                        break

            # 构建背景图像文件路径
            bg = ys_bg + '/' + game_dynamic_bg_name
            image_reader = QImageReader(bg)
            image = image_reader.read()
            pixmap = QPixmap.fromImage(image)
        else:
            data = base64_image
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(data))





        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        image_folder='ScreenShot'
        self.images = [
            os.path.join(image_folder, img)
            for img in os.listdir(image_folder)
            if img.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
        self.current_image = -1

        self.image_label = QLabel("", self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)


        self.timer = QTimer(self)
        self.timer.setInterval(3000)
        self.timer.start()
        self.timer.timeout.connect(self.next_image)

    def next_image(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        pixmap = QPixmap(self.images[self.current_image]).scaled(505,285)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(30, 210, 505, 285)

    def on_button_clicked(self):

        pass


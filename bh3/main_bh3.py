from PyQt6.QtWidgets import QTabWidget,QMessageBox, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout,QApplication, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt,QByteArray,QSize, QCoreApplication
import threading  # 提供多线程编程支持
import configparser
import os
import win32api
import ctypes
import subprocess
import shutil
import requests
import sys
import base64
import base64a
from base64a import bg
from base64a import cz
base64_image = base64.b64decode(bg)
config = configparser.ConfigParser()
config.read('start_config.ini')
bh3_ml = config.get('DEFAULT', 'bh3_ml')
bh3_config = 'config.ini'
bh3_bg = os.path.join('bg/bh3')
bh3_bg = bh3_bg.replace('\\', '/')
xzlj = "https://fs-im-kefu.7moor-fs1.com/29397395/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1708161130394/PCGameSDK.dll"
bfplugin = bh3_ml+"/Honkai Impact 3rd Game/BH3_Data/Plugins/PCGameSDK.dll"
gfplugin= bh3_ml+"/Honkai Impact 3rd Game/BH3_Data/Plugins/PCGameSDK.dllx"

G = """cps=mihoyo
channel=1
"""
B = """cps=bilibili_PC
channel=14
sub_channel=0
"""
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class bh3(QWidget):
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
        self.guanfu.clicked.connect(self.on_button_clicked_guanfu)
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
        self.bfu.clicked.connect(self.on_button_clicked_bfu)
        # 设置按钮的大小为图片的大小
        self.bfu.setIcon(QIcon(scaled_pixmap))
        self.bfu.setFixedSize(pixmap_b.width(), pixmap_b.height())

        # 将图标设置为按钮的背景
        self.bfu.setIcon(QIcon(pixmap_b))
        self.bfu.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小


        if os.path.exists(bh3_config):


            # 构建背景图像文件路径
            bg = bh3_bg + '/' + 'b3.png'
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

    def on_button_clicked_guanfu(self):
        if not is_admin():
            QMessageBox.critical(None, "错误", "请以管理员权限运行程序！")
            return
        with open(bh3_config, 'w') as file:
            file.write(G)
            if os.path.exists(bfplugin):
                os.remove(bfplugin)

        exe = bh3_ml + '/' + "Honkai Impact 3rd Game/BH3.exe"
        exe = '"' + exe + '"'

        def run_exe():
            subprocess.Popen(exe)

        self.window().showMinimized()
        t = threading.Thread(target=run_exe)
        t.start()  # 启动新线程

    def on_button_clicked_bfu(self):
        if not is_admin():
            QMessageBox.critical(None, "错误", "请以管理员权限运行程序！")
            return
        with open(bh3_config, 'w') as file:
            file.write(B)
            if os.path.exists(bfplugin):
                os.remove(bfplugin)
            else:
                shutil.copyfile('PCGameSDK.dll', bfplugin)

        exe =bh3_ml + '/' + "Honkai Impact 3rd Game/BH3.exe"
        exe= '"'+exe+'"'


        def run_exe():
            subprocess.Popen(exe)

        self.window().showMinimized()
        t = threading.Thread(target=run_exe)
        t.start()  # 启动新线程





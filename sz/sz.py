
from PyQt6.QtWidgets import QApplication, QFileDialog, QRadioButton, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QTabWidget, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtWidgets import QApplication, QMessageBox, QVBoxLayout, QRadioButton, QTextEdit, QWidget, QPushButton
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QRadioButton, QPushButton
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt, QSize, QCoreApplication, pyqtSignal, QObject
from PyQt6.QtCore import QByteArray
import configparser
import subprocess
import requests
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QRadioButton, QTextEdit, QPushButton, QHBoxLayout, QMainWindow, QWidget
import sys
import os
import threading
import requests
import sys
import time
import base64
import base64a
from base64a import bg
base64_image = base64.b64decode(bg)

class DownloadWorker(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, url, save_path, total_tasks, progress_callback):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.total_tasks = total_tasks
        self.progress_callback = progress_callback

    def download_file(self):
        response = requests.get(self.url, stream=True)
        total_length = response.headers.get('content-length')
        downloaded = 0
        if total_length is None:
            total_length = 0
        else:
            total_length = int(total_length)

        with open(self.save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    downloaded += len(chunk)
                    percent_complete = int(100 * downloaded / total_length) if total_length else 0
                    self.progress.emit(percent_complete)
                    self.progress_callback(percent_complete / self.total_tasks)
        self.finished.emit()
class sz(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(''))
        data = base64_image
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(data))
        self.config = configparser.ConfigParser()
        self.download_url = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/mihoyo_start.zip"
        self.download_ysurl = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/ys.png"
        self.download_xturl = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/xt.png"
        self.download_b3url = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/b3.png"
        self.download_zzzurl = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/zzz.png"

        # self.bg_urls = {
        #     'bg_1': "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/ys.png",
        #     'bg_2': "https://example.com/bg_2.zip",
        #     'bg_3': "https://example.com/bg_3.zip",
        #     'bg_4': "https://example.com/bg_4.zip"
        # }
        self.config_file_path = 'start_config.ini'
        self.check_and_load_config()


        #原神
        # 添加图片
        pixmap_ys = QPixmap("image/ys.png")  # 这里替换为实际图像文件的名字
        pixmap_ys = pixmap_ys.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel(self)
        image_label.setPixmap(pixmap_ys)
        image_label.setGeometry(10, 100, pixmap_ys.width(), pixmap_ys.height())  # （x位置，y位置，宽度，高度）

        # 添加文本框
        config = configparser.ConfigParser()
        config.read('start_config.ini')
        default_text_ys = config.get('DEFAULT', 'ys_ml')
        self.txt_input_ys = QLineEdit(self)
        self.txt_input_ys.setGeometry(100, 140, 380, 30)  # 设置文本框的位置和大小
        self.txt_input_ys.setText(default_text_ys)  # 设置默认值
        self.txt_input_ys.setReadOnly(True)
        icon_data = base64.b64decode(base64a.cz)  # 使用cz解码base64
        pixmap_cz = QPixmap()
        pixmap_cz.loadFromData(icon_data)  # 从数据加载Pixmap
        # 创建按钮
        scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao_ys = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao_ys.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao_ys.move(420, 100)
        self.chazhao_ys.clicked.connect(self.button_click_ys)
        # 设置按钮的大小为图片的大小
        self.chazhao_ys.setIcon(QIcon(scaled_pixmap))
        self.chazhao_ys.setFixedSize(pixmap_cz.width(), pixmap_cz.height())

        # 将图标设置为按钮的背景
        self.chazhao_ys.setIcon(QIcon(pixmap_cz))
        self.chazhao_ys.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小

        # 星穹铁道
        # 添加图片
        pixmap_xqtd = QPixmap("image/xqtd.png")  # 这里替换为实际图像文件的名字
        pixmap_xqtd = pixmap_xqtd.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel(self)
        image_label.setPixmap(pixmap_xqtd)
        image_label.setGeometry(10, 200, pixmap_xqtd.width(), pixmap_xqtd.height())  # （x位置，y位置，宽度，高度）

        # 添加文本框
        config = configparser.ConfigParser()
        config.read('start_config.ini')
        default_text_xqtd = config.get('DEFAULT', 'xqtd_ml')
        self.txt_input_xqtd = QLineEdit(self)
        self.txt_input_xqtd.setGeometry(100, 240, 380, 30)  # 设置文本框的位置和大小
        self.txt_input_xqtd.setText(default_text_xqtd)  # 设置默认值
        self.txt_input_xqtd.setReadOnly(True)
        icon_data = base64.b64decode(base64a.cz)  # 使用cz解码base64
        pixmap_cz = QPixmap()
        pixmap_cz.loadFromData(icon_data)  # 从数据加载Pixmap
        # 创建按钮
        scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao_xqtd = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao_xqtd.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao_xqtd.move(420, 200)
        self.chazhao_xqtd.clicked.connect(self.button_click_xqtd)
        # 设置按钮的大小为图片的大小
        self.chazhao_xqtd.setIcon(QIcon(scaled_pixmap))
        self.chazhao_xqtd.setFixedSize(pixmap_cz.width(), pixmap_cz.height())

        # 将图标设置为按钮的背景
        self.chazhao_xqtd.setIcon(QIcon(pixmap_cz))
        self.chazhao_xqtd.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小

        # 设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # zzz
        # 添加图片
        pixmap_zzz = QPixmap("image/zzz.png")  # 这里替换为实际图像文件的名字
        pixmap_zzz = pixmap_zzz.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel(self)
        image_label.setPixmap(pixmap_zzz)
        image_label.setGeometry(10, 300, pixmap_zzz.width(), pixmap_zzz.height())  # （x位置，y位置，宽度，高度）

        # 添加文本框
        config = configparser.ConfigParser()
        config.read('start_config.ini')
        default_text_zzz = config.get('DEFAULT', 'zzz_ml')
        self.txt_input_zzz = QLineEdit(self)
        self.txt_input_zzz.setGeometry(100, 340, 380, 30)  # 设置文本框的位置和大小
        self.txt_input_zzz.setText(default_text_zzz)  # 设置默认值
        self.txt_input_zzz.setReadOnly(True)
        icon_data = base64.b64decode(base64a.cz)  # 使用cz解码base64
        pixmap_cz = QPixmap()
        pixmap_cz.loadFromData(icon_data)  # 从数据加载Pixmap
        # 创建按钮
        scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao_zzz = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao_zzz.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao_zzz.move(420, 300)
        self.chazhao_zzz.clicked.connect(self.button_click_zzz)
        # 设置按钮的大小为图片的大小
        self.chazhao_zzz.setIcon(QIcon(scaled_pixmap))
        self.chazhao_zzz.setFixedSize(pixmap_cz.width(), pixmap_cz.height())

        # 将图标设置为按钮的背景
        self.chazhao_zzz.setIcon(QIcon(pixmap_cz))
        self.chazhao_zzz.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小

        # bh3
        # 添加图片
        pixmap_bh3 = QPixmap("image/bh3.png")  # 这里替换为实际图像文件的名字
        pixmap_bh3 = pixmap_bh3.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel(self)
        image_label.setPixmap(pixmap_bh3)
        image_label.setGeometry(10, 400, pixmap_bh3.width(), pixmap_bh3.height())  # （x位置，y位置，宽度，高度）

        # 添加文本框
        config = configparser.ConfigParser()
        config.read('start_config.ini')
        default_text_bh3 = config.get('DEFAULT', 'bh3_ml')
        self.txt_input_bh3 = QLineEdit(self)
        self.txt_input_bh3.setGeometry(100, 440, 380, 30)  # 设置文本框的位置和大小
        self.txt_input_bh3.setText(default_text_bh3)  # 设置默认值
        self.txt_input_bh3.setReadOnly(True)
        icon_data_cz = base64.b64decode(base64a.cz)  # 使用cz解码base64
        pixmap_cz = QPixmap()
        pixmap_cz.loadFromData(icon_data_cz)  # 从数据加载Pixmap

        # 创建按钮
        scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao_bh3 = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao_bh3.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao_bh3.move(420, 400)
        self.chazhao_bh3.clicked.connect(self.button_click_bh3)
        # 设置按钮的大小为图片的大小
        self.chazhao_bh3.setIcon(QIcon(scaled_pixmap))
        self.chazhao_bh3.setFixedSize(pixmap_cz.width(), pixmap_cz.height())

        # 将图标设置为按钮的背景
        self.chazhao_bh3.setIcon(QIcon(pixmap_cz))
        self.chazhao_bh3.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小



        #保存按钮
        icon_data_bc = base64.b64decode(base64a.bc)  # 使用bc解码base64
        pixmap_bc = QPixmap()
        pixmap_bc.loadFromData(icon_data_bc)  # 从数据加载Pixmap
        # 创建按钮
        scaled_pixmap = pixmap_bc.scaled(600, 220, Qt.AspectRatioMode.KeepAspectRatio)
        self.chazhao_bc = QPushButton('', self)  # 注意，按钮的文字为空
        self.chazhao_bc.setStyleSheet(f"border:none;")  # 移除按钮的边框
        self.chazhao_bc.move(680, 550)
        self.chazhao_bc.clicked.connect(self.restart)
        # 设置按钮的大小为图片的大小
        self.chazhao_bc.setIcon(QIcon(scaled_pixmap))
        self.chazhao_bc.setFixedSize(pixmap_bc.width(), pixmap_bc.height())

        # 将图标设置为按钮的背景
        self.chazhao_bc.setIcon(QIcon(pixmap_bc))
        self.chazhao_bc.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小


        #
        # # 更新按钮
        # scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        # self.chazhao_gx = QPushButton('', self)  # 注意，按钮的文字为空
        # self.chazhao_gx.setStyleSheet(f"border:none;")  # 移除按钮的边框
        # self.chazhao_gx.move(150, 500)
        # self.chazhao_gx.clicked.connect(self.show_message_box)
        # # 设置按钮的大小为图片的大小
        # self.chazhao_gx.setIcon(QIcon(scaled_pixmap))
        # self.chazhao_gx.setFixedSize(pixmap_cz.width(), pixmap_cz.height())
        #
        # # 将图标设置为按钮的背景
        # self.chazhao_gx.setIcon(QIcon(pixmap_cz))
        # self.chazhao_gx.setIconSize(QSize(scaled_pixmap.width(), scaled_pixmap.height()))  # 设置icon的大小


    def button_click_ys(self):
        # 首先创建 configparser.ConfigParser 实例
        config = configparser.ConfigParser()

        # 确认正确读取 start_config.ini 文件（或者你需要读取的文件名）
        config.read('start_config.ini')


        file_dialog = QFileDialog(self)  # 设置 ys 为 file_dialog 的父窗体
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # 设置为选择已存在的文件模式
        file_dialog.setNameFilter("Executable files (*.exe)")  # 设置只显示 .exe 文件

        if file_dialog.exec():  # 如果用户选择了
            file_name = file_dialog.selectedFiles()[0]  # 获取选定文件的路径
            if os.path.basename(file_name) != 'YuanShen.exe':
                QMessageBox.warning(self, "错误", "请选择YuanShen.exe")
            else:
                upper_directory = os.path.dirname(file_name)  # 获取文件的上一级目录
                grandparent_directory = os.path.dirname(upper_directory)
                # 这里调用 set 方法更改配置项
                config.set('DEFAULT', 'ys_ml', grandparent_directory)
                # 打开文件并保存配置
                with open('start_config.ini', 'w') as configfile:
                    config.write(configfile)

                self.txt_input_ys.setText(grandparent_directory)



        else:
            print("用户取消选择")
    def button_click_xqtd(self):
        # 首先创建 configparser.ConfigParser 实例
        config = configparser.ConfigParser()

        # 确认正确读取 start_config.ini 文件（或者你需要读取的文件名）
        config.read('start_config.ini')


        file_dialog = QFileDialog(self)  # 设置 ys 为 file_dialog 的父窗体
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # 设置为选择已存在的文件模式
        file_dialog.setNameFilter("Executable files (*.exe)")  # 设置只显示 .exe 文件

        if file_dialog.exec():  # 如果用户选择了
            file_name = file_dialog.selectedFiles()[0]  # 获取选定文件的路径
            if os.path.basename(file_name) != 'StarRail.exe':
                QMessageBox.warning(self, "错误", "请选择StarRail.exe")
            else:
                upper_directory = os.path.dirname(file_name)  # 获取文件的上一级目录
                grandparent_directory = os.path.dirname(upper_directory)
                # 这里调用 set 方法更改配置项
                config.set('DEFAULT', 'xqtd_ml', grandparent_directory)
                # 打开文件并保存配置
                with open('start_config.ini', 'w') as configfile:
                    config.write(configfile)
                self.txt_input_xqtd.setText(grandparent_directory)



        else:
            print("用户取消选择")




    def button_click_zzz(self):
            # 首先创建 configparser.ConfigParser 实例
            config = configparser.ConfigParser()

            # 确认正确读取 start_config.ini 文件（或者你需要读取的文件名）
            config.read('start_config.ini')


            file_dialog = QFileDialog(self)  # 设置 ys 为 file_dialog 的父窗体
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # 设置为选择已存在的文件模式
            file_dialog.setNameFilter("Executable files (*.exe)")  # 设置只显示 .exe 文件

            if file_dialog.exec():  # 如果用户选择了
                file_name = file_dialog.selectedFiles()[0]  # 获取选定文件的路径
                if os.path.basename(file_name) != 'ZenlessZoneZero.exe':
                    QMessageBox.warning(self, "错误", "请选择ZenlessZoneZero.exe")
                else:
                    upper_directory = os.path.dirname(file_name)  # 获取文件的上一级目录
                    grandparent_directory = os.path.dirname(upper_directory)
                    # 这里调用 set 方法更改配置项
                    config.set('DEFAULT', 'zzz_ml', grandparent_directory)
                    # 打开文件并保存配置
                    with open('start_config.ini', 'w') as configfile:
                        config.write(configfile)
                    self.txt_input_ys.setText(grandparent_directory)



            else:
                print("用户取消选择")
    def button_click_bh3(self):
        # 首先创建 configparser.ConfigParser 实例
        config = configparser.ConfigParser()

        # 确认正确读取 start_config.ini 文件（或者你需要读取的文件名）
        config.read('start_config.ini')


        file_dialog = QFileDialog(self)  # 设置 ys 为 file_dialog 的父窗体
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # 设置为选择已存在的文件模式
        file_dialog.setNameFilter("Executable files (*.exe)")  # 设置只显示 .exe 文件

        if file_dialog.exec():  # 如果用户选择了
            file_name = file_dialog.selectedFiles()[0]  # 获取选定文件的路径
            if os.path.basename(file_name) != 'BH3.exe':
                QMessageBox.warning(self, "错误", "请选择BH3.exe")
            else:
                upper_directory = os.path.dirname(file_name)  # 获取文件的上一级目录
                grandparent_directory = os.path.dirname(upper_directory)
                # 这里调用 set 方法更改配置项
                config.set('DEFAULT', 'bh3_ml', grandparent_directory)
                # 打开文件并保存配置
                with open('start_config.ini', 'w') as configfile:
                    config.write(configfile)

                self.txt_input_bh3.setText(grandparent_directory)

        else:
            print("用户取消选择")
    def check_and_load_config(self):
        try:
            with open(self.config_file_path, 'r', encoding='utf-8') as f:
                self.config.read_file(f)
            # 如果配置文件中存在 version_id 则读取，否则默认设为 0
            if self.config.has_section('OSS') and self.config.has_option('OSS', 'version_id'):
                self.local_version_id = float(self.config.get('OSS', 'version_id'))
            if self.config.has_section('OSS') and self.config.has_option('OSS', 'bz_ys'):
                self.local_bz_ys = float(self.config.get('OSS', 'bz_ys'))
            if self.config.has_section('OSS') and self.config.has_option('OSS', 'bz_xt'):
                self.local_bz_xt = float(self.config.get('OSS', 'bz_xt'))
            if self.config.has_section('OSS') and self.config.has_option('OSS', 'bz_b3'):
                self.local_bz_b3 = float(self.config.get('OSS', 'bz_b3'))
            if self.config.has_section('OSS') and self.config.has_option('OSS', 'bz_zzz'):
                self.local_bz_zzz = float(self.config.get('OSS', 'bz_zzz'))
        except (FileNotFoundError, UnicodeDecodeError, ValueError):
            # 如果文件不存在、编码错误或值错误，设置本地版本ID为0
            self.local_version_id = 0
            self.local_bz_ys = 0
            self.local_bz_xt = 0
            self.local_bz_b3 = 0
            self.local_bz_zzz = 0

        self.check_for_update()
        self.check_for_ysdate()
        self.check_for_xtdate()
        self.check_for_b3date()
        self.check_for_zzzdate()



    def check_for_update(self):
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_url, headers=headers)
            print(response)
            # for key, url in self.bg_urls.items():
            #     try:
            #         response = requests.head(url, headers=headers)
            #         print(f"{key} response: {response}")
            #
            #         oss_meta_key = f'x-oss-meta-{key}'
            #         if oss_meta_key in response.headers:
            #             print(f"获取到的 {oss_meta_key}: {response.headers[oss_meta_key]}")
            #
            #
            #             if not self.check_bg_param(key,response.headers[oss_meta_key]):
            #                 if key == 'bg_1':
            #                     bg_1()
            #                 elif key == 'bg_2':
            #                     bg_2()
            #                 elif key == 'bg_3':
            #                     bg_3()
            #                 elif key == 'bg_4':
            #                     bg_4()
            #     except requests.ConnectionError:
            #         print(f"网络连接错误，无法检查 {key} 的更新，跳过更新检查。")
            if 'x-oss-meta-id' in response.headers:
                self.oss_meta_id = float(response.headers['x-oss-meta-id'])
                print(f"获取到的 x-oss-meta-id: {self.oss_meta_id}")

                if self.oss_meta_id > self.local_version_id:
                    print("有新版本，开始提示用户...")
                    update_prompt = QMessageBox.question(
                        None,  # 父窗口，可以为 None
                        "检测到新版本",
                        f"最新版本为: V{self.oss_meta_id}\n是否前往更新?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )
                    if update_prompt == QMessageBox.StandardButton.Yes:
                        print("有新版本，打开下载程序...")
                        subprocess.Popen("检查更新.exe")
                        sys.exit()
        except requests.ConnectionError:
            print("网络连接错误，无法检查更新，跳过更新检查。")

    def check_for_ysdate(self):
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_ysurl, headers=headers)
            print(response)
            self.oss_meta_ys = float(response.headers['x-oss-meta-ys'])
            print(f"获取到的 x-oss-meta-ys: {self.oss_meta_ys}")
            # if self.oss_meta_ys > self.local_version_ys:


        except requests.ConnectionError:
            print("网络连接错误，无法检查更新，跳过更新检查。")
    def check_for_xtdate(self):
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_xturl, headers=headers)
            print(response)
            self.oss_meta_xt = float(response.headers['x-oss-meta-xt'])
            print(f"获取到的 x-oss-meta-xt: {self.oss_meta_xt}")

        except requests.ConnectionError:
            print("网络连接错误，无法检查更新，跳过更新检查。")

    def check_for_b3date(self):
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_b3url, headers=headers)
            print(response)
            self.oss_meta_b3 = float(response.headers['x-oss-meta-b3'])
            print(f"获取到的 x-oss-meta-b3: {self.oss_meta_b3}")

        except requests.ConnectionError:
            print("网络连接错误，无法检查更新，跳过更新检查。")

    def check_for_zzzdate(self):
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_zzzurl, headers=headers)
            print(response)
            self.oss_meta_zzz = float(response.headers['x-oss-meta-zzz'])
            print(f"获取到的 x-oss-meta-zzz: {self.oss_meta_zzz}")

        except requests.ConnectionError:
            print("网络连接错误，无法检查更新，跳过更新检查。")

    # https://wj.qq.com/s2/15022705/76fe/
    # def submit_to_tencent_form(self,feedback_type, content):
    #     """
    #     提交反馈到腾讯表单
    #     """
    #     url = 'https://wj.qq.com/s2/15022705/76fe/'  # 替换为你的腾讯表单提交链接
    #
    #     # 替换为实际的表单字段ID和用户提供的数据
    #     data = {
    #         'q-2-RXsj': {'value': feedback_type}, # 替换为实际的表单字段ID
    #         'q-3-i9ta': {'value': content}
    #     }
    #     try:
    #         response = requests.post(url, json=data)  # 使用 json 参数而不是 data，这取决于服务器的要求
    #         if response.status_code == 200:
    #             print("反馈提交成功！")
    #         else:
    #             print("提交失败，状态码：", response.status_code)
    #     except requests.RequestException as e:
    #         print("提交失败：", e)
    #
    # def show_message_box(self):
    #     """
    #     显示一个消息弹窗，并带有两个单选按钮和一个大的文本框。
    #     """
    #     dialog = QDialog()
    #     dialog.setWindowTitle("反馈或建议")
    #
    #     # 创建单选按钮和文本框并设置布局
    #     layout = QVBoxLayout()
    #
    #     radio_feedback = QRadioButton("问题反馈")
    #     radio_suggestion = QRadioButton("更新建议")
    #     text_edit = QTextEdit()
    #     text_edit.setFixedHeight(200)
    #
    #     layout.addWidget(radio_feedback)
    #     layout.addWidget(radio_suggestion)
    #     layout.addWidget(text_edit)
    #
    #     # 创建确定和取消按钮
    #     button_layout = QHBoxLayout()
    #     ok_button = QPushButton("确定")
    #     cancel_button = QPushButton("取消")
    #
    #     # 将按钮与槽函数连接
    #     def on_ok_clicked():
    #         feedback_type = "问题反馈" if radio_feedback.isChecked() else "更新建议"
    #         content = text_edit.toPlainText()
    #         self.submit_to_tencent_form(feedback_type, content)
    #         dialog.accept()
    #
    #     ok_button.clicked.connect(on_ok_clicked)
    #     cancel_button.clicked.connect(dialog.reject)
    #
    #     # 将按钮添加到水平布局
    #     button_layout.addWidget(ok_button)
    #     button_layout.addWidget(cancel_button)
    #
    #     # 将水平布局添加到垂直布局的底部
    #     layout.addLayout(button_layout)
    #
    #     dialog.setLayout(layout)
    #
    #     dialog.exec()
    def restart(self):
        os.execv(sys.executable, ['python'] + sys.argv)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 窗口置顶
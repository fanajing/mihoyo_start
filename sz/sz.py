from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QTabWidget, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt, QSize, QCoreApplication, pyqtSignal, QObject
from PyQt6.QtCore import QByteArray
import configparser
import subprocess
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



        # # 更新按钮
        # scaled_pixmap = pixmap_cz.scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio)
        # self.chazhao_gx = QPushButton('', self)  # 注意，按钮的文字为空
        # self.chazhao_gx.setStyleSheet(f"border:none;")  # 移除按钮的边框
        # self.chazhao_gx.move(150, 500)
        # self.chazhao_gx.clicked.connect(self.button_click_gx)
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
        except (FileNotFoundError, UnicodeDecodeError, ValueError):
            # 如果文件不存在、编码错误或值错误，设置本地版本ID为0
            self.local_version_id = 0

        self.check_for_update()

    def check_for_update(self):
        headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
        response = requests.head(self.download_url, headers=headers)
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


    def restart(self):
        os.execv(sys.executable, ['python'] + sys.argv)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 窗口置顶
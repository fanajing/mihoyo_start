from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton
from PyQt6.QtWidgets import QTabWidget, QTabBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtCore import QSize, QCoreApplication
import configparser
import os
import sys
import base64
import base64a

class ys(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        config = configparser.ConfigParser()
        config.read('start_config.ini')
        ys_ml = config.get('DEFAULT', 'ys_ml', fallback=None)  # 如果'ys_ml'不存在，返回None
        ys_ml = ys_ml.strip('\'')  # 使用strip方法移除两边的单引号
        if ys_ml == '':  # 如果ys_ml的值为空字符
            icon_data = base64.b64decode(base64a.cz)  # 使用cz解码base64
            pixmap = QPixmap()
            pixmap.loadFromData(icon_data)  # 从数据加载Pixmap

            # 创建按钮
            self.button = QPushButton('', self)  # 注意，按钮的文字为空
            self.button.setStyleSheet(f"border:none;")  # 移除按钮的边框
            self.button.move(800, 600)
            self.button.clicked.connect(self.on_button_clicked)
            # 设置按钮的大小为图片的大小
            self.button.setFixedSize(pixmap.width(), pixmap.height())

            # 将图标设置为按钮的背景
            self.button.setIcon(QIcon(pixmap))
            self.button.setIconSize(QSize(pixmap.width(), pixmap.height()))  # 设置icon的大小

        else:  # 如果ys_ml的值不为空字符
            print('y')  # 打印 'y'
        # 使用base64a.cz创建图标


        with open('config.ini', 'r') as file:
            for line in file:
                if 'game_dynamic_bg_name=' in line:
                    game_dynamic_bg_name = line.split('=')[1].strip()
                    break

        # 构建背景图像文件路径
        bg = "bg/" + game_dynamic_bg_name

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap(image)

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

        self.image_label = QLabel("Image goes here", self)
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
        # 首先创建 configparser.ConfigParser 实例
        config = configparser.ConfigParser()

        # 确认正确读取 start_config.ini 文件（或者你需要读取的文件名）
        config.read('start_config.ini')

        # 以下为原有代码
        file_dialog = QFileDialog(self)  # 设置 ys 为 file_dialog 的父窗体
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # 设置为选择已存在的文件模式
        file_dialog.setNameFilter("Executable files (*.exe)")  # 设置只显示 .exe 文件

        if file_dialog.exec():  # 如果用户选择了
            file_name = file_dialog.selectedFiles()[0]  # 获取选定文件的路径
            if os.path.basename(file_name) != 'YuanShen.exe':
                print("请选择一个 yuanshen.exe 文件")
            else:
                upper_directory = os.path.dirname(file_name)  # 获取文件的上一级目录
                grandparent_directory = os.path.dirname(upper_directory)
                # 这里调用 set 方法更改配置项
                config.set('DEFAULT', 'ys_ml', grandparent_directory)
                # 打开文件并保存配置
                with open('start_config.ini', 'w') as configfile:
                    config.write(configfile)
        else:
            print("用户取消选择")


from PyQt6.QtWidgets import QApplication,QTabWidget, QTabBar, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QIcon,QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import QTimer, Qt
import os

class ys(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


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




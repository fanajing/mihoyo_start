from PyQt6.QtWidgets import QApplication, QTabWidget, QLabel, QTabBar
from PyQt6.QtGui import QPixmap, QIcon,QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QByteArray
from ys.main_ys import ys # 原神
from xqtd.main_xqtd import xqtd  # 星穹铁道
from zzz.main_zzz import zzz  # 绝区零
from bh3.main_bh3 import bh3  # 崩坏3
from sz.sz import sz  # 设置
import base64
import configparser
import os
from base64a import bg

app = QApplication([])

base64_image = base64.b64decode(bg)
config = configparser.ConfigParser()
config.read('start_config.ini')
ys_ml = config.get('DEFAULT', 'ys_ml')
ys_config = os.path.join(ys_ml, 'config.ini')
ys_config = ys_config.replace('\\', '/')
ys_bg=os.path.join(ys_ml,'bg')
ys_bg = ys_bg.replace('\\', '/')

def on_tab_changed(index):
    if index == 0:  # 第一个选项卡
        if os.path.exists(ys_config):
            with open(ys_config, 'r') as file:
                for line in file:
                    if 'game_dynamic_bg_name=' in line:
                        game_dynamic_bg_name = line.split('=')[1].strip()
                        break

            # 构建背景图像文件路径
            bg = ys_bg +'/'+ game_dynamic_bg_name
            image_reader = QImageReader(bg)
            image = image_reader.read()
            pixmap = QPixmap.fromImage(image)
        else:
           data = base64_image
           pixmap = QPixmap()
           pixmap.loadFromData(QByteArray(data))

        # 控制 QTabWidget 显示在适当位置
        tabs.resize(pixmap.width(), pixmap.height())
    
        # 设置背景图像
        palette = tabs.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        tabs.setPalette(palette)
        tabs.setAutoFillBackground(True)

    elif index == 2:  # 第二个选项卡
        with open('xqtd/config.ini', 'r') as file:
            for line in file:
                if 'game_dynamic_bg_name=' in line:
                    game_dynamic_bg_name = line.split('=')[1].strip()
                    break

            # 构建背景图像文件路径
        bg = "bg/" + game_dynamic_bg_name

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap.fromImage(image)

        # 控制 QTabWidget 显示在适当位置
        tabs.resize(pixmap.width(), pixmap.height())

        # 设置背景图像
        palette = tabs.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        tabs.setPalette(palette)
        tabs.setAutoFillBackground(True)
    # 以此类推，你可以添加更多的条件以处理更多的选项卡
    elif index == 4:  # 第三个选项卡
        with open('zzz/config.ini', 'r') as file:
            for line in file:
                if 'game_dynamic_bg_name=' in line:
                    game_dynamic_bg_name = line.split('=')[1].strip()
                    break

            # 构建背景图像文件路径
        bg = "bg/" + game_dynamic_bg_name

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap.fromImage(image)

        # 控制 QTabWidget 显示在适当位置
        tabs.resize(pixmap.width(), pixmap.height())

        # 设置背景图像
        palette = tabs.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        tabs.setPalette(palette)
        tabs.setAutoFillBackground(True)
    elif index == 6:  # 第三个选项卡
        with open('bh3/config.ini', 'r') as file:
            for line in file:
                if 'game_dynamic_bg_name=' in line:
                    game_dynamic_bg_name = line.split('=')[1].strip()
                    break

            # 构建背景图像文件路径
        bg = "bg/" + game_dynamic_bg_name

        image_reader = QImageReader(bg)
        image = image_reader.read()
        pixmap = QPixmap.fromImage(image)

        # 控制 QTabWidget 显示在适当位置
        tabs.resize(pixmap.width(), pixmap.height())

        # 设置背景图像
        palette = tabs.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        tabs.setPalette(palette)
        tabs.setAutoFillBackground(True)
    elif index == 8:  # 第四个选项卡
        data = base64_image
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(data))

        tabs.resize(pixmap.width(), pixmap.height())

        # 设置背景图像
        palette = tabs.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        tabs.setPalette(palette)
        tabs.setAutoFillBackground(True)


if os.path.exists(ys_config):
    with open(ys_config, 'r') as file:
        for line in file:
            if 'game_dynamic_bg_name=' in line:
                game_dynamic_bg_name = line.split('=')[1].strip()
                break

    # 构建背景图像文件路径
    bg = ys_bg +'/'+ game_dynamic_bg_name

    image_reader = QImageReader(bg)
    image = image_reader.read()
    pixmap = QPixmap.fromImage(image)

else:
    data = base64_image
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray(data))

tabs = QTabWidget()
tabs.addTab(ys(), "")
index = tabs.addTab(QLabel('Disabled Tab'), '  ')
tabs.addTab(xqtd(), "")
index2 = tabs.addTab(QLabel('Disabled Tab'), '  ')
tabs.addTab(zzz(), "")
index3 = tabs.addTab(QLabel('Disabled Tab'), '  ')
tabs.addTab(bh3(), "")
indexx = tabs.addTab(QLabel('Disabled Tab'), '                        ')
tabs.setTabEnabled(index, False)  # 禁用选项卡
tabs.setTabEnabled(index2, False)  # 禁用选项卡
tabs.setTabEnabled(index3, False)  # 禁用选项卡
tabs.setTabEnabled(indexx, False)  # 禁用选项卡
tabs.setUsesScrollButtons(False)
tabs.addTab(sz(), "")


# 控制 QTabWidget 显示在适当位置
tabs.setGeometry(0, 0, pixmap.width(), pixmap.height())

# 设置背景图像
palette = tabs.palette()
palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
tabs.setPalette(palette)
tabs.setAutoFillBackground(True)
tabs.setFixedSize(pixmap.width(), pixmap.height())

tab_bar = tabs.tabBar()
tabs.setStyleSheet("QTabWidget::pane { border: 0; } QTabBar::tab {background-color: rgba(0,0,0,30%);}")

#原神
label1 = QLabel()
YS = QPixmap("image/ys.png")
ys = YS.scaled(70, 70, Qt.AspectRatioMode.IgnoreAspectRatio)
label1.setPixmap(ys)
tab_bar.setTabButton(0, QTabBar.ButtonPosition.LeftSide, label1)

#星穹铁道
label2 = QLabel()
XQTD = QPixmap("image/xqtd.png")
xqtd = XQTD.scaled(70, 70, Qt.AspectRatioMode.IgnoreAspectRatio)
label2.setPixmap(xqtd)
tab_bar.setTabButton(2, QTabBar.ButtonPosition.LeftSide, label2)

#绝区零
label3 = QLabel()
ZZZ = QPixmap("image/zzz.png")
zzz = ZZZ.scaled(70, 70, Qt.AspectRatioMode.IgnoreAspectRatio)
label3.setPixmap(zzz)
tab_bar.setTabButton(4, QTabBar.ButtonPosition.LeftSide, label3)

#崩坏3
label4 = QLabel()
HB3 = QPixmap("image/bh3.png")
bh3 = HB3.scaled(70, 70, Qt.AspectRatioMode.IgnoreAspectRatio)
label4.setPixmap(bh3)
tab_bar.setTabButton(6, QTabBar.ButtonPosition.LeftSide, label4)

#设置
label5 = QLabel()
SZ = QPixmap("image/sz.png")
sz = SZ.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)
label5.setPixmap(sz)
tab_bar.setTabButton(8, QTabBar.ButtonPosition.LeftSide, label5)


tabs.setTabPosition(QTabWidget.TabPosition.East)
# 获取屏幕宽度和高度
screen = app.primaryScreen().geometry()
# 设置窗口的位置和大小，使其居中
tabs.setGeometry((screen.width()-pixmap.width())//2, (screen.height()-pixmap.height())//2, pixmap.width(), pixmap.height())
tabs.currentChanged.connect(on_tab_changed)
tabs.setWindowTitle("米哈游启动器")
tabs.setWindowIcon(QIcon('image/caoyuansu.ico'))
tabs.show()
tabs.setCurrentIndex(8)
app.exec()
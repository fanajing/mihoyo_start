from PyQt6.QtWidgets import QApplication, QTabWidget, QLabel, QTabBar
from PyQt6.QtGui import QPixmap, QIcon,QImageReader, QGuiApplication, QPalette, QBrush
from PyQt6.QtCore import Qt
from ys.main_ys import ys # 原神
from xqtd.main_xqtd import xqtd  # 星穹铁道
from zzz.main_zzz import zzz  # 绝区零
from bh3.main_bh3 import bh3  # 崩坏3
app = QApplication([])

def on_tab_changed(index):
    if index == 0:  # 第一个选项卡
        with open('config.ini', 'r') as file:
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

    elif index == 1:  # 第二个选项卡
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
    elif index == 2:  # 第三个选项卡
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
    elif index == 3:  # 第三个选项卡
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





with open('config.ini', 'r') as file:
    for line in file:
        if 'game_dynamic_bg_name=' in line:
            game_dynamic_bg_name = line.split('=')[1].strip()
            break

# 构建背景图像文件路径
bg = "bg/"+game_dynamic_bg_name

image_reader = QImageReader(bg)
image = image_reader.read()
pixmap = QPixmap.fromImage(image)

tabs = QTabWidget()
tabs.addTab(ys(), "")
tabs.addTab(xqtd(), "")
tabs.addTab(zzz(), "")
tabs.addTab(bh3(), "")
index = tabs.addTab(QLabel('Disabled Tab'), '                    ')
tabs.setTabEnabled(index, False)  # 禁用选项卡
index = tabs.addTab(QLabel('Disabled Tab'), '                        ')
tabs.setUsesScrollButtons(False)
tabs.setTabEnabled(index, False)  # 禁用选项卡
# 控制 QTabWidget 显示在适当位置
tabs.setGeometry(0, 0, pixmap.width(), pixmap.height())

# 设置背景图像
palette = tabs.palette()
palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
tabs.setPalette(palette)
tabs.setAutoFillBackground(True)
tabs.setFixedSize(pixmap.width(), pixmap.height())

tab_bar = tabs.tabBar()
tabs.setStyleSheet("QTabWidget::pane { border: 0; } QTabBar::tab {background-color: rgba(0,0,0,50%);}")

#原神
label1 = QLabel()
YS = QPixmap("image/ys.png")
ys = YS.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)
label1.setPixmap(ys)
tab_bar.setTabButton(0, QTabBar.ButtonPosition.LeftSide, label1)

#星穹铁道
label2 = QLabel()
XQTD = QPixmap("image/xqtd.png")
xqtd = XQTD.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)
label2.setPixmap(xqtd)
tab_bar.setTabButton(1, QTabBar.ButtonPosition.LeftSide, label2)

#绝区零
label3 = QLabel()
ZZZ = QPixmap("image/zzz.png")
zzz = ZZZ.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)
label3.setPixmap(zzz)
tab_bar.setTabButton(2, QTabBar.ButtonPosition.LeftSide, label3)

#崩坏3
label4 = QLabel()
HB3 = QPixmap("image/bh3.png")
bh3 = HB3.scaled(100, 100, Qt.AspectRatioMode.IgnoreAspectRatio)
label4.setPixmap(bh3)
tab_bar.setTabButton(3, QTabBar.ButtonPosition.LeftSide, label4)

# Set tab position to the right side
tabs.setTabPosition(QTabWidget.TabPosition.East)
# 获取屏幕宽度和高度
screen = app.primaryScreen().geometry()
# 设置窗口的位置和大小，使其居中
tabs.setGeometry((screen.width()-pixmap.width())//2, (screen.height()-pixmap.height())//2, pixmap.width(), pixmap.height())

tabs.currentChanged.connect(on_tab_changed)
tabs.setWindowTitle("米哈游启动器")
tabs.setWindowIcon(QIcon('image/caoyuansu.ico'))
tabs.show()

app.exec()
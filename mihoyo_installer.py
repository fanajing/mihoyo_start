import sys
import requests
import zipfile
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt6.QtGui import QIcon

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("安装程序")
        self.setGeometry(100, 100, 380, 200)

        # 创建一个标签
        self.label = QLabel("请选择米哈游聚合启动器的launcher.exe程序", self)
        self.label.move(30, 50)
        self.label.setStyleSheet("font-size: 16px;")

        # 创建只读的文本框
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # 设置为只读
        self.text_edit.setText("")
        self.text_edit.setStyleSheet("border: 1px solid black;")
        self.text_edit.setGeometry(30, 100, 300, 30)  # 设置文本框的位置和大小

        # 创建一个按钮
        self.button1 = QPushButton("选择文件", self)
        self.button1.move(80, 150)
        self.button1.clicked.connect(self.open_file_dialog)  # 关联选择文件的槽函数

        # 创建一个按钮
        self.button2= QPushButton("开始安装", self)
        self.button2.move(200, 150)
        self.button2.clicked.connect(self.start_install)  # 关联开始安装的槽函数

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件", "", "launcher.exe")  # 只允许选择launcher.exe文件
        if file_path:
            self.text_edit.setText(file_path)

    def start_install(self):
        # 从 text_edit 获取路径
        selected_path = self.text_edit.toPlainText()
        if selected_path.endswith('exe'):
            selected_path = selected_path[:-13]
        selected_path=os.path.normpath(selected_path)
        extract_path = os.path.join(selected_path, 'games')  # 构建解压路径
        print(extract_path)
        #这里假设压缩包的 GitHub 下载链接
        github_zip_url = "https://codeload.github.com/fanajing/mihoyo_Releases/zip/refs/heads/main"
        response = requests.get(github_zip_url)
        if response.status_code == 200:
            with open("ceshi.zip", "wb") as file:
                file.write(response.content)
            with zipfile.ZipFile("ceshi.zip", 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            os.remove("ceshi.zip")  # 删除临时的压缩文件
        else:
            print("下载失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())


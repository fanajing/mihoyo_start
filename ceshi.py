import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
import logging

# 配置日志记录到文件
logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    class DirectoryCreatorApp(QWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("文件夹创建器")
            self.layout = QVBoxLayout()

            self.label = QLabel("文件夹位置：")
            self.layout.addWidget(self.label)

            self.directory_input = QLineEdit('C:/Program Files')
            self.layout.addWidget(self.directory_input)

            self.choose_directory_button = QPushButton('选择位置')
            self.choose_directory_button.clicked.connect(self.choose_directory)
            self.layout.addWidget(self.choose_directory_button)

            self.create_directory_button = QPushButton('创建文件夹')
            self.create_directory_button.clicked.connect(self.create_directory)
            self.layout.addWidget(self.create_directory_button)

            self.setLayout(self.layout)

        def choose_directory(self):
            default_location = "C:/Program Files"
            directory_name = QFileDialog.getExistingDirectory(self, '选择文件夹位置', default_location)
            if directory_name:
                self.directory_input.setText(directory_name)

        def create_directory(self):
            directory_name = self.directory_input.text()
            full_path = os.path.join(directory_name, 'mihoyostatic')
            try:
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
            except Exception as e:
                print(f"Error creating directory: {e}")

    app = QApplication(sys.argv)
    demo = DirectoryCreatorApp()
    demo.show()
    sys.exit(app.exec())
except Exception as e:
    # 当程序出错时，将错误信息记录到日志中
    logging.error(e, exc_info=True)

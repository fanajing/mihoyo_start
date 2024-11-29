import configparser
import os
import requests
import threading
import tkinter as tk
from tkinter import messagebox, ttk
import zipfile

# 本地配置文件路径
config_file_path = 'start_config.ini'

# 下载文件 URL
download_url = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/mihoyo_start.zip"

class DownloadApp:
    def __init__(self, master, download_url, config_file_path):
        self.master = master
        self.download_url = download_url
        self.config_file_path = config_file_path

        self.config = configparser.ConfigParser()
        self.local_version_id = 0
        self.oss_meta_id = 0

        self.progress_window = None
        self.progress_bar = None

        self.master.withdraw()  # 隐藏主窗口
        self.check_and_load_config()

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
        try:
            headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
            response = requests.head(self.download_url, headers=headers)
            if 'x-oss-meta-id' in response.headers:
                self.oss_meta_id = float(response.headers['x-oss-meta-id'])
                print(f"获取到的 x-oss-meta-id: {self.oss_meta_id}")

                if self.oss_meta_id > self.local_version_id:
                    print("有新版本，开始提示用户...")
                    update_prompt = messagebox.askyesno(
                        "检测到新版本",
                        f"当前版本为: V{self.local_version_id}\n最新版本为: V{self.oss_meta_id}\n是否更新?"
                    )

                    if update_prompt:
                        print("有新版本，开始下载...")
                        self.start_download_thread()
                    else:
                        self.master.quit()
                        self.master.destroy()
                else:
                    messagebox.showinfo("更新", f"当前是最新版本，版本号为：v{self.oss_meta_id}")
                    self.master.quit()
                    self.master.destroy()
            else:
                messagebox.showwarning("错误", "未找到版本文件")
                self.master.quit()
                self.master.destroy()

        except requests.RequestException:
        # 无网络状态下直接启动主程序
            print("无网络连接，直接启动程序")
            self.master.quit()
            self.master.destroy()

    def start_download_thread(self):
        download_thread = threading.Thread(target=self.download_and_extract, args=(self.download_url, os.getcwd()), daemon=True)
        download_thread.start()

    def update_local_version(self):
        if not self.config.has_section('OSS'):
            self.config.add_section('OSS')
        self.config.set('OSS', 'version_id', str(self.oss_meta_id))

        with open(self.config_file_path, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def show_progress_window(self, total_size):
        self.progress_window = tk.Toplevel(self.master)
        self.progress_window.title("更新")
        tk.Label(self.progress_window, text="下载进度:").pack(pady=10)
        self.progress_bar = ttk.Progressbar(self.progress_window, length=300, mode='determinate', maximum=total_size)
        self.progress_bar.pack(pady=10)

    def update_progress_bar(self, value):
        if self.progress_bar:
            self.progress_bar['value'] = value

    def download_and_extract(self, url, target_dir):
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))

            # 在主线程中创建进度条
            self.master.after(0, self.show_progress_window, total_size)

            file_path = os.path.join(target_dir, 'mihoyo_start.zip')
            with open(file_path, 'wb') as f:
                bytes_downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        bytes_downloaded += len(chunk)
                        # 在主线程中更新进度条
                        self.master.after(0, self.update_progress_bar, bytes_downloaded)

            extract_path = os.path.abspath(os.path.join(target_dir, os.pardir))
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            os.remove(file_path)  # 下载完成后删除临时的压缩文件


            self.master.after(0, self.progress_window.destroy)
            messagebox.showinfo("下载完成", f"最新版本已下载并解压，换服器版本更新为：v{self.oss_meta_id}。")
            self.update_local_version()
            self.master.quit()
            self.master.destroy()
        except Exception as e:
            self.master.after(0, lambda: messagebox.showerror("错误", f"下载或解压过程中出现错误: {e}"))
            self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = DownloadApp(root, download_url, config_file_path)
    root.mainloop()
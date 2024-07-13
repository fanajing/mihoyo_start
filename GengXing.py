import configparser
import requests
import os
import zipfile
import tkinter as tk
from tkinter import messagebox, ttk
import threading

# 本地配置文件路径
config_file_path = 'start_config.ini'

# 下载文件 URL
download_url = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/mihoyo_start.zip"

# 创建一个配置解析器
config = configparser.ConfigParser()

# 初始化 tkinter
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 检查并初始化本地配置文件
try:
    with open(config_file_path, 'r', encoding='utf-8') as f:
        config.read_file(f)
    # 如果配置文件中存在 version_id 则读取，否则默认设为 0
    if config.has_section('OSS') and config.has_option('OSS', 'version_id'):
        local_version_id = float(config.get('OSS', 'version_id'))
    else:
        local_version_id = 0
except (FileNotFoundError, UnicodeDecodeError, ValueError):
    # 如果文件不存在、编码错误或值错误，设置本地版本ID为0
    local_version_id = 0

# 发送HEAD请求以获取响应头中的 x-oss-meta-id
response = requests.head(download_url)
if 'x-oss-meta-id' in response.headers:
    oss_meta_id = float(response.headers['x-oss-meta-id'])
    print(f"获取到的 x-oss-meta-id: {oss_meta_id}")

    if oss_meta_id > local_version_id:
        print("有新版本，开始提示用户...")

        # 弹出对话框提示用户是否更新
        update_prompt = messagebox.askyesno(
            "检测到新版本",
            f"当前版本为: V{local_version_id}\n最新版本为: V{oss_meta_id}\n是否更新?"
        )

        # 比对 x-oss-meta-id 和本地的 version_id 并决定是否下载
        if update_prompt:
            print("有新版本，开始下载...")

            def download_and_extract(url, target_dir):
                response = requests.get(url, stream=True)
                total_size = int(response.headers.get('content-length', 0))

                progress_window = tk.Toplevel(root)
                progress_window.title("下载进度")
                tk.Label(progress_window, text="下载进度:").pack(pady=10)
                progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
                progress_bar.pack(pady=10)
                progress_bar['maximum'] = total_size

                file_path = os.path.join(target_dir, 'mihoyo_start.zip')

                with open(file_path, 'wb') as f:
                    bytes_downloaded = 0
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            bytes_downloaded += len(chunk)
                            progress_bar['value'] = bytes_downloaded
                            progress_window.update_idletasks()

                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(target_dir)
                os.remove(file_path)  # 下载完成后删除临时的压缩文件

                progress_window.destroy()  # 关闭进度窗口

            def start_download_thread(url, target_dir):
                download_thread = threading.Thread(target=download_and_extract, args=(url, target_dir))
                download_thread.start()

            # 下载并解压
            target_dir = os.getcwd()  # 当前运行目录
            parent_dir = os.path.dirname(target_dir)
            start_download_thread(download_url, parent_dir)

            # 更新本地配置文件中的 version_id 为 x-oss-meta-id
            if not config.has_section('OSS'):
                config.add_section('OSS')
            config.set('OSS', 'version_id', str(oss_meta_id))

            with open(config_file_path, 'w', encoding='utf-8') as configfile:
                config.write(configfile)

            # 下载完成提示
            messagebox.showinfo("下载完成", f"最新版本已下载并解压，换服器版本更新为：v{oss_meta_id}。")
    else:
        messagebox.showinfo("更新", f"当前是最新版本，版本号为：v{oss_meta_id}。")
else:
    # 提示未能获取到 x-oss-meta-id
    messagebox.showwarning("错误", "未找到版本文件")
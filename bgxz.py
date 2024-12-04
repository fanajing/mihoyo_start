import os
import requests
from PIL import Image

# # 下载目录
ys_bg = os.path.join('bg', 'ys')
# xqtd_bg = os.path.join('bg', 'xqtd')
# bh3_bg = os.path.join('bg', 'bh3')
# zzz_bg  = os.path.join('bg', 'zzz')
#
# # 确保下载目录存在
# os.makedirs(ys_bg, exist_ok=True)
# os.makedirs(xqtd_bg, exist_ok=True)
# os.makedirs(bh3_bg, exist_ok=True)
# os.makedirs(zzz_bg, exist_ok=True)
#
# # 下载URL
url_ys = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/ys.png"


# url_xqtd = "https://example.com/yourfile.zip"
# url_bh3 = "https://example.com/yourfile.zip"
# url_zzz = "https://example.com/yourfile.zip"
#
#


def download_ys():
    url_ys = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/ys.png"
    ys_bg = os.path.join(os.getcwd(), "bg", "ys")
    file_path = os.path.join(ys_bg, "ys.png")

    response = requests.get(url_ys, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"文件 {file_path} 下载成功")
    image = Image.open(file_path)
    image.save(file_path, 'PNG')
    print(f"文件 {image} 读取")
    resized_image = image.resize((1280, 730), Image.Resampling.LANCZOS)
    print(f"文件 {resized_image} 修改后")
    resized_image.save(file_path)



def download_xt():
    url_xt = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/xt.png"
    xt_bg = os.path.join(os.getcwd(), "bg", "xqtd")
    file_path = os.path.join(xt_bg, "xt.png")

    response = requests.get(url_xt, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"文件 {file_path} 下载成功")
    image = Image.open(file_path)
    image.save(file_path, 'PNG')
    print(f"文件 {image} 读取")
    resized_image = image.resize((1280, 730), Image.Resampling.LANCZOS)
    print(f"文件 {resized_image} 修改后")
    resized_image.save(file_path)

def download_b3():
    url_b3 = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/b3.png"
    b3_bg = os.path.join(os.getcwd(), "bg", "bh3")
    file_path = os.path.join(b3_bg, "b3.png")

    response = requests.get(url_b3, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"文件 {file_path} 下载成功")
    image = Image.open(file_path)
    image.save(file_path, 'PNG')
    print(f"文件 {image} 读取")
    resized_image = image.resize((1280, 730), Image.Resampling.LANCZOS)
    print(f"文件 {resized_image} 修改后")
    resized_image.save(file_path)

def download_zzz():
    url_zzz = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/zzz.png"
    zzz_bg = os.path.join(os.getcwd(), "bg", "zzz")
    file_path = os.path.join(zzz_bg, "zzz.png")

    response = requests.get(url_zzz, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"文件 {file_path} 下载成功")
    image = Image.open(file_path)
    image.save(file_path, 'PNG')
    print(f"文件 {image} 读取")
    resized_image = image.resize((1280, 730), Image.Resampling.LANCZOS)
    print(f"文件 {resized_image} 修改后")
    resized_image.save(file_path)
    #
    # except requests.RequestException as e:
    #     print(f"下载文件时出现错误: {e}")
    # except OSError as e:
    #     print(f"保存文件时出现本地文件系统错误: {e}")
    # except:
    #     print(f"图片处理过程中出现未知错误")

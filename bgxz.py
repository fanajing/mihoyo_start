import os
import requests

# 下载目录
ys_bg = os.path.join('bg', 'ys')
xqtd_bg = os.path.join('bg', 'xqtd')
bh3_bg = os.path.join('bg', 'bh3')
zzz_bg  = os.path.join('bg', 'zzz')

# 确保下载目录存在
os.makedirs(ys_bg, exist_ok=True)
os.makedirs(xqtd_bg, exist_ok=True)
os.makedirs(bh3_bg, exist_ok=True)
os.makedirs(zzz_bg, exist_ok=True)

# 下载URL
download_ys = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/bz/ys.png"
download_xqtd = "https://example.com/yourfile.zip"
download_bh3 = "https://example.com/yourfile.zip"
download_zzz = "https://example.com/yourfile.zip"





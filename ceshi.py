import requests


def get_headers(url):
    try:
        response = requests.head(url)  # 使用 HEAD 请求方法
        headers = response.headers

        # 输出所有头信息
        for key, value in headers.items():
            print(f"{key}: {value}")

    except requests.RequestException as e:
        print(f"请求发生错误: {e}")


if __name__ == "__main__":
    url = "https://mihoyostart.oss-cn-beijing.aliyuncs.com/mihoyo_start.zip"  # 将此更改为你的下载地址
    get_headers(url)
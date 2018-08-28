import urllib3
import re
import urllib.request

urllib3.disable_warnings()
http = urllib3.PoolManager()


def get_html(url, coding="gbk"):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"

    }
    r = http.request('GET', url, headers=headers, retries=5, redirect=500)
    return r.data.decode(coding, "ignore")


def get_html_with_referer(url, referer, coding="gbk"):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Referer": referer
    }
    r = http.request('GET', url, headers=headers, retries=5, redirect=500)
    return r.data.decode(coding, "ignore")

def get_html2(url):
    r = urllib.request.urlopen(url).read()
    return r.decode("gbk", "ignore")


def download_img(path, url, prefix_name=""):
    create_folder(path)
    name = re.split("/", url)
    name = prefix_name + "_" + name[len(name) - 1]
    path = path + name
    r = http.request('GET', url, preload_content=False)
    with open(path, 'wb') as out:
        while True:
            data = r.read()
            if not data:
                break
            out.write(data)


def create_folder(path):
    # 引入模块
    import os
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':
    url = "http://127.0.0.1:8888/inputtest?name=ccfeng"

    # html = get_html_with_referer(url2, url)
    html = get_html(url, 'utf-8')

    print(html)

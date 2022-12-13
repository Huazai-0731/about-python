# 导入 requests 库
import requests
# 导入 文件操作库
import os

from bs4 import BeautifulSoup

import sys

import importlib

importlib.reload(sys)

global headers

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
# 爬图地址
# webUrl = 'https://placekitten.com/'
webUrl = 'https://unsplash.com/es/t/nature'

# 定义存储位置

global current_path
current_path = os.path.dirname(__file__)

global save_path

save_path = os.path.join(current_path, '/py_data')

# 创建文件夹


def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)

    # 切换路径至上面创建的文件夹
    os.chdir(file_path)

#  下载文件
# todo


def download(file_path):
    return

# main


def main():

    res = requests.get(webUrl)

    soup = BeautifulSoup(res.text, 'html.parser')

    all_img = soup.find_all('img')

    print(all_img)

    # 创建文件夹

    createFile(save_path)

    count = 0
    for img in all_img:
        count = count + 1
        filename = str(count) + '.png'
        # 提取src
        url = img.attrs['src']

        href_sub = webUrl + url

        href_headers = {'Referer': href_sub}
        img = requests.get(href_sub, headers=href_headers)

        print('开始保存图片', save_path, img)

        file = save_path + '/' + filename

        f = open(file, 'ab')

        f.write(img.content)

        f.close()


if __name__ == '__main__':
    main()

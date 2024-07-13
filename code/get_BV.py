#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# 创建时间：2020-12-31 9:23
# 文件名称：get_BV.py
import requests
import re

headers = {
    "authority": "www.bilibili.com",
    "method": "GET",
    "path": "/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "cookie": "_uuid=D7B8DB0E-B75F-C0D4-0A78-C9BF304143D185218infoc; "
              "buvid3=B9FD1C8F-FB14-46C6-B992-9C65A8BA430A143108infoc; sid=b18op4gm; DedeUserID=51160844; "
              "DedeUserID__ckMd5=8ea87b40584db453; CURRENT_FNVAL=80; rpdid=|(J~l~|lRkRk0J'uY|kJ|Jk)u; "
              "CURRENT_QUALITY=120; LIVE_BUVID=AUTO5116023360721606; blackside_state=1; PVID=1; "
              "SESSDATA=607ed093%2C1619496042%2C76e46*a1; bili_jct=a26df988fa140f890978c893dd7c4573; "
              "bp_video_offset_51160844=455128463064631634; bp_t_offset_51160844=455726039049133355",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63 "}
# url = 'https://www.bilibili.com/bangumi/play/ep84340'
# r = requests.get(url, headers=headers)
# r.encoding = r.apparent_encoding
# p = r'"bvid":"(BV.{10})"'
# result = re.findall(p, str(r.text))
# print(result)
url = 'http://comment.bilibili.com/48126815.xml'
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
print(r.text)

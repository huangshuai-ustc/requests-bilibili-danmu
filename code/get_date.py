#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# 创建时间：2020-12-28 22:21
# 文件名称：get_date.py
import requests
import requests_cache
import ast
import time
import os
import json

os.chdir('E:/Output/curriculudesign/')
requests_cache.install_cache(backend='memory')
requests_cache.clear()
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
header = {
    "authority": "www.bilibili.com",
    "method": "GET",
    "path": "/",
    "scheme": "https",
    "accept": "textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "cookie": "_uuid=330736B7-3C8F-EC18-9BAF-B3C10F8B202235012infoc;buvid3=A87AABE4-0A2B-4D5C-8AAD"
              "-663C2A1A7A9C138376infoc; sid=8k8d6m0x; DedeUserID=218960786; DedeUserID__ckMd5=9c190ccc5e2169eb; "
              "SESSDATA=9a77ad7c%2C1616942445%2Cc44d3*91; bili_jct=8802bb967bbffcfd497fe7957747bdd3; "
              "CURRENT_FNVAL=80; blackside_state=1; rpdid=|(umumRmukmm0J'uY|uJm|~~Y; LIVE_BUVID=AUTO6016017269775483; "
              "CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1608252121; "
              "fingerprint3=022994f47e992b484c73ff68db4fa513; fingerprint=58aa96e70649ee998e72e336682463a5; "
              "fingerprint_s=a75092ebfc742be9d664cc54cd8234d8; "
              "buivd_fp=A87AABE4-0A2B-4D5C-8AAD-663C2A1A7A9C138376infoc; "
              "buvid_fp_plain=A87AABE4-0A2B-4D5C-8AAD-663C2A1A7A9C138376infoc; "
              "bp_video_offset_218960786=473783090874722027; bp_t_offset_218960786=473783090874722027; "
              "_dfcaptcha=3ca78df22cbc687683b99aacf4c648af; PVID=1; finger=158939783",
    "dnt": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69 "}


def get_cid(BV_Number):
    url = "https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp"
    r = requests.get(url.format(BV_Number), headers=headers)
    r.encoding = r.apparent_encoding
    cid = ast.literal_eval(r.text)["data"][0]["cid"]
    return cid


cid = get_cid('BV1cs411Q71j')  # 48126815

if __name__ == '__main__':
    date_all = []
    month = ['2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05',
             '2018-06', '2018-07', '2018-07', '2018-08']
    for i in month:
        url = 'http://api.bilibili.com/x/v2/dm/history/index?type=1&oid={}&month=%s'.format(cid) % i
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        date = json.loads(r.text)["data"]
        if date is None:
            pass
        else:
            for i in date:
                date_all.append(i)
    print(date_all)

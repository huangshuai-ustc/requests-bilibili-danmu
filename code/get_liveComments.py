#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# 创建时间：2020-12-28 22:21
# 文件名称：get_liveComments.py
import requests
import requests_cache
from bs4 import BeautifulSoup
from 程序.get_date import cid

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
date = [
    '2017-09-01',
    '2017-09-02',
    '2017-09-03',
    '2017-09-04',
    '2017-09-05',
    '2017-09-06',
    '2017-09-07',
    '2017-09-08',
    '2017-09-09',
    '2017-09-10',
    '2017-09-11',
    '2017-09-12',
    '2017-09-13',
    '2017-09-14',
    '2017-09-15',
    '2017-09-16',
    '2017-09-17',
    '2017-09-18',
    '2017-09-19',
    '2017-09-20',
    '2017-09-21',
    '2017-09-22',
    '2017-09-23',
    '2017-09-24',
    '2017-09-25',
    '2017-09-26',
    '2017-09-27',
    '2017-09-28',
    '2017-09-29',
    '2017-09-30',
    '2017-10-01',
    '2017-10-02',
    '2017-10-03',
    '2017-10-04',
    '2017-10-05',
    '2017-10-06',
    '2017-10-07',
    '2017-10-08',
    '2017-10-09',
    '2017-10-10',
    '2017-10-11',
    '2017-10-12',
    '2017-10-13',
    '2017-10-14',
    '2017-10-15',
    '2017-10-16',
    '2017-10-17',
    '2017-10-18',
    '2017-10-19',
    '2017-10-20',
    '2017-10-21',
    '2017-10-22',
    '2017-10-23',
    '2017-10-24',
    '2017-10-25',
    '2017-10-26',
    '2017-10-27',
    '2017-10-28',
    '2017-10-29',
    '2017-10-30',
    '2017-10-31',
    '2017-11-01',
    '2017-11-02',
    '2017-11-03',
    '2017-11-04',
    '2017-11-05',
    '2017-11-06',
    '2017-11-07',
    '2017-11-08',
    '2017-11-09',
    '2017-11-10',
    '2017-11-11',
    '2017-11-12',
    '2017-11-13',
    '2017-11-14',
    '2017-11-15',
    '2017-11-16',
    '2017-11-17',
    '2017-11-18',
    '2017-11-19',
    '2017-11-20',
    '2017-11-21',
    '2017-11-22',
    '2017-11-23',
    '2017-11-24',
    '2017-11-25',
    '2017-11-26',
    '2017-11-27',
    '2017-11-28',
    '2017-11-29',
    '2017-11-30',
    '2017-12-01',
    '2017-12-02',
    '2017-12-03',
    '2017-12-04',
    '2017-12-05',
    '2017-12-06',
    '2017-12-07',
    '2017-12-08',
    '2017-12-09',
    '2017-12-10',
    '2017-12-11',
    '2017-12-12',
    '2017-12-13',
    '2017-12-14',
    '2017-12-15',
    '2017-12-16',
    '2017-12-17',
    '2017-12-18',
    '2017-12-19',
    '2017-12-20',
    '2017-12-21',
    '2017-12-22',
    '2017-12-23',
    '2017-12-24',
    '2017-12-25',
    '2017-12-26',
    '2017-12-27',
    '2017-12-28',
    '2017-12-29',
    '2017-12-30',
    '2017-12-31',
    '2018-01-01',
    '2018-01-02',
    '2018-01-03',
    '2018-01-04',
    '2018-01-05',
    '2018-01-06',
    '2018-01-07',
    '2018-01-08',
    '2018-01-09',
    '2018-01-10',
    '2018-01-11',
    '2018-01-12',
    '2018-01-13',
    '2018-01-14',
    '2018-01-15',
    '2018-01-16',
    '2018-01-17',
    '2018-01-18',
    '2018-01-19',
    '2018-01-20',
    '2018-01-21',
    '2018-01-22',
    '2018-01-23',
    '2018-01-24',
    '2018-01-25',
    '2018-01-26',
    '2018-01-27',
    '2018-01-28',
    '2018-01-29',
    '2018-01-30',
    '2018-01-31',
    '2018-02-01',
    '2018-02-02',
    '2018-02-03',
    '2018-02-04',
    '2018-02-05',
    '2018-02-06',
    '2018-02-07',
    '2018-02-08',
    '2018-02-09',
    '2018-02-10',
    '2018-02-11',
    '2018-02-12',
    '2018-02-13',
    '2018-02-14',
    '2018-02-15',
    '2018-02-16',
    '2018-02-17',
    '2018-02-18',
    '2018-02-19',
    '2018-02-20',
    '2018-02-21',
    '2018-02-22',
    '2018-02-23',
    '2018-02-24',
    '2018-02-25',
    '2018-02-26',
    '2018-02-27',
    '2018-02-28',
    '2018-03-01',
    '2018-03-02',
    '2018-03-03',
    '2018-03-04',
    '2018-03-05',
    '2018-03-06',
    '2018-03-07',
    '2018-03-08',
    '2018-03-09',
    '2018-03-10',
    '2018-03-11',
    '2018-03-12',
    '2018-03-13',
    '2018-03-14',
    '2018-03-15',
    '2018-03-16',
    '2018-03-17',
    '2018-03-18',
    '2018-03-19',
    '2018-03-20',
    '2018-03-21',
    '2018-03-22',
    '2018-03-23',
    '2018-03-24',
    '2018-03-25',
    '2018-03-26',
    '2018-03-27',
    '2018-03-28',
    '2018-03-29',
    '2018-03-30',
    '2018-03-31',
    '2018-04-01',
    '2018-04-02',
    '2018-04-03',
    '2018-04-04',
    '2018-04-05',
    '2018-04-06',
    '2018-04-07',
    '2018-04-08',
    '2018-04-09',
    '2018-04-10',
    '2018-04-11',
    '2018-04-12',
    '2018-04-13',
    '2018-04-14',
    '2018-04-15',
    '2018-04-16',
    '2018-04-17',
    '2018-04-18',
    '2018-04-19',
    '2018-04-20',
    '2018-04-21',
    '2018-04-22',
    '2018-04-23',
    '2018-04-24',
    '2018-04-25',
    '2018-04-26',
    '2018-04-27',
    '2018-04-28',
    '2018-04-29',
    '2018-04-30',
    '2018-05-01',
    '2018-05-02',
    '2018-05-03',
    '2018-05-04',
    '2018-05-05',
    '2018-05-06',
    '2018-05-07',
    '2018-05-08',
    '2018-05-09',
    '2018-05-10',
    '2018-05-11',
    '2018-05-12',
    '2018-05-13',
    '2018-05-14',
    '2018-05-15',
    '2018-05-16',
    '2018-05-17',
    '2018-05-18',
    '2018-05-19',
    '2018-05-20',
    '2018-05-21',
    '2018-05-22',
    '2018-05-23',
    '2018-05-24',
    '2018-05-25',
    '2018-05-26',
    '2018-05-27',
    '2018-05-28',
    '2018-05-29',
    '2018-05-30',
    '2018-05-31',
    '2018-06-01',
    '2018-06-02',
    '2018-06-03',
    '2018-06-04',
    '2018-06-05',
    '2018-06-06',
    '2018-06-07',
    '2018-06-08',
    '2018-06-09',
    '2018-06-10',
    '2018-06-11',
    '2018-06-12',
    '2018-06-13',
    '2018-06-14',
    '2018-06-15',
    '2018-06-16',
    '2018-06-17',
    '2018-06-18',
    '2018-06-19',
    '2018-06-20',
    '2018-06-21',
    '2018-06-22',
    '2018-06-23',
    '2018-06-24',
    '2018-06-25',
    '2018-06-26',
    '2018-06-27',
    '2018-06-28',
    '2018-06-29',
    '2018-06-30',
    '2018-07-01',
    '2018-07-02',
    '2018-07-03',
    '2018-07-04',
    '2018-07-05',
    '2018-07-06',
    '2018-07-07',
    '2018-07-08',
    '2018-07-09',
    '2018-07-10',
    '2018-07-11',
    '2018-07-12',
    '2018-07-13',
    '2018-07-14',
    '2018-07-15',
    '2018-07-16',
    '2018-07-17',
    '2018-07-18',
    '2018-07-19',
    '2018-07-20',
    '2018-07-21',
    '2018-07-22',
    '2018-07-23',
    '2018-07-24',
    '2018-07-25',
    '2018-07-26',
    '2018-07-27',
    '2018-07-28',
    '2018-07-29',
    '2018-07-30',
    '2018-07-31',
    '2018-07-01',
    '2018-07-02',
    '2018-07-03',
    '2018-07-04',
    '2018-07-05',
    '2018-07-06',
    '2018-07-07',
    '2018-07-08',
    '2018-07-09',
    '2018-07-10',
    '2018-07-11',
    '2018-07-12',
    '2018-07-13',
    '2018-07-14',
    '2018-07-15',
    '2018-07-16',
    '2018-07-17',
    '2018-07-18',
    '2018-07-19',
    '2018-07-20',
    '2018-07-21',
    '2018-07-22',
    '2018-07-23',
    '2018-07-24',
    '2018-07-25',
    '2018-07-26',
    '2018-07-27',
    '2018-07-28',
    '2018-07-29',
    '2018-07-30',
    '2018-07-31',
    '2018-08-01',
    '2018-08-02',
    '2018-08-03',
    '2018-08-04',
    '2018-08-05',
    '2018-08-06',
    '2018-08-07',
    '2018-08-08',
    '2018-08-09',
    '2018-08-10',
    '2018-08-11',
    '2018-08-12',
    '2018-08-13',
    '2018-08-14',
    '2018-08-15',
    '2018-08-16',
    '2018-08-17',
    '2018-08-18',
    '2018-08-19',
    '2018-08-20',
    '2018-08-21',
    '2018-08-22',
    '2018-08-23',
    '2018-08-24',
    '2018-08-25',
    '2018-08-26',
    '2018-08-27',
    '2018-08-28',
    '2018-08-29',
    '2018-08-30',
    '2018-08-31',
    '2018-09-01',
    '2018-09-02',
    '2018-09-03',
    '2018-09-04',
    '2018-09-05',
    '2018-09-06',
    '2018-09-07',
    '2018-09-08',
    '2018-09-09',
    '2018-09-10',
    '2018-09-11',
    '2018-09-12',
    '2018-09-13',
    '2018-09-14',
    '2018-09-15',
    '2018-09-16',
    '2018-09-17',
    '2018-09-18',
    '2018-09-19',
    '2018-09-20',
    '2018-09-21',
    '2018-09-22',
    '2018-09-23',
    '2018-09-24',
    '2018-09-25',
    '2018-09-26',
    '2018-09-27',
    '2018-09-28',
    '2018-09-29',
    '2018-09-30',
    '2018-10-01',
    '2018-10-02',
    '2018-10-03',
    '2018-10-04',
    '2018-10-05',
    '2018-10-06',
    '2018-10-07',
    '2018-10-08',
    '2018-10-09',
    '2018-10-10',
    '2018-10-11',
    '2018-10-12',
    '2018-10-13',
    '2018-10-14',
    '2018-10-15',
    '2018-10-16',
    '2018-10-17',
    '2018-10-18',
    '2018-10-19',
    '2018-10-20',
    '2018-10-21',
    '2018-10-22',
    '2018-10-23',
    '2018-10-24',
    '2018-10-25',
    '2018-10-26',
    '2018-10-27',
    '2018-10-28',
    '2018-10-29',
    '2018-10-30',
    '2018-10-31',
    '2018-11-01',
    '2018-11-02',
    '2018-11-03',
    '2018-11-04',
    '2018-11-05',
    '2018-11-06',
    '2018-11-07',
    '2018-11-08',
    '2018-11-09',
    '2018-11-10',
    '2018-11-11',
    '2018-11-12',
    '2018-11-13',
    '2018-11-14',
    '2018-11-15',
    '2018-11-16',
    '2018-11-17',
    '2018-11-18',
    '2018-11-19',
    '2018-11-20',
    '2018-11-21',
    '2018-11-22',
    '2018-11-23',
    '2018-11-24',
    '2018-11-25',
    '2018-11-26',
    '2018-11-27',
    '2018-11-28',
    '2018-11-29',
    '2018-11-30',
    '2018-12-01',
    '2018-12-02',
    '2018-12-03',
    '2018-12-04',
    '2018-12-05',
    '2018-12-06',
    '2018-12-07',
    '2018-12-08',
    '2018-12-09',
    '2018-12-10',
    '2018-12-11',
    '2018-12-12',
    '2018-12-13',
    '2018-12-14',
    '2018-12-15',
    '2018-12-16',
    '2018-12-17',
    '2018-12-18',
    '2018-12-19',
    '2018-12-20',
    '2018-12-21',
    '2018-12-22',
    '2018-12-23',
    '2018-12-24',
    '2018-12-25',
    '2018-12-26',
    '2018-12-27',
    '2018-12-28',
    '2018-12-29',
    '2018-12-30',
    '2018-12-31',
    '2019-01-01',
    '2019-01-02',
    '2019-01-03',
    '2019-01-04',
    '2019-01-05',
    '2019-01-06',
    '2019-01-07',
    '2019-01-08',
    '2019-01-09',
    '2019-01-10',
    '2019-01-11',
    '2019-01-12',
    '2019-01-13',
    '2019-01-14',
    '2019-01-15',
    '2019-01-16',
    '2019-01-17',
    '2019-01-18',
    '2019-01-19',
    '2019-01-20',
    '2019-01-21',
    '2019-01-22',
    '2019-01-23',
    '2019-01-24',
    '2019-01-25',
    '2019-01-26',
    '2019-01-27',
    '2019-01-28',
    '2019-01-29',
    '2019-01-30',
    '2019-01-31',
    '2019-02-01',
    '2019-02-02',
    '2019-02-03',
    '2019-02-04',
    '2019-02-05',
    '2019-02-06',
    '2019-02-07',
    '2019-02-08',
    '2019-02-09',
    '2019-02-10',
    '2019-02-11',
    '2019-02-12',
    '2019-02-13',
    '2019-02-14',
    '2019-02-15',
    '2019-02-16',
    '2019-02-17',
    '2019-02-18',
    '2019-02-19',
    '2019-02-20',
    '2019-02-21',
    '2019-02-22',
    '2019-02-23',
    '2019-02-24',
    '2019-02-25',
    '2019-02-26',
    '2019-02-27',
    '2019-02-28',
    '2019-03-01',
    '2019-03-02',
    '2019-03-03',
    '2019-03-04',
    '2019-03-05',
    '2019-03-06',
    '2019-03-07',
    '2019-03-08',
    '2019-03-09',
    '2019-03-10',
    '2019-03-11',
    '2019-03-12',
    '2019-03-13',
    '2019-03-14',
    '2019-03-15',
    '2019-03-16',
    '2019-03-17',
    '2019-03-18',
    '2019-03-19',
    '2019-03-20',
    '2019-03-21',
    '2019-03-22',
    '2019-03-23',
    '2019-03-24',
    '2019-03-25',
    '2019-03-26',
    '2019-03-27',
    '2019-03-28',
    '2019-03-29',
    '2019-03-30',
    '2019-03-31',
    '2019-04-01',
    '2019-04-02',
    '2019-04-03',
    '2019-04-04',
    '2019-04-05',
    '2019-04-06',
    '2019-04-07',
    '2019-04-08',
    '2019-04-09',
    '2019-04-10',
    '2019-04-11',
    '2019-04-12',
    '2019-04-13',
    '2019-04-14',
    '2019-04-15',
    '2019-04-16',
    '2019-04-17',
    '2019-04-18',
    '2019-04-19',
    '2019-04-20',
    '2019-04-21',
    '2019-04-22',
    '2019-04-23',
    '2019-04-24',
    '2019-04-25',
    '2019-04-26',
    '2019-04-27',
    '2019-04-28',
    '2019-04-29',
    '2019-04-30',
    '2019-05-01',
    '2019-05-02',
    '2019-05-03',
    '2019-05-04',
    '2019-05-05',
    '2019-05-06',
    '2019-05-07',
    '2019-05-08',
    '2019-05-09',
    '2019-05-10',
    '2019-05-11',
    '2019-05-12',
    '2019-05-13',
    '2019-05-14',
    '2019-05-15',
    '2019-05-16',
    '2019-05-17',
    '2019-05-18',
    '2019-05-19',
    '2019-05-20',
    '2019-05-21',
    '2019-05-22',
    '2019-05-23',
    '2019-05-24',
    '2019-05-25',
    '2019-05-26',
    '2019-05-27',
    '2019-05-28',
    '2019-05-29',
    '2019-06-06',
    '2019-06-07',
    '2019-06-08',
    '2019-06-09',
    '2019-06-10',
    '2019-06-11',
    '2019-06-12',
    '2019-06-13',
    '2019-06-14',
    '2019-06-15',
    '2019-06-16',
    '2019-06-17',
    '2019-06-18',
    '2019-06-19',
    '2019-06-20',
    '2019-06-21',
    '2019-06-22',
    '2019-06-23',
    '2019-06-24',
    '2019-06-25',
    '2019-06-26',
    '2019-06-27',
    '2019-06-28',
    '2019-06-29',
    '2019-06-30',
    '2019-07-01',
    '2019-07-02',
    '2019-07-03',
    '2019-07-04',
    '2019-07-05',
    '2019-07-06',
    '2019-07-07',
    '2019-07-08',
    '2019-07-09',
    '2019-07-10',
    '2019-07-11',
    '2019-07-12',
    '2019-07-13',
    '2019-07-14',
    '2019-07-15',
    '2019-07-16',
    '2019-07-17',
    '2019-07-18',
    '2019-07-19',
    '2019-07-20',
    '2019-07-21',
    '2019-07-22',
    '2019-07-23',
    '2019-07-24',
    '2019-07-25',
    '2019-07-26',
    '2019-07-27',
    '2019-07-28',
    '2019-07-29',
    '2019-07-30',
    '2019-07-31',
    '2019-08-01',
    '2019-08-02',
    '2019-08-03',
    '2019-08-04',
    '2019-08-05',
    '2019-08-06',
    '2019-08-07',
    '2019-08-08',
    '2019-08-09',
    '2019-08-10',
    '2019-08-11',
    '2019-08-12',
    '2019-08-13',
    '2019-08-14',
    '2019-08-15',
    '2019-08-16',
    '2019-08-17',
    '2019-08-18',
    '2019-08-19',
    '2019-08-20',
    '2019-08-21',
    '2019-08-22',
    '2019-08-23',
    '2019-08-24',
    '2019-08-25',
    '2019-08-26',
    '2019-08-27',
    '2019-08-28',
    '2019-08-29',
    '2019-08-30',
    '2019-08-31',
    '2019-09-01',
    '2019-09-02',
    '2019-09-03',
    '2019-09-04',
    '2019-09-05',
    '2019-09-06',
    '2019-09-07',
    '2019-09-08',
    '2019-09-09',
    '2019-09-10',
    '2019-09-11',
    '2019-09-12',
    '2019-09-13',
    '2019-09-14',
    '2019-09-15',
    '2019-09-16',
    '2019-09-17',
    '2019-09-18',
    '2019-09-19',
    '2019-09-20',
    '2019-09-21',
    '2019-09-22',
    '2019-09-23',
    '2019-09-24',
    '2019-09-25',
    '2019-09-26',
    '2019-09-27',
    '2019-09-28',
    '2019-09-29',
    '2019-09-30',
    '2019-10-01',
    '2019-10-02',
    '2019-10-03',
    '2019-10-04',
    '2019-10-05',
    '2019-10-06',
    '2019-10-07',
    '2019-10-08',
    '2019-10-09',
    '2019-10-10',
    '2019-10-11',
    '2019-10-12',
    '2019-10-13',
    '2019-10-14',
    '2019-10-15',
    '2019-10-16',
    '2019-10-17',
    '2019-10-18',
    '2019-10-19',
    '2019-10-20',
    '2019-10-21',
    '2019-10-22',
    '2019-10-23',
    '2019-10-24',
    '2019-10-25',
    '2019-10-26',
    '2019-10-27',
    '2019-10-28',
    '2019-10-29',
    '2019-10-30',
    '2019-10-31',
    '2019-11-01',
    '2019-11-02',
    '2019-11-03',
    '2019-11-04',
    '2019-11-05',
    '2019-11-06',
    '2019-11-07',
    '2019-11-08',
    '2019-11-09',
    '2019-11-10',
    '2019-11-11',
    '2019-11-12',
    '2019-11-13',
    '2019-11-14',
    '2019-11-15',
    '2019-11-16',
    '2019-11-17',
    '2019-11-18',
    '2019-11-19',
    '2019-11-20',
    '2019-11-21',
    '2019-11-22',
    '2019-11-23',
    '2019-11-24',
    '2019-11-25',
    '2019-11-26',
    '2019-11-27',
    '2019-11-28',
    '2019-11-29',
    '2019-11-30',
    '2019-12-01',
    '2019-12-02',
    '2019-12-03',
    '2019-12-04',
    '2019-12-05',
    '2019-12-06',
    '2019-12-07',
    '2019-12-08',
    '2019-12-09',
    '2019-12-10',
    '2019-12-11',
    '2019-12-12',
    '2019-12-13',
    '2019-12-14',
    '2019-12-15',
    '2019-12-16',
    '2019-12-17',
    '2019-12-18',
    '2019-12-19',
    '2019-12-20',
    '2019-12-21',
    '2019-12-22',
    '2019-12-23',
    '2019-12-24',
    '2019-12-25',
    '2019-12-26',
    '2019-12-27',
    '2019-12-28',
    '2019-12-29',
    '2019-12-30',
    '2019-12-31',
    '2020-01-01',
    '2020-01-02',
    '2020-01-03',
    '2020-01-04',
    '2020-01-05',
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-11',
    '2020-01-12',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
    '2020-01-16',
    '2020-01-17',
    '2020-01-18',
    '2020-01-19',
    '2020-01-20',
    '2020-01-21',
    '2020-01-22',
    '2020-01-23',
    '2020-01-24',
    '2020-01-25',
    '2020-01-26',
    '2020-01-27',
    '2020-01-28',
    '2020-01-29',
    '2020-01-30',
    '2020-01-31',
    '2020-02-01',
    '2020-02-02',
    '2020-02-03',
    '2020-02-04',
    '2020-02-05',
    '2020-02-06',
    '2020-02-07',
    '2020-02-08',
    '2020-02-09',
    '2020-02-10',
    '2020-02-11',
    '2020-02-12',
    '2020-02-13',
    '2020-02-14',
    '2020-02-15',
    '2020-02-16',
    '2020-02-17',
    '2020-02-18',
    '2020-02-19',
    '2020-02-20',
    '2020-02-21',
    '2020-02-22',
    '2020-02-23',
    '2020-02-24',
    '2020-02-25',
    '2020-02-26',
    '2020-02-27',
    '2020-02-28',
    '2020-02-29',
    '2020-03-01',
    '2020-03-02',
    '2020-03-03',
    '2020-03-04',
    '2020-03-05',
    '2020-03-06',
    '2020-03-07',
    '2020-03-08',
    '2020-03-09',
    '2020-03-10',
    '2020-03-11',
    '2020-03-12',
    '2020-03-13',
    '2020-03-14',
    '2020-03-15',
    '2020-03-16',
    '2020-03-17',
    '2020-03-18',
    '2020-03-19',
    '2020-03-20',
    '2020-03-21',
    '2020-03-22',
    '2020-03-23',
    '2020-03-24',
    '2020-03-25',
    '2020-03-26',
    '2020-03-27',
    '2020-03-28',
    '2020-03-29',
    '2020-03-30',
    '2020-03-31',
    '2020-04-01',
    '2020-04-02',
    '2020-04-03',
    '2020-04-04',
    '2020-04-05',
    '2020-04-06',
    '2020-04-07',
    '2020-04-08',
    '2020-04-09',
    '2020-04-10',
    '2020-04-11',
    '2020-04-12',
    '2020-04-13',
    '2020-04-14',
    '2020-04-15',
    '2020-04-16',
    '2020-04-17',
    '2020-04-18',
    '2020-04-19',
    '2020-04-20',
    '2020-04-21',
    '2020-04-22',
    '2020-04-23',
    '2020-04-24',
    '2020-04-25',
    '2020-04-26',
    '2020-04-27',
    '2020-04-28',
    '2020-04-29',
    '2020-04-30',
    '2020-05-01',
    '2020-05-02',
    '2020-05-03',
    '2020-05-04',
    '2020-05-05',
    '2020-05-06',
    '2020-05-07',
    '2020-05-08',
    '2020-05-09',
    '2020-05-10',
    '2020-05-11',
    '2020-05-12',
    '2020-05-13',
    '2020-05-14',
    '2020-05-15',
    '2020-05-16',
    '2020-05-17',
    '2020-05-18',
    '2020-05-19',
    '2020-05-20',
    '2020-05-21',
    '2020-05-22',
    '2020-05-23',
    '2020-05-24',
    '2020-05-25',
    '2020-05-26',
    '2020-05-27',
    '2020-05-28',
    '2020-05-29',
    '2020-05-30',
    '2020-05-31',
    '2020-06-01',
    '2020-06-02',
    '2020-06-03',
    '2020-06-04',
    '2020-06-05',
    '2020-06-06',
    '2020-06-07',
    '2020-06-08',
    '2020-06-09',
    '2020-06-10',
    '2020-06-11',
    '2020-06-12',
    '2020-06-13',
    '2020-06-14',
    '2020-06-15',
    '2020-06-16',
    '2020-06-17',
    '2020-06-18',
    '2020-06-19',
    '2020-06-20',
    '2020-06-21',
    '2020-06-22',
    '2020-06-23',
    '2020-06-24',
    '2020-06-25',
    '2020-06-26',
    '2020-06-27',
    '2020-06-28',
    '2020-06-29',
    '2020-06-30',
    '2020-07-01',
    '2020-07-02',
    '2020-07-03',
    '2020-07-04',
    '2020-07-05',
    '2020-07-06',
    '2020-07-07',
    '2020-07-08',
    '2020-07-09',
    '2020-07-10',
    '2020-07-11',
    '2020-07-12',
    '2020-07-13',
    '2020-07-14',
    '2020-07-15',
    '2020-07-16',
    '2020-07-17',
    '2020-07-18',
    '2020-07-19',
    '2020-07-20',
    '2020-07-21',
    '2020-07-22',
    '2020-07-23',
    '2020-07-24',
    '2020-07-25',
    '2020-07-26',
    '2020-07-27',
    '2020-07-28',
    '2020-07-29',
    '2020-07-30',
    '2020-07-31',
    '2020-08-01',
    '2020-08-02',
    '2020-08-03',
    '2020-08-04',
    '2020-08-05',
    '2020-08-06',
    '2020-08-07',
    '2020-08-08',
    '2020-08-09',
    '2020-08-10',
    '2020-08-11',
    '2020-08-12',
    '2020-08-13',
    '2020-08-14',
    '2020-08-15',
    '2020-08-16',
    '2020-08-17',
    '2020-08-18',
    '2020-08-19',
    '2020-08-20',
    '2020-08-21',
    '2020-08-22',
    '2020-08-23',
    '2020-08-24',
    '2020-08-25',
    '2020-08-26',
    '2020-08-27',
    '2020-08-28',
    '2020-08-29',
    '2020-08-30',
    '2020-08-31',
    '2020-09-01',
    '2020-09-02',
    '2020-09-03',
    '2020-09-04',
    '2020-09-05',
    '2020-09-06',
    '2020-09-07',
    '2020-09-08',
    '2020-09-09',
    '2020-09-10',
    '2020-09-11',
    '2020-09-12',
    '2020-09-13',
    '2020-09-14',
    '2020-09-15',
    '2020-09-16',
    '2020-09-17',
    '2020-09-18',
    '2020-09-19',
    '2020-09-20',
    '2020-09-21',
    '2020-09-22',
    '2020-09-23',
    '2020-09-24',
    '2020-09-25',
    '2020-09-26',
    '2020-09-27',
    '2020-09-28',
    '2020-09-29',
    '2020-09-30',
    '2020-10-01',
    '2020-10-02',
    '2020-10-03',
    '2020-10-04',
    '2020-10-05',
    '2020-10-06',
    '2020-10-07',
    '2020-10-08',
    '2020-10-09',
    '2020-10-10',
    '2020-10-11',
    '2020-10-12',
    '2020-10-13',
    '2020-10-14',
    '2020-10-15',
    '2020-10-16',
    '2020-10-17',
    '2020-10-18',
    '2020-10-19',
    '2020-10-20',
    '2020-10-21',
    '2020-10-22',
    '2020-10-23',
    '2020-10-24',
    '2020-10-25',
    '2020-10-26',
    '2020-10-27',
    '2020-10-28',
    '2020-10-29',
    '2020-10-30',
    '2020-10-31',
    '2020-11-01',
    '2020-11-02',
    '2020-11-03',
    '2020-11-04',
    '2020-11-05',
    '2020-11-06',
    '2020-11-07',
    '2020-11-08',
    '2020-11-09',
    '2020-11-10',
    '2020-11-11',
    '2020-11-12',
    '2020-11-13',
    '2020-11-14',
    '2020-11-15',
    '2020-11-16',
    '2020-11-17',
    '2020-11-18',
    '2020-11-19',
    '2020-11-20',
    '2020-11-21',
    '2020-11-22',
    '2020-11-23',
    '2020-11-24',
    '2020-11-25',
    '2020-11-26',
    '2020-11-27',
    '2020-11-28',
    '2020-11-29',
    '2020-11-30',
    '2020-12-01',
    '2020-12-02',
    '2020-12-03',
    '2020-12-04',
    '2020-12-05',
    '2020-12-06',
    '2020-12-07',
    '2020-12-08',
    '2020-12-09',
    '2020-12-10',
    '2020-12-11',
    '2020-12-12',
    '2020-12-13',
    '2020-12-14',
    '2020-12-15',
    '2020-12-16',
    '2020-12-17',
    '2020-12-18',
    '2020-12-19',
    '2020-12-20',
    '2020-12-21',
    '2020-12-22',
    '2020-12-23',
    '2020-12-24',
    '2020-12-25',
    '2020-12-26',
    '2020-12-27',
    '2020-12-28',
    '2020-12-29',
    '2020-12-30',
    '2020-12-31']

if __name__ == '__main__':
    for i in date:
        url = 'http://api.bilibili.com/x/v2/dm/history?type=1&oid={}&date=%s'.format(cid) % i
        r = requests.get(url, headers=header)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)
        with open('E:/Output/curriculudesign/{}.xml'.format(i), 'w', encoding='utf-8') as f:
            f.write(str(soup))
            f.close()

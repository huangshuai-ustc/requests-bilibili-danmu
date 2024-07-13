#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# 创建时间：2020-12-30 19:45
# 文件名称：画.py
from 程序.test import __1, __1s, __2, __2s
from scipy.interpolate import make_interp_spline
import numpy as np
from matplotlib import pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# # 1.
# x = np.array(__1)
# y = np.array(__1s)
# x1_new = np.linspace(0, 1550, 10000)
# x1 = [0]*10000
# y1_smooth = make_interp_spline(x, y)(x1_new)
# plt.plot(x1_new, y1_smooth, c='r')
# plt.fill_between(x1_new, y1_smooth, x1, facecolor='cyan', alpha=1)  # 填充最大最小值区间的范围，facecolor颜色，alpha色度深浅
# plt.title("本集弹幕相对时间的分布")
# plt.grid()  # 生成网格
# plt.style.use('ggplot')
# plt.show()
# 2.
colors = ['gray', 'pink', 'purple', 'red', 'green', 'blue', 'yellow', 'orange']
explode = [0.05, 0, 0, 0, 0, 0, 0, 0]
plt.pie(__2s, labels=__2, colors=colors,
        labeldistance=1.2,
        autopct='%.2f%%',
        startangle=90,
        radius=0.5,
        center=(0, 0),
        textprops={'fontsize': 12, 'color': 'k'},
        pctdistance=0.6,
        frame=1,
        explode=explode)
plt.axis('equal')
plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0.8))
plt.title("弹幕颜色及其占比\n\n")
plt.grid()
# plt.set_facecolor('blueviolet')
plt.show()
# text = open("E:/Output/first_results/list.txt", 'r', encoding='utf-8').read()
# result = "\n".join(jieba.cut(text))
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
# wc = WordCloud(
#     font_path="C:/Users/MisakaMikoto/AppData/Local/Microsoft/Windows/Fonts/汉仪时光体W.ttf",
#     background_color='white', width=1000, height=1000,
#     max_font_size=100, min_font_size=10,
#     mode='RGBA', colormap='Reds', mask=np.array(Image.open("E:/Users/MisakaMikoto/Desktop/37601598.png")),
#     color_func=ImageColorGenerator(np.array(Image.open("E:/Users/MisakaMikoto/Desktop/37601598.png")))
# ).generate(text.lower())
# wc.generate(result)
# # wc.to_file(r"E:/Output/{}.png".format(file_name))
# # plt.figure("{}".format(file_name))
# plt.imshow(wc)
# plt.axis("off")
# plt.show()

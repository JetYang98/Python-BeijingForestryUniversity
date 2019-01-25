# 根据图形形成词云
# 图形背景是白色的

import jieba
import wordcloud
from scipy.misc import imread

mask = imread('china.jpg')
with open('gaige.txt') as f:
	t = f.read()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='msyh.ttc',mask=mask,\
	width = 1000,height=700,background_color='white')
w.generate(txt)
w.to_file('Output.jpg')
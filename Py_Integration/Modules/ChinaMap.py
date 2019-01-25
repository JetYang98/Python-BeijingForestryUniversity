# 根据图形形成词云
# 图形背景是白色的

import jieba
import wordcloud
from scipy.misc import imread

class ChinaMap:
	'''
	制作词云
	'''
	def text(self):
		'''
		从文件中获得文本
		'''
		f = open('Resources/gaige.txt')
		t = f.read()
		f.close()
		ls = jieba.lcut(t)
		self.txt = ' '.join(ls)
	def word(self):
		'''
		生成词云图片
		'''
		mask = imread('Resources/china.jpg')
		w = wordcloud.WordCloud(font_path='msyh.ttc',mask=mask,\
			width = 1000,height=700,background_color='white')
		w.generate(self.txt)
		w.to_file('Output/Output.jpg')
# 自动安装第三方库

import os

libs = ['jieba', 'pyinstaller', 'wordcloud', 'TensorFlow']
try:
	for lib in libs:
		os.system('pip install ' + lib)
	print('Successful')
except:
	print('Failed Somehow')
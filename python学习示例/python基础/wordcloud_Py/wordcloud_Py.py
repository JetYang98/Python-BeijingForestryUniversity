# 词云库的使用

import jieba
import wordcloud

txt = 'Python具有丰富和强大的库。它常被昵称为胶水语言，\
能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。\
常见的一种应用情形是，使用Python快速生成程序的原型\
（有时甚至是程序的最终界面），然后对其中有特别要求的部分，\
用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，\
就可以用C/C++重写，而后封装为Python可以调用的扩展类库。\
需要注意的是在您使用扩展类库时可能需要考虑平台问题，\
某些可能不提供跨平台的实现。'
w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',height=700,max_words=15)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file('pywcloud.png')
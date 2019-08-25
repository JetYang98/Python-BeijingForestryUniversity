# jieba库是中文分词库

import jieba

a = open("threekingdoms.txt","r",encoding="utf-8")
txt = a.read()
a.close()
excludes = {"将军","却说","荆州","二人","不可","不能","如此",'商议','如何','主公','军士','左右','军马','引兵'}
words = jieba.lcut(txt)
counts = {}
for word in words:
	if len(word) == 1:
		continue
	elif word == '诸葛亮' or word == '孔明曰':
		rword = '孔明'
	elif word == '关公' or word == '云长':
		rword = '关羽'
	elif word == '玄德' or word == '玄德曰':
		rword = '刘备'
	elif word == '孟德' or word == '丞相':
		rword = '曹操'
	else:
		rword = word
	counts[rword] = counts.get(rword,0) + 1
for word in excludes:
	del counts[word]
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
print(type(counts.items()))
# print(counts.items())
print(type(items))
# print(items)
for i in range(10):
	word,count = items[i]
	print("{0:<10}{1:>5}".format(word,count))

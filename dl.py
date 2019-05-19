import sys
import os
import jieba

sent = '在包含问题的所有解的空间书中，按照深度优先搜索的策略，从根节点出发深度'
wordlist = jieba.cut(sent,cut_all=True)
w2 = [wordlist]
print(' '.join(wordlist))
print(w2)
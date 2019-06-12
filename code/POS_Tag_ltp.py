# -*- coding: utf-8 -*-
"""
使用Ltp3.4进行中文分词词性标注

"""
import os
from pyltp import Postagger

# ltp模型目录的路径
LTP_DATA_DIR = 'D:\ltp_data_v3.4.0\ltp_data_v3.4.0' 
# 词性标注模型路径，模型名称为`pos.model` 
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  
# 初始化实例
posttagger = Postagger()
# 加载词性标注模型
posttagger.load(pos_model_path)
# 分词结果
words = ['元芳', '你', '怎么', '看']
# 词性标注
postags = posttagger.postag(words)
# Ltp的词性标注遵从国标863词性标注集
for word,postag in zip(words,postags):
    print(word+"/"+postag)
# 释放模型
posttagger.release()  
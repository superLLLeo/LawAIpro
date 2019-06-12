# -*- coding: utf-8 -*-
"""
使用Ltp3.4进行中文命名实体识别

"""
import os
from pyltp import NamedEntityRecognizer

# ltp模型目录的路径
LTP_DATA_DIR = 'D:\ltp_data_v3.4.0\ltp_data_v3.4.0' 
# 命名实体识别模型路径，模型名称为`ner.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  
# 初始化实例
recognizer = NamedEntityRecognizer() 
# 加载模型
recognizer.load(ner_model_path)
# 分词结果
words = ['元芳', '你', '怎么', '看']
# 词性标注结果
postags = ['nh', 'r', 'r', 'v']
# 命名实体识别
netags = recognizer.recognize(words, postags)
# 释放模型
print ('\t'.join(netags))
recognizer.release() 
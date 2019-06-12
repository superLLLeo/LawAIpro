# -*- coding: utf-8 -*-
"""
使用Ltp3.4进行中文分词,词性标注和命名实体识别

"""

import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer


# ltp模型目录的路径  
LTP_DATA_DIR = 'D:\ltp_data_v3.4.0\ltp_data_v3.4.0'  
# 分词模型路径，模型名称为cws.model；词性标注模型路径，模型名称为`pos.model`；命名实体识别模型路径，模型名称为`ner.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')    
# 实例化分词模块
segmentor = Segmentor()
# 加载分词库
segmentor.load(cws_model_path)
# 打开文件进行分词
with open('doc_new.txt',"r",encoding="utf-8") as govdoc_file:
    for i in range(1000):
        gov_onetext = govdoc_file.readline()
        # 分词 words的返回值类型是VectorOfString类型
        words = segmentor.segment(gov_onetext)
        words_seg = " ".join(words)
        # 初始化词性标注实例
        posttagger = Postagger()
        # 加载词性标注模型
        posttagger.load(pos_model_path)
        # 词性标注
        postags = posttagger.postag(words)
        # 初始化命名实体识别实例
        recognizer = NamedEntityRecognizer() 
        # 加载命名实体识别模型
        recognizer.load(ner_model_path)
        # 命名实体识别 
        netags = recognizer.recognize(words, postags)
        # 将分词结果写入新文件doc_seg.txt
        with open('doc_seg.txt',"a",encoding="utf-8") as govdoc_file_seg:
            for word,postag,netag in zip(words,postags,netags):
                govdoc_file_seg.write(word + "/" + postag + "//命名实体识别" + netag)
            govdoc_file_seg.write("\n")

# 释放模型
segmentor.release()
posttagger.release()  
recognizer.release() 
print("分词和词性标注结束")

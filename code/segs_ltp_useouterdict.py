# -*- coding: utf-8 -*-
"""
使用Ltp3.4进行中文分词,添加使用分词外部词典

"""
import os
from pyltp import Segmentor

# ltp模型目录的路径 # 
LTP_DATA_DIR = 'D:\ltp_data_v3.4.0\ltp_data_v3.4.0'  
# 分词模型路径，模型名称为cws.model
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  
# 实例化分词模块
segmentor = Segmentor()
# 加载模型，第二个参数是外部词典文件路径
segmentor.load_with_lexicon(cws_model_path, 'D:\doc_nlp\mydict.txt') 
# 打开文件进行分词
with open('doc_new.txt',"r",encoding="utf-8") as govdoc_file:
    for i in range(1):
        gov_onetext = govdoc_file.readline()
        # 分词 words的返回值类型是VectorOfString类型
        words = segmentor.segment(gov_onetext)
        words_seg = "|".join(words)
        # 将分词结果写入新文件doc_seg_useouterdict.txt'
        with open('doc_seg_useouterdict.txt',"a",encoding="utf-8") as govdoc_file_seg:
            govdoc_file_seg.write(words_seg+"\n\n")
# 释放模型
segmentor.release()
print("分词结束")

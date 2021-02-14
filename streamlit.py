import streamlit as st
import pandas as pd
import openpyxl
import sys
import random 
from PIL import Image

data=pd.read_excel(r'E:\Python\python_code\KnowledgeMeme\data\all_data.xlsx')
all_sao=pd.read_excel(r'E:\Python\python_code\KnowledgeMeme\data\sao_corpus(mark).xlsx')
#分离函数
def clean(text) :
    # if not text is None :
        sp=text.split('$')
        list1=[]
        for i in range(0,len(sp)):
            if len(sp) > 0 :
                list1.append(sp[i])
        # print(list1)
        list2=[]
        for i in list1 :
            gjc1 = [i.split("#")]
            for j in gjc1 :
                # print(j)
                list2.append(j)
        list3=[]
        list3 = [i for i in list2 if i !=['']]
    # else :
        # text = None
        
        return list3

#抽取函数
def sao_extraction():
    extractor = TripleExtractor()
    svos = extractor.triples_main(b)
    return svos

#随机抽取的SAO
sample_sao=[all_sao.iloc[random.randint(0,len(all_sao.columns))][0],all_sao.iloc[random.randint(0,len(all_sao.columns))][1],all_sao.iloc[random.randint(0,len(all_sao.columns))][2]]

#研究方法和研究对象          
method=[]
obj1=[]
obj2=[]

st.title('基于知识基因的自动综述系统')
st.markdown("---")
title = st.text_input('请输入文本')

# st.button('提交')
for i in range(len(data)) :
    if data.iloc[i][1]==title : #如果输入文本在题名中
        st.success('所在文献：{}\n作者：{}\n被引次数:{}'.format(data.iloc[i][1],data.iloc[i][2],data.iloc[i][19]))
        try :       #如果SAO不为空
            for k in clean(str(data.iloc[i][23])) :
                method.append(k[1]) #A作为研究方法
                obj1.append(k[0])   #S和O作为研究对象
                obj2.append(k[2])
                obj=obj1+obj2
            st.success('研究对象：{}\n研究方法：{}'.format(obj,method))
        except IndexError :
            st.error("Error: SAO为空")
        break
    else :
        st.write('///')
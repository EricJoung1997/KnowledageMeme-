import pandas as pd
import openpyxl
import sys
import random 
# sys.path.append('E:\Python\python_code\KnowledgeMeme\Extraction\triple_extraction.py')
from  Extraction.triple_extraction import *  

data=pd.read_excel(r'E:\Python\python_code\KnowledgeMeme\data\all_data.xlsx')
all_sao=pd.read_excel(r'E:\Python\python_code\KnowledgeMeme\data\sao_corpus(mark).xlsx')
b=input("请输入文本:")

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
for i in range(len(data)) :
    if data.iloc[i][1]==b or data.iloc[i][6]==b : #如果输入文本在题名中
        print('相关文献：{}\n作者：{}\n被引次数:{}'.format(data.iloc[i][1],data.iloc[i][2],data.iloc[i][19]))
        try :       #如果SAO不为空
            for k in clean(str(data.iloc[i][23])) :
                method.append(k[1]) #A作为研究方法
                obj1.append(k[0])   #S和O作为研究对象
                obj2.append(k[2])
                obj=obj1+obj2
            print('研究对象：{}\n研究方法：{}'.format(obj,method))
            if data.iloc[i][26] != '[]' : #如果知识基因不为空
                print('知识基因：{}'.format(data.iloc[i][26]))

                print('可能感兴趣的知识基因：{}'.format(data.iloc[i][28]))
                break
            else : #如果没有知识基因就推荐引文知识基因和随机产生的知识基因
                print('该文没有知识基因。\n可能感兴趣的知识基因：{},{}'.format(data.iloc[i][28],sample_sao))
            # print('可能感兴趣的知识基因：{}'.format(data.iloc[i][28]))
        except IndexError :
            print ("Error: SAO为空")
        break   

else :      #如果输入文本不在题名中
        sao=sao_extraction()
        # print('包含的SAO有：{}'.format(sao)) #抽取SAO，判别研究方法/对象、知识基因
        if sao !=  []:
            for i in sao :
                print('研究方法：',i[0],i[2])
                print('研究对象：',i[1])
                break
        else:
            print('*{}*无法构成知识基因'.format(b))
            print('可能感兴趣的知识基因有：{}'.format(sample_sao))  #直接随机抽
            
import pandas as pd
import random 
from textrank import *

#定义行为
action=['提出','指出','阐述','认为','研究了','介绍','探讨了','论述了','分析','探究','表述']

#按年排列，输出综述
def n_year(n,c,target_data) :#n是哪一年，c为0表示摘要策略，为1表示知识基因策略，target_data是要匹配的数据
    print('在{}年：'.format(n))
    labeln = pd.DataFrame(columns=target_data.columns)
    labeln=target_data[target_data.年==n]
    for i in range(len(labeln)) :
        if c==0 :
            print('{}{}{}'.format(labeln['作者'].iloc[i]," ".join(random.sample(action,1))," ".join([each for each in summarize(labeln['摘要'].iloc[i],1)])))
        if c==1 :
            print('{}{}{}'.format(labeln['作者'].iloc[i]," ".join(random.sample(action,1)),labeln['abstractKM'].iloc[i]))


def time_summary(year,k,year_data):
    for i in year :
        # print('---------------')
        n_year(i,k,year_data)#调用n_year，遍历推荐出来的所有年份，k同c,year_data同target_data



# print('?')
# text='''文章认为嵌入用户环境是学科服务中的关键问题,分析了嵌入用户环境的学科服务的背景和特点,并就嵌入教学与学习、嵌入学术交流与科学研究、嵌入临床工作的学科服务的服务内容,以及嵌入用户物理空间及嵌入用户虚拟空间的嵌入式学科服务服务模式展开了详细论述。
# # '''
# text=text.replace('\n', '')
# # summarys=summarize(text,1)
# print(" ".join([each for each in summarize(text,1)]))
# # for each in summarys:
# #     print (each)
# print()
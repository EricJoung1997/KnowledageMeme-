import pandas as pd

data=pd.read_excel('E:\Python\python_code\KnowledgeMeme\data\generateddata\YY.xlsx')

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

# 分离
for i in range(len(data)) :
    data['摘要知识基因'].iloc[i]=clean(str(data['摘要SAO'].iloc[i]))

# Su=['立场','该模型','读者决策采购']
Su=['图书馆','公共图书馆','数字图书馆', '企业','读者', '数据','大数据','大学图书馆','图书馆员','情报学',
'数字','图书馆服务','国家图书馆','图书馆联盟','图书馆学', '图书馆界','元数据','古籍','关联数据','机构知识库',
'文本','竞争情报','文摘','21世纪','文献','美国图书馆','搜索引擎','Web2.0','清华大学图书馆','电子资源',
'个性化服务', '专利','图书馆事业','藏书','个性化信息服务','社区图书馆','手机图书馆','北京大学图书馆','计算机',
'理事会','聚类','知识图谱''图书馆精神', '电子政务','博客','电子阅览室','数字化','处理','图书馆资源', 
'上海交通大学图书馆', '数字鸿沟','咨询服务','知识库','叙词表', '链接','数据库','分类法','区域','图书馆核心价值',
'广州大学图书馆','实时','数字馆藏','评价指标','图书馆网站','纸质文献','识别','数据挖掘','公共服务','上海图书馆',
'出版','杭州图书馆','书刊','同济大学图书馆','深圳图书馆','数字资源','公共信息资源','馆藏','海南大学图书馆',
'关键词','读者服务','图书馆学研究','李国新','刘炜','读书会','满意度','热点','馆长','算法','农村图书馆','分类',
'企业信息化','电子期刊', '层次分析法','数据集']
# Ob=['多馆资源','研究出发点','读者决策概念']
Ob=['数据','图书馆','个性化服务', '情报学','大数据', '文献', '特色数据库','工具','热点','概述',
'个性化信息服务','数字图书馆','算法','数据库','竞争情报','差异','图书馆服务','读者','元数据','服务质量', 
'标准','搜索引擎','归纳','对比','检索','公共图书馆','处理','聚类','咨询服务','知识图谱','期刊','关键词','类',
'数字鸿沟', '实体','范围','非物质文化遗产','收集','图书馆事业','数字资源','词','标志','关联数据', 
'版权','图书馆协会','特色馆藏','阅读活动','电子资源','国家图书馆','分类法','层次分析法','识别','分类','范式', 
'图书馆核心价值','图书馆工作', '软件', '读者需求', '标准化', '解释', '公共服务', '路径', '服务器', '情感分析']

def HighFrequencyWords(list1) :
    for k in list1[:] :
            if (k[0] not in Su and k[2] not in Ob) :
                list1.remove(k)
    return list1

# 高频词
for i in range(len(data)) :
    if data['摘要知识基因'].iloc[i] != [['nan']] :
        data['摘要知识基因'].iloc[i]=HighFrequencyWords(data['摘要知识基因'].iloc[i])

f = open("E:\Python\python_code\KnowledgeMeme\dictionary\Dir.txt", encoding='utf8')
Dir=f.read().split("\n")    #Dir为词典

def NotInDir(list3) :
    for k in list3[:] :
            if (k[0] not in Dir and k[2] not in Dir) :
                list3.remove(k)
    return list3

# 遍历词典
for i in range(len(data)) :
    if data['摘要知识基因'].iloc[i] != [['nan']] :
        data['摘要知识基因'].iloc[i]=NotInDir(data['摘要知识基因'].iloc[i])


print('finished!')
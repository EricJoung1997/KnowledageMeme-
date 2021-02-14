import gensim,time
from gensim import corpora, models, similarities
from gensim.models import LdaModel
# TaggededDocument = gensim.models.doc2vec.TaggedDocument

def genlda(textlist,n):
    # ticks = str(time.time()).replace('.','')[-6:-1]
    nn=str(n)
    dictionary = corpora.Dictionary(textlist)
    corpus = [ dictionary.doc2bow(text) for text in textlist ]

    lda =models.LdaMulticore(corpus=corpus, id2word=dictionary, num_topics=n,passes=100,workers=3) 
    doc_topic = [a for a in lda[corpus]]

    topics_r = lda.print_topics(num_topics = n, num_words =20)
    k=0
    LDAlabel=[]
    for i in lda.get_document_topics(corpus)[:]:
        listj=[]
        for j in i:
            listj.append(j[1])
        bz=listj.index(max(listj))
        iiilabel=k,i[bz][0],i[bz][1],listj,listj.index(max(listj))
        LDAlabel.append(iiilabel)
        k=k+1

    return LDAlabel

# if __name__ == '__main__':
#     a=[
#         ['20', '科技情报机构', '作者', '概述', '我国', '情报工作', '形势', '存在的问题'], 
#         ['联机检索系统' ,'科技情报中心' ,'处理程序' ,'标引人员' ,'科学技术情报' '日本', '科学技术情报'], 
#         ['百余种', '情报工作', '中起', '作用', '检索刊物', '质量', '文献', '搜集', '报道', '不全', '时差'], 
#         # ['两种 典型 模式 卽 分散型 集中型 苏联 集中型 代表 二十年代 列宁'], 
#         # ['关键技术问题 研讨会 983 年 月 中国科学技术情报学会 编译'], 
#         # ['面临的问题 作者 提出 省级 综合性 科技情报所 面临 功能 '], 
#         ['描述' ,'一种', '数据库计算机', '图书情报', '自动化', '方案']
#         ]
#     # for i in a:
#     #     for k in i :
#     #         k.split(' ')
    
#     print(genlda(a,2))
print('success...')
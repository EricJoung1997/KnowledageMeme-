#将引证文献进行格式化抽取
import sqlite3
conn = sqlite3.connect('KnowledgeGene/KGData/db(1).sqlite3')
#创建一个cursor：
cursor = conn.cursor()
#执行查询语句：
#cursor.execute("select cited_papers from paper_all where title like ?",('图书馆%',))
cursor.execute("select  DOI,参考文献 from LIS_PAPERS")
#使用featchall获得结果集（list）
values = cursor.fetchall()
#print(values)
#取出每篇文章中的被引文献
# print(len(values))
for i in range(len(values)):
# # for i in range(3):
#     #变量pa_p:文章doi+作者；pa_au:文章i的作者;pa_doi:文章的DOI号
    pa_p=values[i]
    pa_doi=pa_p[0]
    pa_citedpaper=pa_p[1]
    print('第',i,'篇文章的参考文献：',pa_citedpaper)
    if pa_citedpaper != None:
        com_count=pa_citedpaper.count('\n')
        print('第',i,'篇文章总共有',com_count,'个换行符')
        pa_citedpaper_1 = pa_citedpaper.split("\n")
        print(len(pa_citedpaper_1))
        for k in range(len(pa_citedpaper_1)):
            pa_citedpaper_2=pa_citedpaper_1[k]#第一行数据不要
            pa_citedpaper_3=pa_citedpaper_2.split(".")
            if len(pa_citedpaper_3) > 1:
                p_cited_author = ','.join(pa_citedpaper_3[0].split(']')[1:])
                print(p_cited_author)
                p_cited_title = ','.join(pa_citedpaper_3[1].split('[')[:1])
                print(p_cited_title)
                p_cited_type=','.join(pa_citedpaper_3[1].split('[')[1:])
                p_cited_type='['+p_cited_type
                print(p_cited_type)
                p_cited_source=','.join(pa_citedpaper_3[2].split(',')[:1])
                print(p_cited_source)
                p_cited_time=','.join(pa_citedpaper_3[2].split(',')[1:2])
                print(p_cited_time)

                sql = "INSERT INTO paper_referenced (doi,referenced_author,referenced_title,referenced_type,referenced_source,referenced_time) VALUES (?,?,?,?,?,?)"
                val = (pa_doi, p_cited_author, p_cited_title, p_cited_type,p_cited_source,p_cited_time)
                cursor.execute(sql, val)

conn.commit()
print("Records created successfully")
conn.close()

#bug1
# Traceback (most recent call last):
#   File "/home/zyj/桌面/python/KnowledgeGene/KG/reference_papers.py", line 35, in <module>
#     p_cited_source=','.join(pa_citedpaper_3[2].split(',')[:1])
# IndexError: list index out of range
#bug2
# 第 0 篇文章的参考文献： None
# Traceback (most recent call last):
#   File "/home/zyj/桌面/python/KnowledgeGene/KG/zyt_EventTriplesExtraction-master/referenced_papers.py", line 20, in <module>
#     com_count=pa_citedpaper.count('\n')
# AttributeError: 'NoneType' object has no attribute 'count'
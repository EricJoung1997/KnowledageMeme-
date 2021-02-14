from triple_extraction import *
import sqlite3

# content='李克强总理今天来我家了,我感到非常荣幸'
# extractor = TripleExtractor()
# svos = extractor.triples_main(content)
# print('svos', svos)
sqlitedata='KnowledgeMeme/data/KM.sqlite3'
'''提取引用文献三元组'''
def tripleCitedtosql():
    conn = sqlite3.connect(sqlitedata)
    cursor = conn.cursor()  
    cursor.execute("select * from paper_cited")
    values = cursor.fetchall()
    # print(values[1][5])
    extractor = TripleExtractor()
    for i in range(0,len(values)):
        contentt=values[i][2]
        # print(contentt)
        paperid=values[i][0]
        time=values[i][5]
        svos = extractor.triples_main(contentt)
        # print(svos)
        print(i)
        # print(contentt)
        # print(svos)
        saot=" "
        for sao in svos:
            sao_convert="#".join(sao)
            saot=saot+"$"+sao_convert
        print(saot)
        sql = "INSERT INTO paper_cited_TripleExtraction (doi,title,tripled,time) VALUES (?,?,?,?)"
        val = (paperid, contentt, saot, time)
        cursor.execute(sql, val)
    conn.commit()
    print("Records created successfully")
    conn.close()





'''提取参考文献三元组'''
def tripleReferencedtosql():
    conn = sqlite3.connect(sqlitedata)
    cursor = conn.cursor()  
    cursor.execute("select * from paper_referenced")
    Rvalues = cursor.fetchall()
    # print(values[1][5])
    extractor = TripleExtractor()
    for i in range(0,len(Rvalues)):
        contentt=Rvalues[i][2]
        # print(contentt)
        paperid=Rvalues[i][0]
        time=Rvalues[i][5]
        svos = extractor.triples_main(contentt)
        # print(svos)
        print(i)
        # print(contentt)
        # print(svos)
        saot=" "
        for sao in svos:
            sao_convert="#".join(sao)
            saot=saot+"$"+sao_convert
        print(saot)
        sql = "INSERT INTO paper_referenced_TripleExtraction (doi,Rtitle,Rtripled,Rtime) VALUES (?,?,?,?)"
        val = (paperid, contentt, saot, time)
        cursor.execute(sql, val)
    conn.commit()
    print("Records created successfully")
    conn.close()



# tripleCitedtosql()
# tripleReferencedtosql()
print('ok')
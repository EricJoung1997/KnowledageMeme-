import numpy as np


#余弦相似度计算函数
def cos_dist(sl1,sl2):#输入的是分好词的列表
    key_word = list(set(sl1 + sl2))## 列出所有的词,取并集
    word_vector1 = np.zeros(len(key_word))## 给定形状和类型的用0填充的矩阵存储向量
    word_vector2 = np.zeros(len(key_word))
    # 计算词频，依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(sl1)):
            if key_word[i] == sl1[j]:
                word_vector1[i] += 1
        for k in range(len(sl2)):
            if key_word[i] == sl2[k]:
                word_vector2[i] += 1
    dist=float(np.dot(word_vector1,word_vector2)/(np.linalg.norm(word_vector1)*np.linalg.norm(word_vector2)))
    return dist


# print(cos_dist(['信息素养'],['信息素养','高校建设','数字化校园']))
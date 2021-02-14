from triple_extraction import *
# import sqlite3
import pandas  as pd
from tqdm import tqdm

# print('?')
data=pd.read_excel('data\CQMdatas.xlsx')
data3=data.iloc[8000:]
# print(data['摘要'].head(5))
data3['SAO']=None

extractor = TripleExtractor()


for i in tqdm(range(len(data3))):
    data3['SAO'].iloc[i]=extractor.triples_main(str(data3['摘要'].iloc[i]))
    # print('第{}条SAO：{}'.format(i,data['SAO'].iloc[i]))

data3.to_excel('CQMdata_with_SAO9503.xlsx')


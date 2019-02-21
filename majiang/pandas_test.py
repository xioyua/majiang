import pandas as pd
import numpy as np

actions = ['1','2','3','4']

indexs = ['手牌', '牌堆']

colu =  indexs + actions
# indexes = pd.MultiIndex.from_product([['期中'],['语']])

# columns = ['tom','jack','rose']
# data = np.random.randint(0,150,size=(1,4))
# q_table = pd.DataFrame(data=data,index=indexes,columns=actions)

q_table = pd.DataFrame(columns=colu, dtype=np.float64)

q_table = q_table.append(pd.Series(['1', '1', 0, 0, 0, 0], index=colu, name='1,2'))

print(q_table)
print(q_table.loc['1,2',:])
#data = pd.Series(np.random.randn(10), index=[['x', 'x', 'x', 'x', 'x', 'x', 'y', 'y', 'y', 'y'], ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

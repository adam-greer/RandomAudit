import pandas as pd
import numpy as np
from pandas import ExcelWriter

df = pd.read_csv("C:\Scripts\Audit\incidents.csv", index_col=False) 
df = df[['Display ID']]
df = df.reindex(np.random.permutation(df.index))column_len = len(df)
ten_percent = int(.1 * column_len) # creates the 10% var
df.head(ten_percent) #outputs the results of the 10%      
df['results'] = df.head(ten_percent)
writer = pd.ExcelWriter('C:\\Scripts\\Audit\{} Results.xlsx'.format(pd.datetime.today().strftime('%Y-%m')))
df.to_excel(writer,'Sheet1',index=False)
writer.save()

import pandas as pd
import os

os.chdir('D:/Users/rsilva/Documents/Python Scripts/webscrap/projects/tripadvisor/')

df_1 = pd.read_csv('test_coord_final.csv', encoding='utf-8-sig')
print(df_1.shape)
df_2 = pd.read_csv('combined.csv', encoding='utf-8-sig')
print(df_2.shape)
df = pd.concat([df_1,df_2])
print(df.shape)

df = df.drop_duplicates()
print(df.shape)

df.to_csv('tripadvisor_restaurants_final.csv', encoding= 'utf-8-sig', index = False)
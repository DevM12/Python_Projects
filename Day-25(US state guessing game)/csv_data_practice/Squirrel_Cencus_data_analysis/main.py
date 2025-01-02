import pandas as pd

data=pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

f_col=[]
for d in data['Primary Fur Color']:
    if d not in f_col and pd.notna(d):
        f_col.append(d)
fur_color_counts_list = [int((data['Primary Fur Color'] == color).sum()) for color in f_col]
dic={'Fur Color':f_col,'Count':fur_color_counts_list}
df=pd.DataFrame(dic)
print(df)
# df.to_csv('fur_color_count.csv')
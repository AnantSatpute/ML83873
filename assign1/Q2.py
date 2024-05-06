import pandas as pd
def function():
 df = pd.read_csv('Advertising.csv')
 print(df.head())
 print(df.tail())
 print(df.columns)
 print(df.tail(3))
 df.info()
 print(df.dtypes)
 print(df.isna().sum())
 print(df.dropna(axis=1,inplace=True))
 df.drop(["radio"],axis=1,inplace=True)
 print(df.head(10))
 update = df['sales'] *0.10
 df['update_sales'] = update + df['sales']
 print(df)
 print(df.shape)

function()
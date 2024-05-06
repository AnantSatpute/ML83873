import pandas as pd
empid = [1,2,3,4,5,6,7,8,9,10]
names = ["anant","omkar","abhishek","rahul","yash","mayur","akash","tejas","sam","angad"]
emp_info = pd.Series(names,index = empid)
print(emp_info)
print(type(emp_info))
df = pd.DataFrame(emp_info)
print(df)
df1 = (emp_info.head())
print(df)
df2 = (emp_info.tail())
print(df)
df.to_csv('myrecord.csv')
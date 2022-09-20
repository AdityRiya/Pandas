# import pandas as pd
# iris=pd.read_csv('pdcsv.csv')
# print(iris.head())
import pandas as pd 
s1=pd.DataFrame({'Name':['adity','rabia','sharif','akib'],'roll':['34','01','27','22']})
print(s1.head(3))
print(s1.tail(3))
print(s1.shape)
print(s1.describe())
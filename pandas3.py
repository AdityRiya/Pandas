#basic Operation of python pandas
import pandas as pd 
s1=pd.Series([1,2,3,4,5,6,7,8,9])
#add 5 to each item
print(s1+5)
#s1+s2
s2=pd.Series([11,22,33,44,55,66,77,88,99])
print(s1+s2)
#s1-s2
print(s1-s2)
#s1%2
print(s1%2)
#s1*2
print(s1*2)
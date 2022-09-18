import pandas as pd
# default Indexing of pandas 
s1 = pd.Series([8,6,5,4,3])
print(s1)
print(type(s1))

#change indexing as I want
s2 = pd.Series([8,6,5,4,3],index=['a','b','c','d','e'])
print(s2)
print(type(s2))

#series with dictionary
s3=pd.Series({'a':10,'b':20,'c':30})
print(s3)
print(type(s3))


#sort and index as i wish
s4=pd.Series({'a':10,'b':20,'c':30},index=['c','b','a'])
print(s4)
print(type(s4))
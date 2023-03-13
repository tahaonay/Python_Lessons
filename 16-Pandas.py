#kaggle.com/datasets
#data.world

import pandas as pd
import numpy as np
import sqlite3
import random

# ---dosya okuma---
"""
db= pd.read_csv("Players.csv")
db = pd.read_excel("sample.xlsx")   #pip install xlrd

connection = sqlite3.connect("sample.db")
db = pd.read_sql_query("SELECT * FROM sudents",connection)

ilk10= db.head(10)
son10= db.tail(10)

print(len(db.index))  # toplam kaç kayıt

"""

# ---data oluşturma---
"""
numbers = [10,20,30,40,50]
letters = ["e","f","g","h","i","j"]
data1 = numbers + letters
scalar = 14


# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(data1)
# pandas_series = pd.Series(scalar,[1,3,5,6])
# pandas_series = pd.Series(numbers,["e","f","g","h","i"])
pandas_series = pd.Series(np.random.randint(10,100,10))

boyut = pandas_series.ndim
type = pandas_series.dtype
sekil = pandas_series.shape

opel2018 = pd.Series([20,30,45,15],["astra","corsa","mokka","insignia"])


#print(opel2018)
print(opel2018["insignia"])

#print(pandas_series[0])
"""
# ---DataFrame---
"""
seri1  = pd.Series([1,3,2,7])
seri2  = pd.Series([4,7,2,8])

data = dict(elmalar=seri1, armutlar=seri2)

df= pd.DataFrame(data)

print(df)
"""

# Seçme
"""
liste =[1,2,3,5,7,9]
ogrenci =[["ahmet",50],["ali",85],["mehmet",45],["şuayip",13]]
df = pd.DataFrame(ogrenci, columns=["Öğrenci","Not"],  index= range( 1 , len(ogrenci)+1 ))  #dtype=float
print(df)

# loc["row","column"]
result = df["Not"]        # sütün
result = df.loc[1]        # satır
result = df.loc[:,["Not","Öğrenci"]]  # Sütün
result = df.iloc[3]

result = df.loc[[1,3],"Not"]

print(result)

# Ekleme
df["sütün3"] = pd.Series([4,5,6,7],[1,2,3,4],dtype=int,)
print(df)

# silme
df.drop("sütün3",axis=1, inplace=True) #yukarıdan aşağıya sütün3'ü sil
print(df)   # inplace false olursa üzerinde değişiklik yapmaz, kopya oluşturur
"""

# gruplama
df= pd.DataFrame(personeller)
result = df.groupby("bölüm").groups
result = df.groupby("bölüm","polis").groups

semtler = df.groupby("semt")

for name, group in semtler:
    print(name)
    print(group)

result = df.groupby("bölüm").get_group("muhasebe")
result = df.groupby("bölüm")["maaş"].mean()

result = df.isnull()   # boş mu?
result = df.notnull()  # boş değil mi?



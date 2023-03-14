import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
x= [5,10,15,20,25]
y= [1,4,9,16,25]
y2= []
x2= range(10)
x3= np.linspace(0,2,100)
for i in x2:
    y2.append(i**2)


#plt.plot(x,y,"x-y")  
#plt.plot(x2,y2,"x-y")
plt.plot(x3,x3**2)

plt.xlabel("X EKSENİ")
plt.ylabel("Y EKSENİ")

plt.axis([0,2,0,5])  #eksen büyüklüğü
"""

df = pd.read_csv("Players.csv")
df = df.head(20)   # ilk 20 veri
df = df.drop(["Player"],axis=1)  #player sütününü ekleme
df.plot(subplots=True)        #

plt.show()
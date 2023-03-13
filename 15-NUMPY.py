import numpy as np

""" ----Basic----
# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])


py_multi =[[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)

print(py_multi)
print(np_multi)

print("Dizi  boyutu:",np_array.ndim)
print("Multi boyutu:",np_multi.ndim)

print(np_array.shape)
print(np_multi.shape)

"""

# dizi = np.array([1,3,5,7,9])

# dizi = np.arange(1,10)      # 1-10 arası eleman oluşturur
# dizi = np.arange(10,100,3)  # 10-100 arası , 3er artar

# dizi = np.zeros(10) # 10 tane 0 dizisi oluştutur
# dizi = np.ones(10)  # 10 tane 1 dizisi oluşturur

# dizi = np.linspace(0,100,5)  # 0-100 arası 5 parçalık dizi

# dizi = np.random.randint(0,10)   # 0 - 10 arası rastgele bir sayı
# dizi = np.random.randint(0,20,3) # 0 - 10 arası 3 tane sayı
# dizi = np.random.randn(20)       # pozitif negatif rastgele float 20 sayı
# dizi = np.random.rand(20)

""" satır-sütün toplamı
np_array = np.arange(50)
dizi = np_array.reshape(5,10)
print(dizi.sum(axis=1))   # satırların toplamı
print(dizi.sum(axis=0))   # sütünların toplamı
"""

#print(dizi)

numbers = np.array([0,5,10,15,20,25,50,75])

# numpy operations

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

#print(numbers1)
#print(numbers2)

toplam = numbers1 + numbers2
fark = numbers1 - numbers2
carpim = numbers1 * numbers2
carpim2 = numbers1 * 10

sinus = np.sin(numbers1)
log = np.log(numbers1)

# matrise dönüştürme
numbers1 = numbers1.reshape(2,3)
numbers2 = numbers2.reshape(2,3)

print(numbers1)
print(numbers2)

# matris birleştirme
"""
birlesik = np.vstack((numbers1,numbers2))
birlesiky= np.hstack((numbers1,numbers2))
print(birlesik)
print(birlesiky)
"""

# buyuk küçük kontrolu  tek tek kontrol eder
buyukmu = numbers1 >= 50
kucukmu = numbers2 <= 10 

kalan = numbers1 %2 == 0
tek = numbers1 %2 == 1
print(tek)
print(numbers1[tek])


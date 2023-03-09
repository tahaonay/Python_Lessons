# Yorum
"""
type()   tip


Operatörler
+ - * / 
** üs
%  mod
// tam bölme

"""

#  a= input("abcd...")   string

# str(a) to string 
# int(a) to integer

"""STRING"""

# \n          alt satır
# yazi[0]     index numarası   
# [0]  ilk
# [-1] son
# [3:7:2]  3'ten 7'ye 2şer karakter, [3:] , [:7]

# len(yazi)   uzunluk

# ---format---
# print("my name is {s} {n}".format(n=name,s=surname))

# ---ondalık kısım çıkarma---
# print("the result is {r:1.4}".format(r=result))
# print(f"my name is {name}{surname}")

# yazi.upper()
# yazi.lower()
# yazi.title()
# yazi.capitalize()
# yazi.strip()           baştaki boşluğu alır
# yazi.split(',')        stringi parçalar
# yazi. ''.join(yazi)    ekler
# yazi.find('')          bulunursa il harf indexi döner
# yazi.starthwith('')    bu değerler başlıyorsa true döner
# yazi.replace('ç','c') 
# yazi.center(100,'*')       100 karakterlik alan


"""Listeler"""
my_list = [1,2,3, True, 5.6, 'one']

len(my_list)

print(my_list[2])      #2.indexli elemanı yazdır

# list3 = list1 + list2    listeleri ekler
# list3 =[list1 , list2]   liste içi liste

del my_list[-1]

print(f"{my_list[0]} {my_list[1]}")

minimum = min(my_list)
maximum = max(my_list)

parcala =my_list[3:6]

my_list.append('53')    #sona ekleme
my_list.insert(3,53)    #3.yere 53 ü ekle

my_list.pop(-3)         # -3.index elemanı siler
my_list.remove(53)      #53 verisini siler

#my_list.sort()          # sıralar
my_list.reverse()       # ters sıralar
my_list.count('s')      # "s" ten kaç tane var


"""tuple"""    #liste içinde değişiklik yapmaz ekleme yapabilir

my_tuple = (1,'iki', 3, True)

"""dictionary"""
#   key - Value
#   3  ==>  üç

sehirler =["Ankara", "Eskisehir"]
plakalar =[6, 26]

plakalar2 = {"Ankara":6, "Eskisehir":26}

print(plakalar2["Ankara"])











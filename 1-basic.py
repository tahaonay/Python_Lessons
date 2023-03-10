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

users = {
    "kullanici1": {
        "age": 6,
        "roles": "admin",
        "phone":1234567
    },

    "kullanici2": 54321
}

print(users["kullanici1"]["age"])


"""operatörler"""
# x += 5
# x -= 5
# x *= 5
# x /= 5
# x //=5
# x **= z

# a == b    eşit mi True, False değer alır
# a != b   eşit değil
# a <= b   küçük eşit
# a >= b   büyük eşit
# a > b
# a < b 

# and
# or
# not(result)

"""

sayi = int(input("Bir sayi giriniz:"))

if(sayi>= 0 and sayi <= 100):
    
    print("0 ile 100 asasında", "sayi:",sayi)


else
    print("değil")

"""

"""is in"""    # is aynı adres mi in aynı değer var mı
x = y =[1,2,3]
z= [1,2,3]

# print(x is y) True   x ile y aynı adreste
# print(x is z) False  x ile z aynı adreste değil


"""if elif else"""

kosul = 1

if kosul==1 :
    print("kosul dogru")

elif kosul ==3:
    print("diger kosul")

else:
    print("kosul dogru degil")

"""for"""
liste = [1,2,3,4,5,6]
for i in liste:
    print(i)


d = {"k1":1, "k2":2, "k3":3}
for key, value in d.items():
    print(key, value)

"""while"""
x = 0

while(x<100):
    print(x)
    x+=1

print("son")

"""break"""      #döngüden çıkar
"""continue"""   #atlar ve bir sonraki döngüye gider


for i in range(2,10,2):  # 2 den 10 a 2şer 2şer
    print(i)

"""fonksiyon"""
def merhaba(name):
    print("Merhaba",name)

def karealma(a):
    return a**2

def toplama(a,b):
    return a+b

def add(*params):
    return sum(params)         #param liste tipi, for da kullanılabilir
"""lambda""" #geçici fonksiyon
sayilar= [1,2,3,4,5]
kare = lambda num: num**2

cevap = kare(5) 


"""global"""
x = 10
def test():
    global x
    x = 100
    print(x)
print(x)

# open()     açmak ve oluşturmak
# open(dosya_adi,dosya_erisme_modu)

# w - Write   yazma 
# a - Append  ekleme
# x - Create  oluşturma  zaten varsa hata verir
# r - Read    okuma      dosya yoksa hata verir
# r+ - Read and write. güncelleme yapmak için 
"---------------------------------------------"

""" write   eğer açiksa siler
file = open("newFile.txt","w",encoding="utf-8")    işlemi bir değişkene atamamız lazım
file.close()

print(a)

file= open("C:/users/H3X4/desktop/newFile.txt","r")

"""

""" append
file = open("C:/Users/H3X4/Desktop/Python Dersleri/newFile.txt","a",encoding="utf-8")
file.write("ilk satır\n")
file.close()
"""


"""  readline()
file = open("newFile.txt","r",encoding="utf-8")
# icerik= file.read(5)   #5 karakter oku
icerik2 = file.read()
print(icerik)
print(icerik2)
file.close()

file.readline()    #tek satır
liste = file.readlines()   #satırları liste yapar
print(liste[2])
"""

# file.tell()    # cursorun konumu
# file.seek(0)   # cursor en başa gider


""" update
with open("newFile.txt","r+",encoding="utf-8") as file:    # 50.yere ekler
    file.seek(50)
    file.write("\ndeneme")

with open("newFile.txt","r+",encoding="utf-8") as file:    # en başa ekler
    file.write("---basa ekle---\n")
"""

""" araya veri yazma
with open("newFile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(2,"\ntaha\n")
    file.seek(0)
    for i in list:
        file.write(i)
"""




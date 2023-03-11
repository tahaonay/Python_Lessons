import os
import datetime


komutlar = dir(os)
#print(komutlar)

# os.chdir("C:\\")
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# yer = os.getcwd()
# print(yer)
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")



icindekiler = os.listdir()
#print(icindekiler)


#.py uzantılı dosyalar
"""
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
"""


ozellikler = os.stat("8-datetime.py")
boyut = ozellikler.st_size

olusturulma = datetime.datetime.fromtimestamp(ozellikler.st_ctime)
son_erisim = datetime.datetime.fromtimestamp(ozellikler.st_atime)
degisme = datetime.datetime.fromtimestamp(ozellikler.st_mtime)


"""
print(ozellikler)
print(boyut)
print("olusturulma:  ",olusturulma)
print("son erisim:   ",son_erisim)
print("degistirilme: ",degisme
"""

# Dosya calıstırma
# os.system("notepad.exe")

# varmi = os.path.exists("C:/python")
# print(varmi)

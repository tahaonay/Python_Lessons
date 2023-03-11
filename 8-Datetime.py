from datetime import datetime 

zaman = datetime.now()
yil = zaman.year
ay = zaman.month
gün = zaman.day
saat = zaman.hour
dakika = zaman.minute
saat2 =zaman.time()
#print(zaman)
#print(yil)
#print(ay)
#print(gün)
#print(saat)
#print(dakika)
#print(saat2)

acik = datetime.ctime(zaman)
acik = datetime.strftime(zaman,"%X %A")
# %Y %X %d %A %B
(print(acik))


def kup():
    for i in range(10+1):
        yield i**3

for i in kup():
    print(i)

"""
hafızada boş yere yer kaplamaz ne zaman ihtiyaç duyulursa i ye o zaman çalıştırılır

"""
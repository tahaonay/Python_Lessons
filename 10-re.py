import re 

komutlar = dir(re)

# print(komutlar)

# ifade kontrolu,

# re module

str= "python kursu deneme"


sonuc = re.findall("python",str)
sonuc = re.split(" ",str)
sonuc2 = re.sub(" ","-",str)
print(sonuc2)



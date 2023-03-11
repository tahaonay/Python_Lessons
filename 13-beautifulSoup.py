import requests 
from bs4 import BeautifulSoup


url= "https://myanimelist.net/anime/season/schedule"

response = requests.get(url).content
#content = response.content
#print(content)

soup = BeautifulSoup(response,"html.parser")

list = soup.find("div",{"class":"js-categories-seasonal"})

mon= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-monday"}).find_all("h2",{"class":"h2_anime_title"})
tue= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-tuesday"}).find_all("h2",{"class":"h2_anime_title"})
wed= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-wednesday"}).find_all("h2",{"class":"h2_anime_title"})
thu= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-thursday"}).find_all("h2",{"class":"h2_anime_title"})
fri= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-friday"}).find_all("h2",{"class":"h2_anime_title"})
sat= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-saturday"}).find_all("h2",{"class":"h2_anime_title"})
sun= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-sunday"}).find_all("h2",{"class":"h2_anime_title"})
oth= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-other"}).find_all("h2",{"class":"h2_anime_title"})
unk= soup.find("div",{"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-unknown"}).find_all("h2",{"class":"h2_anime_title"})

name = soup.find_all("h2",{"class":"h2_anime_title"})
sira = 1

for i in name:
    title = i.find("a").text
    print(sira,title)
    sira += 1

print("Bulunan kayit: ",len(name))



from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url = "https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=T27BMD7YS41Q1YQH1DZF&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3"
filmListesi = []
imdbListesi = []

def getUrl():
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    list = soup.find("tbody", {"class" : "lister-list"}).find_all("tr") #buraya limit degeri de girilebilir.
    count = 0
    for tr in list:
        title = tr.find("td", {"class": "titleColumn"}).find("a").text
        year = tr.find("td", {"class": "titleColumn"}).find("span", {"class": "secondaryInfo"}).text.strip("()")
        rating = tr.find("td", {"class": "ratingColumn imdbRating"}).find("strong").text
        count += 1
        a = (count, title, year, rating)
        filmListesi.append(a)

getUrl()

def toExcell():
    for i in filmListesi:
        print(i)
        imdbListesi.append(i[3])
    filmDataFrame = pd.DataFrame(data= filmListesi)
    filmDataFrame.columns = ["Number", "Name".ljust(10), "Year", "IMDB"]
    print(filmDataFrame)
    filmDataFrame.to_csv("IMDB Film Arsivi", index= False)
    filmDataFrame.to_excel("IMDB Film Arsivi.xlsx", index= False)

toExcell()
x_list = np.linspace(1,250,250)
filmDizisi = np.array(imdbListesi)
plt.plot(x_list, imdbListesi, label= "IMDB FİLMLERİ")
plt.legend(bbox_to_anchor=(1, 1), loc='lower right')
plt.xlabel("FİLM LİSTESİ")
plt.ylabel("IMDB PUANLARI")
plt.savefig("IMDB.png", dpi=200)



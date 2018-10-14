from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
pink_text = raw_data.decode("utf-8")
soup = BeautifulSoup(pink_text, "html.parser")
h3 = soup.find_all("h3")
h4 = soup.find_all("h4")
new_list = []
for i in range(min(h3.__len__(),h4.__len__())):
    news = {
        "Name": h3[i].string,
        "Artist": h4[i].string,
    }
    new_list.append(news)
    
pyexcel.save_as(records= new_list, dest_file_name= "itune.xlsx")

from youtube_dl import YoutubeDL
options = {
    'default': 'ytsearch',
    'maxdownload': 1
}
h3 = url + h4["href"]
dl = YoutubeDL()
for linkk in new_list:
    dl.download(h3)
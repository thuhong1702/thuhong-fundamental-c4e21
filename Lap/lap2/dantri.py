# 1 download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://dantri.com.vn"
#1.1 Connect
conn = urlopen(url)

#1.2 download raw
raw_data = conn.read()

#1.3 decode data
webpage_text = raw_data.decode("utf-8")

#1.4 Save data
# f = open("dantri.html", "wb")
# #w = write
# f.write(raw_data)
# f.close()

# 2 Extract ROI
# 21 convert text to soup
soup = BeautifulSoup(webpage_text,"html.parser")
ul = soup.find("ul", "ul1 ulnew")
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    a = li.a
    title = a.string
    link = url + a["href"]
    # print(title)
    # print(link)
    news = {
        "Title": title,
        "Link": link
    }
    print("***")
    new_list.append(news)
    print(*new_list, sep="\n*****\n")
    # print(soup.prettify())
    #3 exract data
    #4 save data
pyexcel.save_as(records= new_list, dest_file_name="dantri.xlsx")
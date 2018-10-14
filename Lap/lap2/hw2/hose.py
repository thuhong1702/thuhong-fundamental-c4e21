import pyexcel
from collections import OrderedDict
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
pink = urlopen(url)
raw_data = pink.read()
pink_text = raw_data.decode("utf-8")


soup = BeautifulSoup(pink_text, "html.parser")
all_tr = soup.find_all("tr","r_item")
new_list = []

list_tieude = soup.find_all("td","h_t")
print(list_tieude)

tieude1 = list_tieude[0].string.replace(" ","")
tieude2 = list_tieude[1].string.replace(" ","")
tieude3 = list_tieude[2].string.replace(" ","")
tieude4 = list_tieude[3].string.replace(" ","")

for tr in all_tr:
    all_td = tr.find_all("td")
    title = all_td[0].string
    title = title.replace("\r\n                \xa0\xa0\r\n                ","")
    cot1 = all_td[1].string
    cot2 = all_td[2].string
    cot3 = all_td[3].string
    cot4 = all_td[4].string

    new = {
        "Title": title,
        tieude1: cot1,
        tieude2: cot2,
        tieude3: cot3,
        tieude4: cot4,  
    }
    new_list.append(new)
print("Saving data")
pyexcel.save_as(records= new_list, dest_file_name="hose.xlsx")
print("Done")
   
        


    # /ew_list, sep="\n*****\n")
    # print(soup.prettify())
    #3 exract data
    #4 save data
# pyexcel.save_as(records= new_list, dest_file_name="dantri.xlsx")
# tds_list = div.find_all("td")
# div_list = []
# for td in tds_list:
#     print(td)
# pyexcel.save_as(records= div, dest_file_name= "cty co phan sua vn")

   
from collections import OrderedDict
r1 = {
    "stt": "1",
    "ten": "huy",
    "muc luong": 25,
    "so gio lam": 14,

}
r2 = {
    "stt": "2",
    "ten": "hoa",
    "muc luong": 20,
    "so gio lam": 7,
}
r3 = {
    "stt": "3",
    "ten": "tam",
    "muc luong": 15,
    "so gio lam": 20,
}
menu = [r1, r2, r3]
total_tong = 0
tong_list = []
for menu in menu:
    ten = menu["ten"]
    mucluong = menu["muc luong"]
    sogiolam = menu["so gio lam"]
    tong_info = OrderedDict({
        "name":ten,
        "tong":mucluong*sogiolam,
        "so gio lam": sogiolam,
    })
    tong_list.append(tong_info)
    tong = mucluong*sogiolam
    total_tong += tong
    print(ten,"luong 1 thang: ", tong)
print("total tong", total_tong)
import pyexcel

pyexcel.save_as(records=tong_list, dest_file_name="bangluong.xlsx")
# for i in menu:
#     print(i)

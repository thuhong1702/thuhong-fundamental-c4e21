# from collections import OrderedDict

# 1.prepare data

data = [
    # OrderedDict(
    {
        "name": "Hong",
        "age": "19",
    }
    #)
    ,
    {
        "name": "Hon",
        "age": "19",
    },
    {
        "name": "Ho",
        "age": "19",
    }
]
#2. save
pyexcel.save_as(records=data, dest_file_name="honghong.xlsx")
# pip install pyexcel // pip install pyexcel-xlsx
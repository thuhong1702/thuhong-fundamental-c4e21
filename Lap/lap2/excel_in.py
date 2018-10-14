import pyexcel
from collections import OrderedDict
data = [
    OrderedDict({
        'name': 'may',
        'age': 50   
    }),
    OrderedDict({
        'name': 'be',
        'age': 11  
    }),
    OrderedDict({
        'name': 'hong',
        'age': 19   
    })
]
pyexcel.save_as(records= data, dest_file_name="sample.xlsx")
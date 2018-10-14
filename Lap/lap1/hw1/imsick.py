from gmail import GMail, Message
gmail = GMail('pink170299@gmail.com', 'hong012356789')
html_pink = '''
<p>Em ch&agrave;o boss ạ!</p>
<p>Em l&agrave; Hồng đ&acirc;y. =)) Nay em ốm mất rồi.</p>
{{problems}}
<p>Boss cho em nghỉ hoạt động đo&agrave;n hội h&ocirc;m nay nh&eacute;&nbsp;<span style="color: #ff99cc;">&lt;3&nbsp;</span></p>
<p><span style="color: #000000;">Em cảm ơn boss nh&igrave;u nh&igrave;u nha&nbsp;<span style="color: #ff99cc;">&lt;3 &lt;3</span></span></p>
'''
from random import choice
list_problems= ['cảm cúm', 'gãy tay', 'đau đầu', 'hen suyễn', 'trật khớp']
x = choice(list_problems)
html_pinkka = html_pink.replace("{{problems}}", x)
msg = Message('xin nghỉ ốm', to= 'pink102h2@gmail.com', html= html_pink)
import datetime

while True:
    pink_time = datetime.datetime.now()
    if pink_time.hour == 22:
        print(pink_time.hour)
        gmail.send(msg)
        print("ok")
        break


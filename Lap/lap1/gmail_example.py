from gmail import GMail, Message
gmail = GMail('pink170299@gmail.com', 'hong012356789')
html_template = '''
{{sympton}}
<p>my name is Hong, nice to meet you.</p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-wink.gif" alt="wink" />&nbsp;</p>
<p>https://pin.it/teqfhzi2zwmevz</p>
'''
from random import choice
list_name = ['sky', 'amazing', 'magic']
x = choice(list_name)

html_content = html_template.replace("{{sympton}}", x )
msg = Message('something', to= 'c4e.techkidsvn@gmail.com', html= html_content)
gmail.send(msg)
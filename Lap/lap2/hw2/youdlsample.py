from youtube_dl import YoutubeDL
options = {
    'default': 'ytsearch',
    'maxdownload': 1
}
dl = YoutubeDL()
dl.download(['https://youtu.be/mWRsgZuwf_8'])


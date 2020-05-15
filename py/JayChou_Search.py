import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
from bs4 import BeautifulSoup

# res = requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6', headers=headers)

res = requests.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=69915796990886583&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0',
    headers = headers)
music_list = res.json()

song_list = music_list['data']['song']['list']
print('QQ音乐周杰伦歌曲名称:')
for song in song_list:
    # 歌曲名称
    song_name = '♪'+song['name']

    # 所属专辑
    song_ab = song['album']['name']

    # 播放时长
    song_time = str(song['interval'])+'秒'

    # 播放链接
    play_link = 'https://y.qq.com/n/yqq/song/'+song['mid']+'.html'

    print(song_name+'\t'+song_ab+'\t'+song_time+'\n'+play_link)









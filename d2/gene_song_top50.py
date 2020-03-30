import requests
from bs4 import BeautifulSoup
import pandas as pd 

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rowlist = []

for x, song in enumerate(songs):
    song_name = song.select_one('td.info > a.title.ellipsis')
    singer = song.select_one('td.info > a.artist.ellipsis')
    l_song = (song_name.text).strip()
    l_singer = (singer.text).strip()
    
    result = {}
    result['rank'] = x+1
    result['song'] = l_song
    result['singer'] = l_singer
    
    rowlist.append(result)

df = pd.DataFrame(rowlist)  
df.to_csv("gene_song_top50.csv", index=False)

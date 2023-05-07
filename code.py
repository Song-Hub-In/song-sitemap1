from __future__ import division
import sys
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

wunder = requests.get("https://www.hungama.com/sitemap/song/song-sitemap1.xml")
parcala = BeautifulSoup(wunder.content, "xml")
urls_from_xml = []
loc_tags = parcala.find_all('loc')
for loc in loc_tags:
    urls_from_xml.append(loc.get_text().split("/")[5])
   
#print(urls_from_xml)

def MidSongLink(song_id):
    wunder = requests.get("https://curls.api.hungama.com/v1/content/"+song_id+"/url/playable?contentType=4&alang=en&mlang=en&vlang=ta&device=web&platform=a&storeId=1&uid=1036627096")
    url = wunder.json()["data"]["body"]["data"]["url"]["playable"][2]["data"]
    r = requests.get(url, allow_redirects=True)
    open("mid/"+song_id+'.mp3', 'wb').write(r.content)
#MidSongLink("48199199")

p = Pool(70)
# p.map(handle, songId)
num_tasks = len(urls_from_xml)
print(num_tasks)
for i, _ in enumerate(p.imap_unordered(MidSongLink, urls_from_xml), 1):
    sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))

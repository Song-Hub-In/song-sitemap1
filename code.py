from __future__ import division
from multiprocessing import Pool
from bs4 import BeautifulSoup
from requests import get
from json import loads
import sys
import os.path


def MidSongLink(song_id):
    check_file = os.path.isfile("mid/"+song_id+'.mp3')
    if(not check_file):
        try:
            wunder = get("https://curls.api.hungama.com/v1/content/"+song_id+"/url/playable?contentType=4&alang=en&mlang=en&vlang=ta&device=web&platform=a&storeId=1&uid=1036627096", timeout=10)
            open("json/"+song_id+'.json', 'wb').write(wunder.content)

            url = wunder.json()["data"]["body"]["data"]["url"]["playable"][2]["data"]

            r = get(url, allow_redirects=True)
            open("mid/"+song_id+'.mp3', 'wb').write(r.content)
        except:
            pass
with open(sys.argv[1], "r") as file1:
    song_id = file1.readlines()

song_id = [i.strip() for i in song_id]

p = Pool(50)
num_tasks = len(song_id)
print(num_tasks)
for i, _ in enumerate(p.imap_unordered(MidSongLink, song_id), 1):
    sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))

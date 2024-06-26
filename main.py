import shutil
import requests
from PIL import Image, ImageFilter
from colorthief import ColorThief
import time
import plugs
import numpy as np
import subprocess
import shlex
import webcolors
import bisect
latest = [0]
colour2={}
def resizing(file, name, value):
    img = Image.open(file)
    sizing = img.resize((round(img.width/int(value)),round(img.height/int(value))), resample=Image.Resampling.BILINEAR)
    sizing.save(name, dpi=(round(img.width/value), round(img.height/value)))

def colour_and_brightness(pic):
    start = time.time()
    img = Image.open(pic).convert("RGB")
    data = img.getdata()
    for i in data:
        bright = (i[0]*299+i[1]*587+i[2]*144) / 1000
        color = i[0],i[1],i[2]
        colour2.update({int(round(bright)): color})
    print(time.time()-start)


def main():
        if plugs.artwork() == None:
            pass
        elif plugs.artwork() == '':
            pass
        else:
            start = time.time()
            latest[0] = plugs.song()
            res = requests.get(plugs.artwork(), stream=True)
            with open("somesong.png", 'wb') as f:
                shutil.copyfileobj(res.raw,f)
            resizing("somesong.png", "somesong.png", 5) #7 or 6
            colour_and_brightness("somesong.png")
            print(len(colour2))
            img = Image.open("sun.png")
            data = img.getdata()
            ndata = []
            colour = sorted(list(colour2.keys()))
            for i in data:
                brightt = (i[0]*299+i[1]*587+i[2]*144) / 1000
                if brightt in colour2:
                    search = colour2.get(brightt)
                    ndata.append(search)
                else:
                    bi = bisect.bisect_right(colour, brightt)
                    if bi ==0:
                       search = colour2[colour[0]]
                       ndata.append(search)
                    else:
                       search = colour2[colour[bi-1]]
                       ndata.append(search)
            img.putdata(ndata)
            img.save("wallpapermodpil.png", "PNG")
            img = Image.open("wallpapermodpil.png")
            subprocess.Popen(shlex.split(f'swww img /home/Sam/spotifywall/wallpapermodpil.png'), stdout=subprocess.PIPE)
            print(time.time()-start)

while True:
    if plugs.artwork() == None:
        pass
    if latest[0]==0:
        main()
    if latest[0]==plugs.song():
        pass
    else:
        latest[0]=0
        colour2.clear()
        main()

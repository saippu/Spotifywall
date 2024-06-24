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
latest = [0]
colour2={}
def resizing(file, name, value):
    img = Image.open(file)
    sizing = img.resize((round(img.width/int(value)),round(img.height/int(value))), resample=Image.Resampling.BILINEAR)
    sizing.save(name, dpi=(round(img.width/value), round(img.height/value)))

def colour_and_brightness(pic):
    img = Image.open(pic)
    data = img.getdata()
    for i in data:
        bright = (i[0]*299+i[1]*587+i[2]*144) / 1000
        color = i[0],i[1],i[2]
        colour2.update({round(bright): color})

def main():
        start = time.time()
        latest[0] = plugs.song()
        res = requests.get(plugs.artwork(), stream=True)
        with open("somesong.png", 'wb') as f:
            shutil.copyfileobj(res.raw,f)
        resizing("somesong.png", "somesong.png", 8) #7 or 6
        colour_and_brightness("somesong.png")
        print(len(colour2))
        img = Image.open("sun.png")
        data = img.getdata()
        ndata = []
        for i in data:
            brightt = (i[0]*299+i[1]*587+i[2]*144) / 1000
            closest = colour2.get(brightt) or colour2[min(colour2.keys(),key=lambda key: abs(key-brightt))]
            ndata.append(closest)
        img.putdata(ndata)
        img.save("wallpapermodpil.png", "PNG")
        img = Image.open("wallpapermodpil.png")
        subprocess.Popen(shlex.split(f'swww img ~/spotifywall/wallpapermodpil.png'), stdout=subprocess.PIPE)
        print(time.time()-start)

while True:
    if plugs.song() == None:
        pass
    if latest[0]==0:
        main()
    if latest[0]==plugs.song():
        pass
    else:
        latest[0]=0
        colour2.clear()
        main()

from colorthief import ColorThief
from urllib.request import urlopen
import io
import pandas as pd
import numpy as np
import ssl
import socket
from cmu_112_graphics import *


# def dominantColor(url):
#     try:
#         print(url)
#         img = urlopen(url)
#         print('1')
#         f = io.BytesIO(img.read())
#         print('2')
#         color_thief = ColorThief(f)
#         print('3')
#         color = color_thief.get_color(quality=1)
#         print(color)
#         return color
#     except:
#         print('this happened')
#         return np.NaN

def dominantColor(url):
    response = requests.request('GET', url) # path is a URL!
    f = io.BytesIO(response.content)
    color_thief = ColorThief(f)
    color = color_thief.get_color(quality=1)
    return color
    
def main():
    df = pd.read_csv("emotionimages.csv")
    urls = df['URLs']
    colors = [dominantColor(url) for url in urls]
    df['color'] = colors
    df.to_csv("emotions_images_colors.csv")
    print('Done.')
  
main()
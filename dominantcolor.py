from colorthief import ColorThief
import io
import pandas as pd
from cmu_112_graphics import *

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
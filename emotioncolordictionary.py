import pandas as pd

def strToInt(r):
    result = ''
    for char in r:
        if char.isdigit():
            result += char
    return int(result)

def fixRGB(r, g, b):
    return strToInt(r), strToInt(g), strToInt(b)

def createDict():
    emotionColors = dict()
    with open('emotions_images_colors.csv') as f:
        fileString = f.read()
    
    firstLine = True
    for line in fileString.splitlines():
        if firstLine:
            firstLine = False
            continue
        (index, emotion, url, r, g, b) = line.split(',')
        (r, g, b) = fixRGB(r, g, b)
        emotionColors[emotion] = emotionColors.get(emotion, []) + [(r, g, b)]
    # df = pd.read_csv("emotions_images_colors_subset.csv")        
    # emotions = df['Emotion']
    # colors = df['color']
    return emotionColors


print(createDict())
import pandas as pd
import requests
from bs4 import BeautifulSoup 
import csv

# converting csv of data to dataframe
dataframe = pd.read_csv('emotions.txt', sep=",",header=None)
dfWords = dataframe[0]
listOfEmotions = dfWords.values.tolist()
setOfEmotions = set(listOfEmotions)
subsetOfEmotions = set(listOfEmotions[0:5])

def createCSV():
    emotionsImages = dict()

    for emotion in setOfEmotions:
        emotionsImages[emotion] = []

        url = f'''https://www.google.com/search?q={emotion}&sxsrf=ALiCzsbU_4iqCOO_EV-A4KOIHte-_LSP_A:1667679491520&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjivMOd7pf7AhVKmokEHTv1DRkQ_AUoAXoECAEQAw&cshid=1667679510040315&biw=1512&bih=798&dpr=2'''

        urlRequest = requests.get(url)
        soup = BeautifulSoup(urlRequest.text, 'html.parser') 
        for item in soup.find_all('img'):
            if 'gif' not in item['src']:
                emotionsImages[emotion].append(item['src'])

    with open('emotionimages.csv', 'w') as f:
        wr = csv.writer(f)
        wr.writerow(['Emotion', 'URLs'])
        for emotion in emotionsImages:
            links = (emotionsImages[emotion])
            for link in links:
                wr.writerow([emotion, link])
    print('Done.')

createCSV()
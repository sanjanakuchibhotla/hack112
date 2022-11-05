import pandas as pd
import requests
from bs4 import BeautifulSoup 

# converting csv of data to dataframe
dataframe = pd.read_csv('emotions.txt', sep=",",header=None)
dfWords = dataframe[0]
#print(dfWords)
listOfEmotions = dfWords.values.tolist()
print(type(listOfEmotions))
print(listOfEmotions)
setOfEmotions = set(listOfEmotions)
randomEmotion = input("Choose an emotion")
wordInList = False
while not wordInList:
    if randomEmotion not in setOfEmotions:
        randomEmotion = input("Choose another emotion")
    else:
        wordInList = True

url = f'''https://www.google.com/search?q={randomEmotion}&sxsrf=ALiCzsbU_4iqCOO_EV-A4KOIHte-_LSP_A:1667679491520&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjivMOd7pf7AhVKmokEHTv1DRkQ_AUoAXoECAEQAw&cshid=1667679510040315&biw=1512&bih=798&dpr=2'''

urlRequest = requests.get(url)
print (urlRequest)
soup = BeautifulSoup(urlRequest.text, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])
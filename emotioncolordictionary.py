import random

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
        (_, emotion, _, r, g, b) = line.split(',')
        (r, g, b) = fixRGB(r, g, b)
        emotionColors[emotion] = emotionColors.get(emotion, []) + [(r, g, b)]
    return emotionColors

emotionColors = createDict()

def generateRandColors():
    emotion = input('Enter an emotion bitch --> ')
    randomEmotion = dict()
    emotion = emotion.lower()
    if emotion not in emotionColors:
        print("Sorry! We don't have that emotion. Try a different one!")
        return generateRandColors()
    else:
        (one, two, three) = (random.randint(1, 19), random.randint(1, 19), 
            random.randint(1, 19))
        while one == two:
            one = random.randint(1,19)
        while one == three:
            one = random.randint(1, 19)
            while two == three:
                two = random.randint(1, 19)
    randomEmotion[emotion] = [emotionColors[emotion][one], emotionColors[emotion][two],
        emotionColors[emotion][three]]
    print(randomEmotion)
    return randomEmotion

generateRandColors()
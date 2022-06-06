import random
import data

baseArr = []
arr = []

def generator():
    baseArr.clear()
    arr.clear()
    x = random.randint(2, 5)
    
    if x == 2:
        arr.append(genreWord(data.genreWords["fillers"]) if random.randint(0, 1) < 1 else (getWordFromData(data.genreWords["starters"])))
        arr.append(genreWord(data.genreWords["fillers"]))

    if x > 2:
        arr.append(genreWord(data.genreWords["fillers"]) if random.randint(0, 1) < 1 else (getWordFromData(data.genreWords["starters"])))
        arr.append(genreWord(data.genreWords["fillers"]) if random.randint(0, 2) < 2 else (getWordFromData(data.genreWords["nationality"])))
        y = x
        coregrindAvailable = True
        while y - 3 > 0:
            if coregrindAvailable and random.randint(0, 1) < 1:
                arr.append(coreWord(data.genreWords["fillers"]) if random.randint(0, 2) < 2 else (genreWord(data.genreWords["core"])))
                coregrindAvailable = False
            elif coregrindAvailable and random.randint(0, 1) < 1:
                arr.append(grindWord(data.genreWords["fillers"]) if random.randint(0, 2) < 2 else (genreWord(data.genreWords["grind"])))
                coregrindAvailable = False
            else:
                arr.append(genreWord(data.genreWords["fillers"]))
            y -= 1
        arr.append(genreWord(data.genreWords["fillers"]) if random.randint(0, 1) < 1 else (getWordFromData(data.genreWords["enders"])))

    return (' '.join(arr) + ' Metal :metal:')

def genreWord(wordData):
    word = getWordFromData(wordData)
    word = word if random.randint(0, 5) < 5 else word + '-' + getWordFromData(data.genreWords["fillers"])
    word = word if random.randint(0, 5) < 5 else getWordFromData(data.genreWords["prefix"]) + '-' + word
    return word

def coreWord(wordData):
    word = getWordFromData(wordData)
    word = word + 'core'
    return word

def grindWord(wordData):
    word = getWordFromData(wordData)
    word = word + 'grind'
    return word

def getWordFromData(wordData):
    word = random.choice(wordData)
    while word in baseArr:
        word = random.choice(wordData)
    baseArr.append(word)
    return word

def create26LengthDict():
    arr = []
    for i in range(0,26):
        arr.append(0)
    return arr

def initializeLetterCount(name):
    name = name.lower()
    nameLetters = create26LengthDict()

    for i in range(0,len(name)):
        nameLetters[ord(name[i]) - 97] = nameLetters[ord(name[i]) - 97] + 1
    return nameLetters

def diff(lettercount1, lettercount2):
    arr = []
    for i in range(0, 26):
        arr.append(abs(lettercount1[i] - lettercount2[i]))
    return arr

def numberOfRemainingLetters(name1, name2):
    name1Letters = initializeLetterCount(name1)
    name2Letters = initializeLetterCount(name2)
    finalLetterCount = diff(name1Letters,name2Letters)

    count = 0
    for i in range(0, 26):
        count += finalLetterCount[i]
    return count

def runFlames(number):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    for i in range(6, 1, -1):
        index = number % i
        flames.pop(index)
    return flames

def returnLetter(name1, name2):
    number = numberOfRemainingLetters(name1, name2)
    letter = runFlames(number)[0]

    return letter
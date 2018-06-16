import random

def chosseQuestions(ids, numbersQuestions):
    if (len(ids) <= numbersQuestions):
        return ids
    choosen = []
    result = []
    for i in range(0, numbersQuestions ,1):
        randElement = random.randint(0, len(ids)-1)
        while (randElement in choosen):
            randElement = random.randint(0, len(ids)-1)
        choosen.append(randElement)
    for i in choosen:
        result.append(ids[i])
    return result
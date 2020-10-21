import random

#Calculates the score for a given store
def scorecalc(customerloc, storeloc, price):
    if customerloc >= storeloc:
        distance = customerloc - storeloc
    elif customerloc < storeloc:
        distance = storeloc - customerloc
    score = ((10 - (distance)) + 3*(6 - price))
    return score


#Calculates the average profit per customer based on the locations and prices below
#La1=5 La2=6 Ca1=6 Ca2=6
def final(La1, La2, Ca1, Ca2):
    count = 0
    profit = 0
    while count < 1000000:
        count += 1
        #Creates random customer location
        customerloc = (random.random()) * 10
        #Calculates the Score for the 4 shops
        a1score = scorecalc(customerloc, La1, Ca1)
        a2score = scorecalc(customerloc, La2, Ca2)
        b1score = scorecalc(customerloc, 4, 5)
        b2score = scorecalc(customerloc, 8, 5)
        #Adds the scores
        tot = a1score + a2score + b1score + b2score
        #Percent chance of each store being chosen
        proba1 = (a1score)/(tot) * 100
        proba2 = (a2score)/(tot) * 100 + proba1
        probb1 = (b1score)/(tot) * 100 + proba2
        probb2 = (b2score)/(tot) * 100 + probb1
        #Random percent to decide the store
        chance = random.random() * 100
        #Adds customer profit to total profit if A1 or A2 is chosen
        if chance < proba1:
            profit += (Ca1-2)
        elif chance < proba2:
            profit += (Ca2-2)
    return profit / 1000000


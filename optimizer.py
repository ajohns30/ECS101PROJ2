import random
from operator import itemgetter

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

def profit(La1, La2, Ca1, Ca2):
    count = 0
    profit = 0
    while count < 1000:
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
        #probb1 = (b1score)/(tot) * 100 + proba2
        #probb2 = (b2score)/(tot) * 100 + probb1
        #Random percent to decide the store
        chance = random.random() * 100
        #Adds customer profit to total profit if A1 or A2 is chosen
        if chance < proba1:
            profit += (Ca1-2)
        elif chance < proba2:
            profit += (Ca2-2)
    return profit / 1000

def optimizer ():
    approx = []
    for l1 in range(0,11):
        for l2 in range(0,11):
            for c1 in range(2,7):
                for c2 in range(2,7):
                   approx += [(profit(l1, l2, c1, c2), [l1, l2, c1, c2])]

    high = max(approx,key=itemgetter(0))

    snd = (0,0)
    flag = 0
    stepL = 0.1
    stepC = 0.01
    finL1 = high[1][0]
    finL2 = high[1][1]
    finC1 = high[1][2]
    finC2 = high[1][3]

    while (high[0] - snd[0]) > 0.0000001:
        money = []

        for adjL1 in [-stepL, 0, stepL]:
            for adjL2 in [-stepL, 0, stepL]:
                for adjC1 in [-stepC, 0, stepC]:
                    for adjC2 in [-stepC, 0, stepC]:
                        if (finL1 + adjL1 <= 10) and (finL1 + adjL1 >= 0) and (finL2 + adjL2 <= 10) and (finL2 + adjL2 >= 0) and (finC1 + adjC1 >= 0) and (finC2 + adjC2 >= 0) and (finC1 + adjC1 <= 6) and (finC2 + adjC2 <=6):
                            money += [(profit(finL1 + adjL1, finL2 + adjL2, finC1 + adjC1, finC2 + adjC2), [finL1 + adjL1, finL2 + adjL2, finC1 + adjC1, finC2 + adjC2])]

        high = max(money,key=itemgetter(0))
        money.remove(high)
        snd = max(money,key=itemgetter(0))
        diff = (high[0] - snd[0])
        finL1 = high[1][0]
        finL2 = high[1][1]
        finC1 = high[1][2]
        finC2 = high[1][3]

        if diff < 0.000001 and flag < 6:
            stepL = stepL/10
            flag = 6
        elif diff < 0.00001 and flag < 5:
            stepL = stepL/10
            flag = 5
        elif diff < 0.0001 and flag < 4:
            stepL = stepL/10
            flag = 4
        elif diff < 0.001 and flag < 3:
            stepL = stepL/10
            flag = 3
        elif diff < 0.01 and flag < 2:
            stepL = stepL/10
            flag = 2
        elif diff < 0.1 and flag < 1:
            stepL = stepL/10
            flag = 1
    
    return "Average profit:", high[0], "Store A1 location:", high[1][0], "price: $", high[1][2], ". Store A2 location:", high[1][1], "price: $", high[1][3]

print(optimizer())

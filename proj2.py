import random

# score of an individual
# location

def score(customerloc, location, cost):
    distance = abs(customerloc) - abs(location)
    if distance < 0:
        distance = abs(location) - abs(customerloc)
    score = ((10 - (distance)) + 3*(6 - cost))
    return score

# score using
# only customer
#location as
# a paramater
# a1 will always
# be at 6km
# and 4 dollars
# a2 will always
# be at 10 km
# and 4 dollars

def scorecalc(customerloc, storeloc, price):
    if customerloc >= storeloc:
        distance = customerloc - storeloc
    elif customerloc < storeloc:
        distance = storeloc - customerloc
    score = ((10 - (distance)) + 3*(6 - price))
    return score


# PROBABILITY

# gonna use 2 for example
def total(customerloc):
    a = scorea1(customerloc)
    b = scorea2(customerloc)
    c = scoreb1(customerloc)
    d = scoreb2(customerloc)
    return a + b + c + d


#La1=5 La2=6 Ca1=6 Ca2=6
def final(La1, La2, Ca1, Ca2):
    count = 0
    profit = 0
    while count < 1000000:
        count += 1
        customerloc = (random.random()) * 10
        a1score = scorecalc(customerloc, La1, Ca1)
        a2score = scorecalc(customerloc, La2, Ca2)
        b1score = scorecalc(customerloc, 4, 5)
        b2score = scorecalc(customerloc, 8, 5)
        tot = a1score + a2score + b1score + b2score
        proba1 = (a1score)/(tot) * 100
        proba2 = (a2score)/(tot) * 100 + proba1
        probb1 = (b1score)/(tot) * 100 + proba2
        probb2 = (b2score)/(tot) * 100 + probb1
        chance = random.random() * 100
        if chance < proba1:
            profit += Ca1-2
        elif chance < proba2:
            profit += Ca2-2
    return profit / 1000000

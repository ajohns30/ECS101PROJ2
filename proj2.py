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

def scorea1(customerloc):
    if customerloc >= 6:
        distance = customerloc - 6
    elif customerloc < 6:
        distance = 6 - customerloc
    score = ((10 - (distance)) + 3*(6 - 4))
    return score

def scorea2(customerloc):
    if customerloc >= 10:
        distance = customerloc - 10
    elif customerloc < 10:
        distance = 10 - customerloc
    score = ((10 - (distance)) + 3*(6 - 4))
    return score

def scoreb1(customerloc):
    if customerloc >= 4:
        distance = customerloc - 4
    elif customerloc < 4:
        distance = 4 - customerloc
    score = ((10 - (distance)) + 3*(6 - 5))
    return score

def scoreb2(customerloc):
    if customerloc > 8:
        distance = customerloc - 8
    elif customerloc < 8:
        distance = 8 - customerloc
    score = ((10 - (distance)) + 3*(6 - 5))
    return score

# PROBABILITY

# gonna use 2 for example
def total(customerloc):
    a = scorea1(customerloc)
    b = scorea2(customerloc)
    c = scoreb1(customerloc)
    d = scoreb2(customerloc)
    return a + b + c + d

def probability(customerloc):
    result = []
    tot = total(customerloc)
    first = scorea1(customerloc)
    firstres = first / tot
    result.append(firstres)
    second = scorea2(customerloc)
    secondres = second / tot
    result.append(secondres)
    third = scoreb1(customerloc)
    thirdres = third / tot
    result.append(thirdres)
    fourth = scoreb2(customerloc)
    fourthres = fourth / tot
    result.append(fourthres)
    x = 0
    for index in result:
        if index > x:
            x = index
    return x
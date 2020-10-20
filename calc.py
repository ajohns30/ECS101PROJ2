# score of an individual
# location

def score(customerloc, location, cost):
    distance = abs(customerloc - location)
    score = ((10 - (distance)) + 3*(6 - cost))
    return score


# PROBABILITY

def probability(customerloc, storeA1Loc, storeA2Loc, storeB1Loc, storeB2Loc, priceA1, priceA2, priceB1, priceB2):
    result = []

    a1 = score(customerloc, storeA1Loc, priceA1)
    a2 = score(customerloc, storeA2Loc, priceA2)
    b1 = score(customerloc, storeB1Loc, priceB1)
    b2 = score(customerloc, storeB2Loc, priceB2)

    tot = a1 + a2 + b1 + b2

    firstres = a1 / tot
    result.append(firstres)
    secondres = a2 / tot
    result.append(secondres)
    thirdres = b1 / tot
    result.append(thirdres)
    fourthres = b2 / tot
    result.append(fourthres)

    return result
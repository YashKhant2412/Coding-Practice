x = [4, 6, 2, 8, 5, 7, 1, 9]
sm = 32

def func(x, sm):
    currSum = 0
    i, j = 0, 0
    way = []
    while j < len(x) & currSum + x[j] <= sm:
        currSum += x[j]
        j += 1
    if currSum == sm:
        way.append([i, j])
    while j < len(x):
        currSum += x[j]
        while currSum > sm:
            currSum -= x[i]
            i += 1
        if currSum == sm:
            way.append([i, j])
        j += 1
    if len(way) == 0:
        return -1
    return way

func(x, sm)

import numpy as np

trainingData = open("usps.train", "r")

train = np.fromfile("usps.train", dtype=float, count=-1, sep=" ")

test = np.fromfile("usps.test", dtype=float, count=-1, sep=" ")

#variables
K = int(train[0]) #number of classes
D = int(train[1]) #number of dimensions
numberOfTrainings = int(np.divide(len(train) - 2, D + 1))
numberOfTests = int(np.divide(len(test) - 2, D + 1))

#parsing is done here
def getVectorTest(n):
    return test[3+257*n: 259 + 257*n]

def getClassTest(n):
    return int(test[2 + n*257])

#parsing is done here
def getVectorTrain(n):
    return train[3+257*n: 259 + 257*n]

def getClassTrain(n):
    return int(train[2 + n*257])

def distance(a, b):
    return np.sum((a - b) ** 2)

def most_common(lst):
    #return max(set(lst), key=lst.count)
    count = np.zeros(11)
    for i in lst:
        count[int(i)] += 1
    return np.argmax(count)

def sort(d, c):
    length = len(d)
    for l in range(0, length - 1):
        if (d[l + 1] == -1) | (d[l + 1] > d[l]):
            tempD = d[l + 1]
            tempC = c[l + 1]
            d[l + 1] = d[l]
            c[l + 1] = c[l]
            d[l] = tempD
            c[l] = tempC
    return d, c

helper = np.divide([113, 107, 107, 110, 108, 121, 115, 117, 126, 126], numberOfTests)
print(helper)

errorCount = np.zeros(10)
for n in range(1, 11):
    for currTest in range(0, numberOfTrainings):
        neighborClass = np.zeros(n)
        neighborDistance = np.array([-1 for i in range(0, n)])
        for currTrain in range(0, numberOfTrainings):
            currDistance = distance(getVectorTrain(currTrain), getVectorTrain(currTest))
            if (neighborDistance[0] == -1) | (neighborDistance[0] > currDistance):
                neighborDistance[0] = currDistance
                neighborClass[0] = getClassTrain(currTrain)
                neighborDistance, neighborClass = sort(neighborDistance, neighborClass)
        if most_common(neighborClass) != getClassTrain(currTest):
            errorCount[n - 1] += 1
        print(errorCount)
    print(errorCount)

errorRate = np.divide(errorCount, numberOfTrainings)
print(errorRate)

'''
errorCount = np.zeros(10)
for n in range(1, 11):
    for currTest in range(0, numberOfTests):
        neighborClass = np.zeros(n)
        neighborDistance = np.array([-1 for i in range(0, n)])
        for currTrain in range(0, numberOfTrainings):
            currDistance = distance(getVectorTrain(currTrain), getVectorTest(currTest))
            if (neighborDistance[0] == -1) | (neighborDistance[0] > currDistance):
                neighborDistance[0] = currDistance
                neighborClass[0] = getClassTrain(currTrain)
                neighborDistance, neighborClass = sort(neighborDistance, neighborClass)
        if most_common(neighborClass) != getClassTest(currTest):
            errorCount[n - 1] += 1
        print(errorCount)
    print(errorCount)

errorRate = np.div(errorCount, numberOfTests)
print(errorRate)
'''



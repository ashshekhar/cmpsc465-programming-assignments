import math
def GrahamScan(P):

    yValues = [point[1] for point in P]
    smallestPointIndex = yValues.index(min(yValues))
    smallestPointx = P[smallestPointIndex][0]
    smallestPointy = P[smallestPointIndex][1]
    
    P.pop(smallestPointIndex)

    angles = []
    for point in range(len(P)):

        vectorx = P[point][0] - smallestPointx
        vectory = P[point][1] - smallestPointy


        numerator = vectorx
        denominator = math.sqrt(((vectorx)**2) + ((vectory)**2)) 
        result = numerator/denominator
        angle = math.acos(result)
        angles.append(angle)                                


    zippedList = zip(angles, P)
    zippedListSorted = sorted(zippedList)
    P = [point for _, point in zippedListSorted]

    S = []
    S.append((smallestPointx,smallestPointy))


    for point in range(2):
        S.append(P.pop(0))


    for k in range(len(P)):
        while len(S) != 0: 
            Pa = S[-1]
            Pb = S[len(S)-2]
            orientation = (Pa[0]-Pb[0])*(P[k][1] - Pa[1]) - ((P[k][0]-Pa[0])*(Pa[1] - Pb[1]))

            if (orientation<0):
                y = S.pop()
            else:
                break
        
        S.append(P[k])

    xPoints = [point[0] for point in S]
    minxIndex = xPoints.index(min(xPoints))
    maxxIndex = xPoints.index(max(xPoints))
    
    upperEnvelope = 0
    lowerEnvelope = 0

    if minxIndex > maxxIndex:
        lowerEnvelope = minxIndex-maxxIndex + 1
        upperEnvelope = len(S) - lowerEnvelope + 2
    else:
        upperEnvelope = maxxIndex-minxIndex + 1
        lowerEnvelope = len(S) - upperEnvelope + 2
    
    
    print(upperEnvelope, lowerEnvelope)



numOfLines = int(input())
lines = []
dualOfLines = []

for line in range(numOfLines):
    point = input().split(" ")
    if len(point) == 3:
        point.pop()
    dualOfLines.append((float(point[0]), -1*float(point[1])))

GrahamScan(dualOfLines)

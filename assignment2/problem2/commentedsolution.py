import math

# Now we implement Graham Scan to find the convex hull of one half of the points for upper and lower envelope
def GrahamScan(P):
    # First: find point with smallest y point 
    # THIS WORKS

    print(f"Original set of coordinates:  \n{P}\n")

    yValues = [point[1] for point in P]
    smallestPointIndex = yValues.index(min(yValues))
    smallestPointx = P[smallestPointIndex][0]
    smallestPointy = P[smallestPointIndex][1]

    print(f"Coorinate with the lowest y value:  ({smallestPointx},{smallestPointy})\n")
    
    P.pop(smallestPointIndex)

    # Second: Sort the set of points by inc angles with respect to the first point found (step 1)
    angles = []
    for point in range(len(P)):

        vectorx = P[point][0] - smallestPointx
        vectory = P[point][1] - smallestPointy

        # angle = math.atan2(vectory,vectorx) 

        numerator = vectorx
        # (vector*P[point][0]) + (smallestPointy*P[point][1])
        # # print(numerator)

        denominator = math.sqrt(((vectorx)**2) + ((vectory)**2)) 
        # # math.sqrt(((P[point][0])**2) + ((P[point][1])**2))
        # # print(denominator)

        result = numerator/denominator
        print(f"Result is {result}\n")

        angle = math.acos(result)
        print(f"Angle is {angle}\n")

        angles.append(angle)                                

    print(f"Unsorted Angles wrt to the lowest y coordinate point: \n{angles}\n")
    print(f"Set of coordinates P initially without the point with lowest y coordinate: \n{P}\n")

    # Third: Name them (P1, P2, ...)
    zipped_lists = zip(angles, P)
    sorted_zipped_lists = sorted(zipped_lists)
    sorted_list1 = [element for _, element in sorted_zipped_lists]
    print(f"Set of coordinates P, sorted based on angles, without the point with lowest y coordinate: \n {sorted_list1}\n")
    P=sorted_list1

    # Fourth: Init empty stack
    S = []
    S.append((smallestPointx,smallestPointy))
    print(f"Final points before appending to first two into S: \n {P}\n")


    # Fifth: Push first 3 points
    for point in range(2):
        # print(f"P before removal: {P}")
        # print(min(angles))
        # print(angles.index(min(angles)))
        S.append(P.pop(0))
        # print(f"P after removal: {P}\n")



    
    print(f"Final points after appending to first two into S: \n {P}\n")
    print(f"Final stack with first three values: \n {S}\n")

    # Sixth: For k is equal to 4 to n, while Stack not empty, examine the orientation going from the second element of the 
    # stack from the top to the first element to the Pkth point

    for k in range(len(P)):
        while len(S) != 0: 
            Pa = S[-1]
            Pb = S[len(S)-2]

            # (Xa-Xb)*(Yk-Ya)     - (Xk-Xa)*(Ya-Yb)
            orientation = (Pa[0]-Pb[0])*(P[k][1] - Pa[1]) - ((P[k][0]-Pa[0])*(Pa[1] - Pb[1]))
            print(f"Orientation: {orientation}\n")

            if (orientation<0):
                y = S.pop()
                print(f"Popped: {y}\n")
            else:
                break
        
        S.append(P[k])
        print(f"Appended: {P[k]}\n")

    print(S)

    xPoints = [point[0] for point in S]
    minxIndex = xPoints.index(min(xPoints))
    maxxIndex = xPoints.index(max(xPoints))
    print(f"xPoints: {xPoints}")
    print(f"minxIndex: {minxIndex}" )    
    print(f"min Point: {S[minxIndex]}")
    
    upperEnvelope = 0
    lowerEnvelope = 0

    if minxIndex > maxxIndex:
        print("1")
        lowerEnvelope = minxIndex-maxxIndex + 1
        upperEnvelope = len(S) - lowerEnvelope + 2
    else:
        print("2")
        upperEnvelope = maxxIndex-minxIndex + 1
        lowerEnvelope = len(S) - upperEnvelope + 2
    
    
    print(upperEnvelope, lowerEnvelope)

    


                
    # Seventh: If turning right, pop topmost, else break the while loop and push the kth point in the stack and
    # then end the for loop. (Direction based on vector product)

    # Eighth: The stack we are left with is the convex hull


numOfLines = int(input())
lines = []
dualOfLines = []

for line in range(numOfLines):
    point = input().split(" ")
    if len(point) == 3:
        point.pop()
    dualOfLines.append((float(point[0]), -1*float(point[1])))
    
# dualOfLines is our set P
GrahamScan(dualOfLines)




# import math
# # Now we implement Graham Scan to find the convex hull of one half of the points for upper and lower envelope
# def GrahamScan(P):
#     # First: find point with smallest y point 
#     # THIS WORKS
#     yValues = [point[1] for point in P]
#     smallestPointIndex = yValues.index(min(yValues))
#     smallestPointx = P[smallestPointIndex][0]
#     smallestPointy = P[smallestPointIndex][1]
#     P.pop(smallestPointIndex)
#     # Second: Sort the set of points by inc angles with respect to the first point found (step 1)
#     angles = []
#     for point in range(len(P)):
#         vectorx = P[point][0] - smallestPointx
#         vectory = P[point][1] - smallestPointy
#         # angle = math.atan2(vectory,vectorx) 
#         numerator = vectorx
#         # (vector*P[point][0]) + (smallestPointy*P[point][1])
#         # # print(numerator)
#         denominator = math.sqrt(((vectorx)**2) + ((vectory)**2)) 
#         # * math.sqrt(((P[point][0])**2) + ((P[point][1])**2))
#         # # print(denominator)
#         result = numerator/denominator
#         # # print(result)
#         angle = math.cos(result)
#         # print(angle)
#         angles.append(angle)                                
#     print(f"angles initial:\n {angles}")
#     print(f"P initial:\n {P}\n")
#     # Third: Name them (P1, P2, ...)
#     zipped_lists = zip(angles, P)
#     sorted_zipped_lists = sorted(zipped_lists)
#     sorted_list1 = [element for _, element in sorted_zipped_lists]
#     print(f"the sorted array is {sorted_list1}\n")
#     P=sorted_list1
#     # Fourth: Init empty stack
#     S = []
#     S.append((smallestPointx,smallestPointy))
#     # print(f"Final points: {P}")
#     # Fifth: Push first 3 points
#     for point in range(2):
#         # print(f"P before removal: {P}")
#         # print(min(angles))
#         # print(angles.index(min(angles)))
#         S.append(P.pop(0))
#         # print(f"P after removal: {P}\n")
#     tempS = [(0.62,-7.27),(3.74,7.94), (1.06,6.12) ]
#     tempP = [(0.82,-2.16), (0.43,9.54), (-0.22,-0.66), (-1.94,1.82), (-3.4,2.15), (-4.99,-3.86), (-3.55,-6.51)]
#     print(f"Final points: {P}")
#     print(f"Final stack: {S}\n")
#     # Sixth: For k is equal to 4 to n, while Stack not empty, examine the orientation going from the second element of the 
#     # stack from the top to the first element to the Pkth point
#     print("Temp Printing starts here")
#     for k in range(len(tempP)): #changed to tempP
#         while len(tempS) != 0:  #Changed to tempS
#             Pa = tempS[-1]
#             Pb = tempS[len(tempS)-2]
#             # (Xa-Xb)*(Yk-Ya)     - (Xk-Xa)*(Ya-Yb)
#             orientation = (Pa[0]-Pb[0])*(tempP[k][1] - Pa[1]) - ((tempP[k][0]-Pa[0])*(Pa[1] - Pb[1]))
#             print(f"the orientation is {orientation}")
#             if (orientation<0):
#                 y = tempS.pop()
#                 print(f"the popped value is {y}")
#             else:
#                 break
#         tempS.append(tempP[k])
#         print(f"The appended value is {tempP[k]}")
#     print(tempS)
#     # Seventh: If turning right, pop topmost, else break the while loop and push the kth point in the stack and
#     # then end the for loop. (Direction based on vector product)
#     # Eighth: The stack we are left with is the convex hull
# numOfLines = int(input())
# lines = []
# dualOfLines = []
# for line in range(numOfLines):
#     point = input().split(" ")
#     if len(point) == 3:
#         point.pop()
#     dualOfLines.append((float(point[0]), -1*float(point[1])))
# # dualOfLines is our set P
# GrahamScan(dualOfLines)








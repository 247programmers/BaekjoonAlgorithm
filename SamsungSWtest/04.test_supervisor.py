#success
import time
import math

roomcount=int(input())

A=[]
list=[]
for i in range(roomcount):

    A.append(0)


list=input().split()

for i in range(roomcount):
    A[i]=int(list[i])

mainSUP,subSUP = input().split()
mainSUP=int(mainSUP)
subSUP=int(subSUP)


leastCOUNT=[]

totalcount=roomcount

for i in range(roomcount):
    if (A[i]-mainSUP)>0:
        leastCOUNT.append(math.ceil((A[i]-mainSUP)/subSUP))
    else :
        leastCOUNT.append(0)


for i in range(roomcount):
    totalcount+=leastCOUNT[i]

print(int(totalcount))







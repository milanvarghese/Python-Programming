#importing python scripts and modules
import math

#Function Definition for batting() module
def batting(runs,balls,boundary,over_boundary):
    #Variable Declaration
    points=0
    strike_rate=(runs/balls)
    if runs>100:
        points+=(10*(math.floor(runs/100)))+(5*(math.floor(runs/50)))+(1*(math.floor(runs/2)))
    elif runs>50:
        points+=(5*(math.floor(runs/50)))+(1*(math.floor(runs/2)))
    elif runs>2:
        points+=(1*(math.floor(runs/2)))
    if strike_rate>100:
        points+=6
    if (strike_rate<100 and strike_rate>80):
        points+=2
    if boundary!=0:
        points+=(1*int(boundary)) 
    if over_boundary!=0:
        points+=(2*int(over_boundary))
    return points

#Function Definiton for bowling() module 
def bowling(wkts,overs,runs,field):
    #Variable Declaration
    point=0
    economy_rate=(runs/overs)
    point+=10*wkts
    if wkts>=5:
        point+=10
    if wkts>=3:
        point+=5
    if economy_rate<=4.5 and economy_rate>=3.5:
        point+=4
    if economy_rate<=3.5 and economy_rate>=2:
        point+=7
    if economy_rate<2:
        point+=10
    #Adding Feilding Points
    if field>=1:
        point+=10*field
    return point


    

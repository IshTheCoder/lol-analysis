import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LeagueofLegends.csv')

bres=data.bResult
rres=data.rResult

bkills=data.bKills
rkills=data.rKills


#We want to separate each kill my time, and how it affected a win or a loss.
killWinner=[]
killMinute=[]

firstblood_time=[]



def chop_till_float(A):
        try:
            out=float(A)
            return out
        except ValueError:
            A=A[0:len(A)-1]
            return chop_till_float(A)

        

A= chop_till_float('2.6123,')
##print A
bwin=[]
rwin=[]
firstblood_blue=[]
firstblood_red=[]

for index in range(len(bkills)-1):

    bwin.append(int(bres[index]))
    firstblood_blue.append(bkills[index][2:6])
    rwin.append(int(rres[index]))

    firstblood_red.append(rkills[index][2:6])

rwins_new=[]
firstblood_red_new=[]



firstblood_blue_new=[]
bwins_new=[]



for index_new in range(len(bwin)-1):

    x=firstblood_red[index_new]
    y=firstblood_blue[index_new]
    try:
        float(x)
        float(y)
        
        firstblood_red_new.append((float(x)))
        rwins_new.append(rwin[index_new])
        firstblood_blue_new.append((float(y)))
        bwins_new.append(bwin[index_new])

        
    except ValueError:
        pass

fbtime=[]
fbwinner=[]
for index_final in range((len(rwins_new)-1)):

    fb_couple=[firstblood_red_new[index_final],firstblood_blue_new[index_final]]
    
    firstbloodtime=min(fb_couple)

    in_min=fb_couple.index(min(fb_couple))

    if in_min==0 and bwins_new[index_final]==0:
        fbwin=1
    elif in_min==1 and bwins_new[index_final]==1:
        fbwin=1
    else:
        fbwin=0

    fbtime.append(firstbloodtime)

    fbwinner.append(fbwin)



#average time of first blood

print sum(fbtime)/len(fbtime)


#First blood win probability

print float(sum(fbwinner))/len(fbwinner)
    
        


        


    


        

    

##
##    firstblood=min([firstblood_blue,firstblood_blue])
##  
##
##    firstblood_time.append(firstblood)

    

    

##print sum(firstblood_time)/len(firstblood_time)


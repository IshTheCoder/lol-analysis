import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict



data = pd.read_csv('LeagueofLegends.csv')

bres=data.bResult
rres=data.rResult

bkills=data.bKills
rkills=data.rKills





data_kills=pd.read_csv('kills.csv')

kills_x_locations=data_kills.x_pos

kills_y_locations=data_kills.y_pos


kill_time=data_kills.Time

killer_id=data_kills.Killer

victim_id=data_kills.Victim



killer_list=pd.Series.tolist(killer_id)


fq= defaultdict( int )
for killer_1 in killer_list:
    fq[killer_1] += 1

inv_killer_map = {v: k for k, v in fq.iteritems()}

ordered_kill_totals=sorted(inv_killer_map.keys(),reverse=True)


topkillers=[]

for key in ordered_kill_totals:
    topkillers.append(inv_killer_map[key])

objects=topkillers[0:19]


y_pos = np.arange(len(objects))

performance=ordered_kill_totals[0:19]
print performance

fig = plt.figure()

labels=objects
plt.bar(objects,performance)
##plt.xticks(y_pos, objects)
##
plt.xlabel('Players')
plt.title('Kill totals')
##ax.legend(loc='best', fontsize=25)
##
##

plt.xticks(objects, labels, rotation='vertical')

plt.show()








##A=map(float,data_kills)
##print max(kill_time)

##kills_x_y=zip(data_kills.x_pos,data_kills.y_pos)


##print kills_x_y



def maximum2(a, n):
    if n == 1:
        return a[0]
    x = maximum2(a[n//2:], n - n//2)
    return x if x > a[0] else a[0]
def maximum(a):
    return maximum2(a, len(a))

def minimum2(a, n):
    if n == 1:
        return a[0]
    x = minimum2(a[n//2:], n - n//2)
    return x if x < a[0] else a[0]
def minimum(a):
    return minimum2(a, len(a))

x_kills=pd.Series.tolist(kills_x_locations)

##print x_kills


        
y_kills=pd.Series.tolist(kills_y_locations)



print sum(data.bResult)
print sum(data.rResult)

x_kills_new=[]
y_kills_new=[]

killer=[]


for ele in range(len(x_kills)-1):
    ele1= x_kills[ele]
    ele2= y_kills[ele]
    ele3=kill_time[ele]
    if ele1!='TooEarly' and ele2!='TooEarly' and float(ele3)<=11:
        if ele1=='nan':
            print 'Yes'
        

        x_kills_new.append(float(ele1))
        y_kills_new.append(float(ele2))



##for ele in x_kills:
##    if ele==float('NaN'):
##        print 'Yes'
##print max(x_kills_new)
##
##print max(y_kills_new)
##
##print min(x_kills_new)
##
##print min(y_kills_new)



##
##plt.hexbin(x_kills_new,y_kills_new,bins=100)
##
##plt.show()




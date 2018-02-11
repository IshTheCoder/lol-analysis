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


##fq= defaultdict( int )
##for killer_1 in killer_list:
##    fq[killer_1] += 1
##
##inv_killer_map = {v: k for k, v in fq.iteritems()}
##
##ordered_kill_totals=sorted(inv_killer_map.keys(),reverse=True)
##
##
##topkillers=[]
##
##for key in ordered_kill_totals:
##    topkillers.append(inv_killer_map[key])
##
##objects=topkillers[0:19]
##
##
##y_pos = np.arange(len(objects))
##
##performance=ordered_kill_totals[0:19]
##
##fig = plt.figure()
##
##labels=objects
##plt.bar(objects,performance)
####plt.xticks(y_pos, objects)
####
##plt.xlabel('Players')
##plt.title('Kill totals')
####ax.legend(loc='best', fontsize=25)
####
####
##
##plt.xticks(objects, labels, rotation='vertical')
##
##plt.show()








##A=map(float,data_kills)
##print max(kill_time)

##kills_x_y=zip(data_kills.x_pos,data_kills.y_pos)


##print kills_x_y






##print x_kills


        
early_killer=defaultdict( int )


killtime=pd.Series.tolist(kill_time)
fq_early= defaultdict( int )

fq_mid= defaultdict( int )

fq_late= defaultdict( int )


for ele in range(len(killtime)-1):

    ele3=killtime[ele]

    if killer_list[ele] != 'TooEarly':
        if float(ele3)<=10:
            fq_early[killer_list[ele]] += 1

        if float(ele3)>10 and float(ele3)<=17:
            fq_mid[killer_list[ele]] += 1

        if float(ele3)>17:
            fq_late[killer_list[ele]]+=1





##inv_killer_map_early = {v: k for k, v in fq_early.iteritems()}
##
##ordered_kill_totals_early=sorted(inv_killer_map_early.keys(),reverse=True)
##
##
##topkillers_early=[]
##
##for key in ordered_kill_totals_early:
##    topkillers_early.append(inv_killer_map_early[key])
##
##objects_early=topkillers_early[0:19]
####print objects_early
##
##performance_early=ordered_kill_totals_early[0:19]
##
##
##labels=objects_early
##plt.bar(objects_early,performance_early)
####plt.xticks(y_pos, objects)
####
##plt.xlabel('Players')
##plt.title('Early Kill totals')
##plt.xticks(objects_early, labels, rotation='vertical')
##
##plt.show()
##
##
##inv_killer_map_mid = {v: k for k, v in fq_mid.iteritems()}
##
##ordered_kill_totals_mid=sorted(inv_killer_map_mid.keys(),reverse=True)
##
##
##topkillers_mid=[]
##
##for key in ordered_kill_totals_mid:
##    topkillers_mid.append(inv_killer_map_mid[key])
##
##objects_mid=topkillers_mid[0:19]
####print objects_mid
##
##performance_mid=ordered_kill_totals_mid[0:19]
##
##plt.figure()
##labels=objects_mid
##plt.bar(objects_mid,performance_mid)
####plt.xticks(y_pos, objects)
####
##plt.xlabel('Players')
##plt.title('mid Kill totals')
##plt.xticks(objects_mid, labels, rotation='vertical')
##
##plt.show()
    
inv_killer_map_late = {v: k for k, v in fq_late.iteritems()}

ordered_kill_totals_late=sorted(inv_killer_map_late.keys(),reverse=True)


topkillers_late=[]

for key in ordered_kill_totals_late:
    topkillers_late.append(inv_killer_map_late[key])

objects_late=topkillers_late[0:19]
##print objects_late

performance_late=ordered_kill_totals_late[0:19]

plt.figure()
labels=objects_late
plt.bar(objects_late,performance_late)
##plt.xticks(y_pos, objects)
##
plt.xlabel('Players')
plt.title('late Kill totals')
plt.xticks(objects_late, labels, rotation='vertical')

plt.show()
        



    

        








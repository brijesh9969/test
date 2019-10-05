from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
import math

  from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
import math



#getting AND storing the data
data=read_csv("records1.csv").values.tolist()
counter=0
try:
    for i in range(len(data)):
        data[i][17]=counter

        if data[i][16]==3 and data[i+1][16]==0:
            counter=counter+1
            print(counter)
except:
    print("Exception occur")
    #getting AND storing the data
data=read_csv("records1.csv").values.tolist()
counter=0
try:
    for i in range(len(data)):
        data[i][17]=counter

        if data[i][16]==3 and data[i+1][16]==0:
            counter=counter+1
            print(counter)
except:
    print("Exception occur")
#taking the fifteen and sixteen column
# print(data)

fifteen_col=[]
sixteen_col=[]

for i in range(len(data)):
    fifteen_col.append(data[i][15])
    sixteen_col.append(data[i][16])

#taking the fifteen and sixteen column

final_list_ten = []

for i in range(0, 10):
    max1 = 0

    for j in range(len(fifteen_col)):
        if fifteen_col[j] > max1:
            max1 = fifteen_col[j];

    fifteen_col.remove(max1);
    final_list_ten.append(max1)


#print(final_list_ten)
#print(mean(final_list_ten))


##################################

time=[]
ex=[]
ey=[]
ez=[]
accx=[]
accy=[]
accz=[]
time_final=[]
ex_final=[]
ey_final=[]
ez_final=[]
accx_final=[]
accy_final=[]
accz_final=[]
j=1

def plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter):
    print("@@@@@@@@@@@@@@@@@@####################")
    # max_ex_final=max(ex_final)
    # print("max ex value")
    # print(max_ex_final)

    plt.subplot(311)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(counter-1):
        c=next(color)
        plt.plot(time_final3[i], ex_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]

        #finding max of the each set for plotting a 60 percent line
        max_ex_final=max(ex_final[i])
        # print(math.ceil(max_ex_final),-math.ceil(max_ex_final),-1)
        for j in range(math.ceil(max_ex_final),-math.ceil(max_ex_final),-1):
            y_sixty.append(j)

        for j in range(math.ceil(max_ex_final),-math.ceil(max_ex_final),-1):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s) in percent')
        plt.ylabel('ex')


    plt.subplot(312)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(counter-1):
        c=next(color)
        plt.plot(time_final3[i], ey_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]
        #finding max of the each set for plotting a 60 percent line
        max_ey_final=max(ey_final[i])
        print(math.ceil(max_ey_final))
        for j in range(math.ceil(max_ey_final)):
            y_sixty.append(j)

        for j in range(math.ceil(max_ey_final)):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s) in percent')
        plt.ylabel('ey')

    plt.subplot(313)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(counter-1):
        c=next(color)
        plt.plot(time_final3[i], ez_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]
        #finding max of the each set for plotting a 60 percent line
        max_ez_final=max(ez_final[i])
        print(math.ceil(max_ez_final))
        for j in range(math.ceil(max_ez_final)):
            y_sixty.append(j)

        for j in range(math.ceil(max_ez_final)):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s) in percent')
        plt.ylabel('ez')
    plt.show()



# print("XXXXXXXXXXXXXXXXXXXXX MAX cycle")
# max2=[]
# for i in range(len(data)):
#     max2.append(data[i][-1])
# max3=max(max2)
# print(max3)

sixty_percent=[]

try:
    for i in range(len(data)):
        if data[i][17]==j:
            if data[i][16]==2 and data[i+1][16]==3:
                ####finding a value of phase for 60%
                sixty_percent.append(data[i+1][0])
            if(j>=counter):
                break
            elif data[i][17]==j and data[i+1][17]==j+1:

                time_final.append(time)
                ex_final.append(ex)
                ey_final.append(ey)
                ez_final.append(ez)
                accx_final.append(accx)
                accy_final.append(accy)
                accz_final.append(accz)
                time=[]
                ex=[]
                ey=[]
                ez=[]
                accx=[]
                accy=[]
                accz=[]
                j+=1

            #360 is -1
            time.append((data[i][0]))
            if data[i][1]<180:
                ex.append(data[i][1])
            else:
                ex.append(data[i][1]-360)
            ey.append(data[i][2])
            ez.append(data[i][3])
            accx.append(data[i][4])
            accy.append(data[i][5])
            accz.append(data[i][6])
except:
    print("Exception2 occur")


print("########")
##########converting time into percentage
##time final is the list of the list in data

time_final3=[]
print("XXXXXXXXXXXLENGTH OF TIME")
print(len(time_final))
sixty_percent_final=[]
print("XXXXXXXXXXXLENGTH OF TIME")

for i in range(len(time_final)):
    print(i)
    time_final2=[]
    for j in range(len(time_final[i])):
        time_final2.append((j/len(time_final[i]))*100)
        for k in range(len(sixty_percent)):
            if(time_final[i][j]==sixty_percent[k]):
                # print(sixty_percent[k])
                sixty_percent_final.append((j/len(time_final[i]))*100)
    time_final3.append(time_final2)
print("DDDDDDDDDDDD")
print(sixty_percent_final)

plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter)
# plottingmap(time_final3,ey_final,"ey")
# plottingmap(time_final3,ez_final,"ez")
# plottingmap(time_final3,accx_final)
# plottingmap(time_final3,accy_final)
# plottingmap(time_final3,accz_final)

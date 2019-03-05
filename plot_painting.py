# -*- coding: utf-8 -*-
import numpy as np
from numpy import loadtxt
import csv
import pdb
import matplotlib.pyplot as plt

base = file('plot_analysis.csv', 'rb')
base.seek(0)
linenum = 0
increasing = []
gbrt = []
dtr = []
line=devia.readline()
while line!='':
    deviation.append(float(line.split(',')[0]))
    lilv.append(float(line.split(',')[1]))
    line=devia.readline()
    linenum+=1

devia.close()
i=[]
j=1
k=[]
while j<=linenum:
    i.append(j)
    k.append(0)
    j+=1
plt.bar(i,deviation,width=0.01,facecolor='black',edgecolor='black')
#plt.bar(i,lilv,width=0.01,facecolor='black',edgecolor='black')
for x,y in zip(i,deviation):
    if(y>50):
        plt.text(x,y+10,'%.2f' % y,ha='center',va='bottom')
    elif(y<-50):
        plt.text(x,y-10,'%.2f' % y,ha='center',va='bottom')
plt.plot(i,k)
plt.show()
print "%s\n"%("end!")

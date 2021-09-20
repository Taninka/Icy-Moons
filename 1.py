import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.interpolate import InterpolatedUnivariateSpline, Rbf
from scipy import interpolate
import random
from scipy import stats
import math

rho_r=[]
for i in range(2000,4000+50,50):
    rho_r.append([float(i),float(920)])
    
#print (rho_r) 
R=[]
for i in range(0,1500000,50000):
    R.append([float(i),float(1500000)])

 
hmotnost=[]

#HMOTNOSTI
#M_0=rho_r[0]*(pow(R[0],3))
for n in range(0,len(R)):
    for i in range(0,len(rho_r)):
        M_0=rho_r[i][0]*(pow(R[n][0],3))
        M = rho_r[i][1] * (pow(R[n][1],3)-pow(R[n][0],3))
        hmotnost.append([(M + M_0)*(4/3.0)*math.pi, n, i])


#print(hmotnost)

C=[]
#POLOMOER
for n in range(0,len(R)):
    for i in range(0,len(rho_r)):
        C_0=rho_r[i][0]*(pow(R[n][0],5))
        C_1 = rho_r[i][1] * (pow(R[n][1],5)-pow(R[n][0],5))
        C.append([(C_1 + C_0)*(8/15.0)*math.pi, n, i])

MoI_computed=[]
for i in range(0,len(C)):
    MoI_computed.append(C[i][0]/(hmotnost[i][0]*pow(R[0][1],2)))

#print(R[0][1])
#print (hmotnost[0][0])      
#print(C[0][0])
#print(MoI)

M = 2.80E22
MoI = 0.3464

mass_difference=[]
inertia_difference=[]

index=0
for i in range(0,len(C)):
    if (abs(hmotnost[i][0]-M)<1E19) and (abs(MoI_computed[i]-MoI)<0.0005):
        index=i

print(index)
print(abs(hmotnost[index][0]-M))
print(abs(MoI_computed[index]-MoI))

print(R[hmotnost[index][1]])
print(rho_r[hmotnost[index][2]])









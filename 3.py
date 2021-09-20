import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.interpolate import InterpolatedUnivariateSpline, Rbf
from scipy import interpolate
import random
from scipy import stats
import math

rho_r=([float(8000),float(3500),float(1100),float(920)])
    
#print (rho_r) 
R=[]
for i in range(0,1900000,50000):
    for j in range(i,1900000,50000):
        R.append([float(i),float(j),float(1900000),float(2000000)])

 
hmotnost=[]
M=[]

#HMOTNOSTI
#M_0=rho_r[0]*(pow(R[0],3))
for n in range(0,len(R)):
    M_0=rho_r[0]*(pow(R[n][0],3))
    M = rho_r[1] * (pow(R[n][1],3)-pow(R[n][0],3)) + rho_r[2] * (pow(R[n][2],3)-pow(R[n][1],3)) + rho_r[3] * (pow(R[n][3],3)-pow(R[n][2],3))
    hmotnost.append([(M + M_0)*(4/3.0)*math.pi,n])


#print(hmotnost)

C=[]
#POLOMOER
for n in range(0,len(R)):
    C_0=rho_r[0]*(pow(R[n][0],5))
    C_1 = rho_r[1] * (pow(R[n][1],5)-pow(R[n][0],5)) + rho_r[2] * (pow(R[n][2],5)-pow(R[n][1],5)) + rho_r[3] * (pow(R[n][3],5)-pow(R[n][2],5))
    C.append([(C_1 + C_0)*(8/15.0)*math.pi, n])

MoI_computed=[]
for i in range(0,len(C)):
    MoI_computed.append(C[i][0]/(hmotnost[i][0]*pow(R[0][3],2)))


M = 8.84E22
MoI = 0.3182

mass_difference=[]
inertia_difference=[]

index=[]
for i in range(0,len(C)):
    if (abs(hmotnost[i][0]-M)<1E21) and (abs(MoI_computed[i]-MoI)<0.005):
        print (i)
        index.append(i)

print(index)
print(abs(hmotnost[index[0]][0]-M))
print(abs(MoI_computed[index[0]]-MoI))

print(R[hmotnost[index[0]][1]])
print(R[index[0]])




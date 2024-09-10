import pandas as pd
import numpy as np

def equip(age,n,cost,rep,t,r,c,s):
    #list p stores the possible states at stage n
    p=[]
    if(age+n-1<=rep):
        p.append(age+n-1)
    p=p+list(np.arange(1,n))

    arr=[]
    R=0
    K=0
    for i in range(n-1,-1,-1):
        di=dict()
        for j in p:
            if(j==rep):
                K=-1
                if(i!=n-1):
                    R=r[0]+s[j]-c[0]-cost
                    R=R+arr[n-i-2][1][0]
                else:
                    R=r[0]+s[j]+s[1]-c[0]-cost
            elif i!=n-1:
                K=r[j]-c[j]+arr[n-i-2][j+1][0]
                R=r[0]+s[j]-c[0]-cost
                R=R+arr[n-i-2][1][0]
            else:
                K=r[j]+s[j+1]-c[j]
                R=r[0]+s[j]+s[1]-c[0]-cost
            if(K>R):
                mx=K
                dec='K'
            elif(R>K):
                mx=R
                dec='R'
            else:
                mx=R
                dec='P'
            if(j>=rep):
                mx=R
                dec='R'
            di[j]=[mx,dec]
        arr.append(di)
        f=0
        for k in range(len(p)):
            p[k]-=1
            if(p[k]==0):
                f=1
        if(f==1):
            p.remove(0)
    print("ITERATION TABLE: ")
    for i in range(n):
        print("stage ",n-i)
        print(arr[i])
    #list d = all possible optimal policies (initially set empty)
    d=[]
    dec=[]
    #get the total cost from stage 1
    totcost=arr[n-1][age][0]
    k=age
    d.append([dec,k])
    #backtracing to find all optimal polices
    for i in range(n-1,-1,-1):
        for j in range(len(d)):
            #check the decision
            dec=d[j][0]
            if(i!=n-1):
                #if the decision is to keep the age of matchine becomes a year older the next year
                if(dec[n-i-2]=='K'):
                    d[j][1]+=1
                #if the decision is to replace then new  matchine with age one in the next stage
                else:
                    d[j][1]=1
                k=d[j][1]
            #if the stage is 1 then only one state
            else:
                k=age
             #append the decision
            if(arr[i][k][1]!='P'):
                d[j][0].append(arr[i][k][1])
            #if the decision is keep or replace we have two choices to continue further and both are optimal policies so we ensure that we store all possible optimal policies
            else:
                dec1=dec.copy()
                d[j][0].append('K')
                dec1.append('R')
                d.append([dec1,k])
    optim=[]
    print("optimal policies: ")
    for i in range(len(d)):
        print(d[i][0])
        optim.append(d[i][0])
    print("total cost: ",totcost)
    print(d)
    return(optim,totcost)
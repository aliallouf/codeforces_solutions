# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:28:14 2022

@author: ASUS
"""
import math
n,d=tuple(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(1,n):
    for j in range (1,n):
        if b[j]<=b[j-1]:
            ans+=(b[j-1]-b[j])//d
            b[j]=b[j]+((b[j-1]-b[j])//d+1)*d
            ans=ans+1
print(ans)            
            
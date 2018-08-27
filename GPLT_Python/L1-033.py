#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:18:22 2018

@author: zhuzihao
"""

N=input().split()
m=int(N[0])
k=int(N[1])
a=[]
a.append(m//1000)
a.append((m//100)%10)
a.append((m//10)%10)
a.append(m%10)
while True:
    b=set(a)
    if len(b)==k:
        break
    m=m+1
    a=[]
    a.append(m//1000)
    a.append((m//100)%10)
    a.append((m//10)%10)
    a.append(m%10)
print(m-int(N[0]),end=' ')
for i in range(4-len(str(m))):
    print('0',end='')
print(m)
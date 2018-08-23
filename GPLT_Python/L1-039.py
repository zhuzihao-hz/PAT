#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:36:35 2018

@author: zhuzihao
"""

N=int(input())
temp=input()
if len(temp)%N==0:
    m=len(temp)//N
else:
    m=len(temp)//N+1
for i in range(N):
    for j in range(m):
        if (m-1-j)*N+i >= len(temp):
            print('',end=' ')
        else:
            print(temp[(m-1-j)*N+i],end='')
    print()
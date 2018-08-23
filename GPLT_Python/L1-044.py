#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:19:24 2018

@author: zhuzihao
"""

k=int(input())
temp=input()
t=0
dic={'ChuiZi':'Bu','JianDao':'ChuiZi','Bu':'JianDao'}
while temp!='End':
    if t==k:
        print(temp)
        t=0
    else:
        print(dic[temp])
        t=t+1
    temp=input()
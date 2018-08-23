#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:23:23 2018

@author: zhuzihao
"""

N=input().split()
b=int(N[1])-1
dic={0:'z',1:'y',2:'x',3:'w',4:'v',5:'u',6:'t',7:'s',8:'r',9:'q',10:'p',11:'o',\
     12:'n',13:'m',14:'l',15:'k',16:'j',17:'i',18:'h',19:'g',20:'f',21:'e',\
     22:'d',23:'c',24:'b',25:'a'}
p=[]
if b==0:
    p.append(0)
while b!=0:
    p.append(b%26)
    b=b//26
while len(p)<int(N[0]):
    p.append(0)
p=p[::-1]
for i in p:
    print(dic[i],end='')
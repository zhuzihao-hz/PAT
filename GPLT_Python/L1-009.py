import math
def compute(x1,x2,y1,y2):
    s1=x1*y2+y1*x2
    s2=x2*y2
    a=math.gcd(s1,s2)
    s1=int(s1/a)
    s2=int(s2/a)
    return s1,s2

    
N=int(input())
temp=input().split()
if N>1:  
    x1=int(temp[0].split('/')[0])
    x2=int(temp[0].split('/')[1])
    y1=int(temp[1].split('/')[0])
    y2=int(temp[1].split('/')[1])
    sum1,sum2=compute(x1,x2,y1,y2)
    for i in range(2,len(temp)):
        x=int(temp[i].split('/')[0])
        if x==0:
            continue
        y=int(temp[i].split('/')[1])
        sum1,sum2=compute(sum1,sum2,x,y)
else:
    sum1=int(temp[0].split('/')[0])
    sum2=int(temp[0].split('/')[1])
    a=math.gcd(sum1,sum2)
    sum1=int(sum1/a)
    sum2=int(sum2/a)

if sum1*sum2==0:
    print('0')
elif sum1*sum2<=0:
    inte=int(abs(sum1))//int(abs(sum2))
    num=int(abs(sum1))%int(abs(sum2))
    if num==0:
        print('-'+str(inte))
    elif inte==0:
        print('-'+str(num)+'/'+str(int(abs(sum2))))
    else:
        print(str(inte)+' -'+str(num)+'/'+str(int(abs(sum2))))
else:
    inte=int(sum1)//int(sum2)
    num=int(sum1)%int(sum2)
    if num==0:
        print(inte)
    elif inte==0:
        print(str(num)+'/'+str(int(sum2)))
    else:
        print(str(inte)+' '+str(num)+'/'+str(int(sum2)))

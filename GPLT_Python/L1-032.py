N=input().split()
temp=input()
a=int(N[0])
if a <= len(temp):
    print(temp[-a:])
else:
    for i in range(a-len(temp)):
        print(N[1],end='')
    print(temp)

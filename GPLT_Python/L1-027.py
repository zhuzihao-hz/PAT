s=input()
a=[]
for i in s:
    a.append(int(i))
b=set(a)
b=sorted(b,reverse=True)
print('int[] arr = new int[]{',end='')
for i in range(len(b)):
    if i==len(b)-1:
        print(str([b[i]])+'};')
    else:
        print(str(b[i]),end=',')
print('int[] index = new int[]{',end='')
for j in range(len(a)):
    if j==len(a)-1:
        print(str(b.index(a[j]))+'};')
    else:
        print(b.index(a[j]),end=',')
w,h=input().split()
m=float(w)/(float(h)**2)
print("%.1f"%m)
if m>25:
    print("PANG")
else:
    print("Hai Xing")
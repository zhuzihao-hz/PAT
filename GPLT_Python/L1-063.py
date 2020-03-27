N = int(input())
for i in range(N):
    sex, height, weight = input().split()
    height = int(height)
    weight = int(weight)
    if sex == '1':
        if height < 130:
            print("duo chi yu!", end=' ')
        elif height == 130:
            print("wan mei!", end=' ')
        else:
            print("ni li hai!", end=' ')
        if weight < 27:
            print("duo chi rou!")
        elif weight == 27:
            print("wan mei!")
        else:
            print("shao chi rou!")
    else:
        if height < 129:
            print("duo chi yu!", end=' ')
        elif height == 129:
            print("wan mei!", end=' ')
        else:
            print("ni li hai!", end=' ')
        if weight < 25:
            print("duo chi rou!")
        elif weight == 25:
            print("wan mei!")
        else:
            print("shao chi rou!")

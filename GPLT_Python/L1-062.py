N = int(input())
for i in range(N):
    s = input()
    num1 = int(s[0]) + int(s[1]) + int(s[2])
    num2 = int(s[-3]) + int(s[-2]) + int(s[-1])
    if num1 == num2:
        print("You are lucky!")
    else:
        print("Wish you good luck.")

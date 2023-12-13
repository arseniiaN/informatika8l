a=int(input("Число: "))
b=0
for i in range(2, a//2+1):
    if (a%i==0):
        b=b+1
if (b<=0):
    print("Простое")
else:
    print("Не является простым")

"""
1) take any non-negative and non-zero integer number and name it c0;
2) if it's even, evaluate a new c0 as c0 ÷ 2;
3) otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4) if c0 ≠ 1, skip to point 2.
"


c0=int(input("Enter number: "))
steps=0
while True:
    if c0==1:
       break
    if c0%2==0:
        c0=int(c0/2)
        print(c0)
    else:
        c0=int(3*c0+1)
        print(c0)
    steps+=1
print("steps= ",steps)

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

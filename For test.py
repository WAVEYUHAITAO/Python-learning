for each in "FishC":
    print(each)

    
for i in range(10):
    print(i)

for i in range(5,10,2):
    print(i)

for i in range(10,5,-2):
    print(i)


for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"是一个素数") 

print("factors of a given number")
n = int(input("enter the number whose factors you want to find"))
for i in range(1,n+1,+1):
    if(n%i==0):
        print(i)


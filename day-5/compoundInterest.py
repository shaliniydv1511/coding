

p = int(input("enter the principal"))
r = float(input("enter the rate"))
n = int(input("enter the number of times interest"))
t = int(input("enter the time"))

A = p*(1+r/n)**(n*t)

print(A)

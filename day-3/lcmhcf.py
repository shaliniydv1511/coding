def lcm(a,b):
    temp = a
    while(1):
        if(temp % b == 0 and temp % a == 0):
            break
        temp+1
    return temp

def hcf(a,b):
    if(b == 0):
        return a
    return hcf(b,a%b)

def four_hcf (a,b,c,d):
    return hcf (hcf(a,b),hcf(c,d))


a= int(input("enter the first number"))
b= int(input("enter the second number"))
c= int(input("enter the third number"))
d= int(input("enter the fourth number"))
if (a<b):
    l = lcm(a,b)
else:
    l=lcm (b,a)

if(c>d):
    k = lcm (c,d)
else:
    k = lcm (d,c)
if(l<k):
    x = lcm(k,l)
    print("lcm of four number is",x)

hcf(a,b)
hcf(c,d)
y =four_hcf(a,b,c,d)
print("hcf of four number is", y)

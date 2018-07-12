print("welcome to my calculator")
typeofsum = input("would you like to addition(a),substraction(s),multiplication(m),division(d)?")
if typeofsum=="a":
    number1= int(input("enter the first number"))
    number2= int(input("enter the second number"))
    print(number1+number2)

elif typeofsum == "s":
        number1 = int(input("enter the first number"))
        number2 = int(input("enter the second number"))
        print(number1 - number2)

elif typeofsum == "m":
            number1 = int(input("enter the first number"))
            number2 = int(input("enter the second number"))
            print(number1 * number2)

elif typeofsum == "d":
                number1 = int(input("enter the first number"))
                number2 = int(input("enter the second number"))
                print(number1 / number2)

else:
    print("sorry")
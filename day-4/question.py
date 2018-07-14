from random import randint
#Intro
print('Welcome to my Math Quiz!')
print('')
#Ask the user to enter their name
print("what is your name?")
print('Rememeber to press the "Enter" Key after every answer.')
print('')
name = input('Type your name:') #store answr in variable called 'name'
print('')
print('Hi',name+'!'+'All the best!')

score = 0
qNum = 1
#loop gor quiz

while qNum<=5:
    num1 = randint(1,100)
    num2 = randint(1,100)
    qAns = num1+num2
    print('')
    print('Question',qNum)
    print('What is',str(num1) +'plus',str(num2)+'?')
    print('')
    ans = input('Type your answer: ')

    qNum = qNum +1
    print('')

print('')
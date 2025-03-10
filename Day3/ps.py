#positive, negative,zero
print(' 1) Positive, Negitive or Zero')
user1 = input('Enter a number: ')
if user1.isdigit() or (user1[0] == '-' and user1[1:].isdigit()):
    user11 = int(user1)
    if user11 < 0:
        print(f'{user11} is Negative')
    elif user11 == 0:
        print(f'{user11} is zero')
    elif user11 > 0:
        print(f'{user11} is positive')
else:
    print('Invalid input')
print()

#Even or odd
print('Even or Odd')
user2 = input('Enter a number : ')
if(user2.isdigit()):
    user22 = int(user2)
    if(user22 % 2 == 1):
        print(f'{user22} is odd')
    else:
        print(f'{user22} is even')
else:
    print('Invalid')
print()

#vote
print('vote validation')
age = int(input('Enter u r Age : '))
if(age.isdigit()):
    age1 = int(age)
    if(age1 > 0 and age1 < 18):
        print('Not Eligible for vote')
    elif(age1 >= 18):
        print('Eligible for vote')
else:
    print('Invalid')
print()

#greater
n1,n2 = map(int,input('Enter two numbers with space : ').split())
if (n1 == n2):
    print('equal')
print(f'{n1} is greater') if (n1 > n2) else print(f'{n2} is greater')

#marks
marks = int(input('Enter marks : '))
print('Pass') if (marks) >=40 else print('Fail')

#days
day = int(input("Enter a number for days : "))
if(day == 1):
    print("Sunday")
elif(day == 2):
    print("Monday")
elif(day == 3):
    print("Tuesday")
elif(day == 4):
    print("Wednesday")
elif(day == 5):
    print("Thursday")
elif(day == 6):
    print("Friday")
elif(day == 7):
    print("Saturday")
else:
    print('Invalid')

#calculator
def on(cal):
    if(b == 0):
       print('divison with 0 is not possible')  
    if (cal == 'add'):
        return a+b
    elif (cal == 'sub'):
        return a-b
    elif (cal == 'mul'):
        return a*b
    elif (cal == 'div'):
        return a/b
    else:
        return 'invalid'
a,b = map(int,input('Enter two numbers : ').split())
print(on(input('Enter required operation of first three letters : ').lower()))

#months
mon = int(input("Enter a number for Months : "))
if(mon == 1):
    print("January")
elif(mon == 2):
    print("February")
elif(mon == 3):
    print("March")
elif(mon == 4):
    print("April")
elif(mon == 5):
    print("May")
elif(mon == 6):
    print("June")
elif(mon == 7):
    print("July")
elif(mon == 8):
    print("August")
elif(mon == 9):
    print("September")
elif(mon == 10):
    print("October")
elif(mon == 11):
    print("November")
elif(mon == 12):
    print("December")
else:
    print('Invalid')

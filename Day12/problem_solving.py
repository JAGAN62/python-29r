print('find Positive or negative or neutral')
def check1(num1):
    if num1 == 0:
      return 'neutral'
    return 'positive' if num1 > 0 else 'Negative'
print(check1(int(input('Enter a number:'))))
print(' ')


print('check Even or odd or neutral')
def check2(num2):
    if num2 == 0:
      return 'neutral'
    return 'Odd' if num2 % 2 == 1 else 'Even'
print(check2(int(input('Enter a number:'))))
print(' ')


print('Eligible to vote or not')
def check3(num3):
    return 'Eligible to vote' if num3 >= 18 else 'Not Eligible to vote'
print(check3(int(input('Enter age to check :'))))
print(' ')


print('Greatest  of two numbers')
def greater(num1,num2):
    if num1 == num2:
      return 'Equal'
    return f'{num1} is greater' if num1 > num2 else f'{num2} is greater'
num1=int(input('Enter first number: '))
num2=int(input('Ente second number: '))
print(greater(num1,num2))
print(' ')


print('check pass of a student based on marks')
def student(marks):
    return 'pass' if marks >= 40 else 'fail'
print(student(int(input('Enter student marks : '))))
print(' ')


print('Extract a week based on number')
def week(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day <= 0:
        print("Invalid input")
    else:
        print(days[(day - 1) % 7])
week(int(input("Enter a number for day: ")))
print(' ')


print('calculate numbers based on operation')
def on(cal,a,b):
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
a,b = map(int,input('Enter two numbers seperated by space : ').split())
print(on(input('Enter required operation of first three letters : ').lower(),a,b))
print(' ')


def month(mon):
    months = ['January',"February",'March','April',"May",'June','July',
              'August','September','October','November','December']
    if mon <= 0:
        return "Invalid Input"
    else:
        return months[(mon - 1) % 12]
print(month(int(input('Enter a number extract month: '))))
print(' ')


print('Greatest of three numbers')
def great(a,b,c):
    if a == b == c:
        return 'Equal'
    else:
        if a > b and a > c:
            return f'{a} is greater'
        elif b > a and b > c:
            return f'{b} is greater'
        else:
            return f'{c} is greater'
a , b , c = map(int,input('Enter 3 numbers seperated by space: ').split())
print(great(a,b,c))
print(' ')


print('check Leap year')
def leap(years):
    if (years.isdigit()):
        year = int(years)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
    else:
        print('Invalid input')
leap(input('Enter a year : '))
print(' ')


# classify a character entered by the user as a vowel, consonant, or neither.
print('Classify Characters')
def classify(char):
    vowles = 'aeiou'
    if (len(char)==1):
        if(char.isalpha() or not(char.isalnum())):
            if (char in vowles):
                print(f" '{char}' is vowle")
            elif(char.isalpha()):
                print(f" '{char}' is consonant")
            else:
                print(f" '{char}' is special Character")
        else:
            print('Invalid input')
    else:
        print('Enter single char  only')
classify(input('Enter a single character : ').lower())
print(' ')


# Calculate the grade  1. 90-100 : Grade A 2. 80-89 : Grade B 3. 70-79 : Grade C 4. <70 : Fail.
print('Grade Calculation')
def grade(user_marks):
    if(user_marks.isdigit()):
        marks = int(user_marks)
        if(marks >= 90 and marks <= 100):
            print('Grade A')
        elif(marks >=80 and marks < 90 ):
            print('Grade B')
        elif(marks >=70 and marks < 80):
            print('Grade C')
        else:
            print('Fail')
    else:
        print("Invalid input")
grade(input('Enter your marks : '))
print(' ')


# Write a program to check if three sides length form a valid triangle.
print('Check valid triangle')
def triangle(s1,s2,s3):
    if s1.isdigit() and s2.isdigit() and s3.isdigit():
        side1,side2,side3 = int(s1),int(s2),int(s3)
        if((side1+side2) > side3 and (side2+side3) > side1 and (side3+side1) > side2):
            print(f'Form a valid Triangle with side lengths {side1},{side2},{side3}.')
        else:
            print(f'Not form valid Triangle with side lengths {side1},{side2},{side3}.')
    else:
        print('Invalid input')
x , y, z = input("Enter length of three sides seperated by space : ").split()
triangle(x,y,z)
print(' ')


print('print 1 to 100 Numbers')
def numbers():
 for i in range(1, 101):
    print(i,end=' ')
numbers()
print(' ')
 

print('Sum of first n natural numbers')
def sum(user):
 if(user.isdigit()):
    num = int(user)
    print(f' sum of first {user} numbers is : {(num*(num+1))//2}' )
 else:
    print("Invalid input")
sum(input('Enter a range of number : '))
print(' ')


print('all even and odd numbers between 1 and 50')
def even_sum(num):
    even =[]
    odd = []
    i = 1
    while i <= num:
        if (i % 2 == 1):
            odd.append(i)
        else:
            even.append(i)
        i+=1
    print(f'Odd numbers from 1 to 50 are:\n {odd}')
    print(f'Even numbers from 1 to 50 are:\n {even}')
even_sum(50)
print(' ')


def table(n):
    for i in range(1,21):
        print(n,'*',i,'=',n*i)
table(int(input('Enter a number to get table from 1 to 20 multiples:\n')))
print(' ')
 

def rev(num1):
    num = num1
    res = 0
    sum =0
    while num > 0:
        rem = num % 10
        sum += rem
        res = res * 10 + rem
        num//=10
    print(f'reverse of a {num1} is : {res}')
    print(f'sum of digits in {num1} is : {sum}')
    if num1 == res:
       print(f'{num1} is palindrom')
    else:
       print(f'{num1} is not a palindrom')
rev(int(input('Enter a number to get reverse: ')))
print(' ')


print('count a digits in a number')
def digits(num1):
    num = num1
    count = 0
    while num > 0:
        count += 1
        num//=10
    return f'number of digits in {num1} is : {count}'
print(digits(int(input('Enter a number : '))))
print(' ')


print('Enter a numbers until enter a negative numbers')
def until():
    while "jagan" == "jagan":
        user = input("Enter a number: ")
        if user.isdigit() or (user.startswith('-') and user[1:].isdigit()):
            wish = int(user)
            if (wish < 0):
                print("Negative number entered. Exiting loop.")
                break
        else:
            print("Invalid input. Please enter a valid number.")
until()
print(' ')


print('Print the first 10 terms of the Fibonacci series using a for loop.')
def fibinocci():
    first = 0
    second = 1
    for jagan in range(10):
        print(first,end=" ")
        first,second = second,first+second
fibinocci()
print(' ')


# Check if a given number is a prime number using a for loop.
def check_prime(n):
    if not n.isdigit():
        return "Invalid input"
    num = int(n)
    if num <= 1:
        return f"{num} is not a prime number"
    for i in range(2,num):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"
print(check_prime(input("Enter a number to check if it's prime: ")))
print(' ')


def fact(n):
    return 1 if n <= 1 else n* fact(n-1)
print(fact(int(input('Enter a number to get factorial : '))))
print(' ')


print('all numbers from 1 to 100 that are divisible by 3 and 5')
def num():
 for jagan in range(15,100,15):
    print(jagan,end=' ')
num()
print(' ')


def exit():
 while 'jagan' == 'jagan':
    print("Menu:")
    print("1. Find the square of a number")
    print("2. Find the cube of a number")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if(choice.isdigit()):
        num = int(choice)
        if(num == 1):
            s = int(input('Enter a number to find a square : '))
            print(f'square of {s} is {s * s}')
        elif(num == 2):
            c = int(input('Enter a number to find a cube : '))
            print(f'cube of {c} is {c ** 3}')
        elif(num == 3):
            print('Exit a loop')
            break
    else:
        print('Invalid input')
exit()
print(' ')


#Implement a basic login system where the user has three attempts to enter the correct password using a loop.
name = input('User Name : ')
def password():
    print('password : 123456')
    print()
    real = '123456'
    attempt = 0
    while attempt < 3:
        user_pass = input('Enter your password : ')
        if user_pass == real:
            print('Login successful!')
            break
        else:
            attempt+=1
            remain = 3 - attempt
            if remain > 0:
                print(f"Incorrect password. You have {remain} attempts left.")
            else:
                print("Access denied. You have used all your attempts.")
                print(f'The correct password is {real}')
password()


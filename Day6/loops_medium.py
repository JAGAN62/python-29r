
#Print the first 10 terms of the Fibonacci series using a for loop.
first = 0
second = 1
for _ in range(10):
    print(first,end=" ")
    first,second = second,first+second
print()


#Check if a given number is a prime number using a for loop.
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
print()


#program to calculate the factorial of a number using a while loop.
user=input('Enter a number for factorial : ')
if(user.isdigit()):
    fact = int(user)
    i=1
    res = 1
    while i <= fact: 
        res = res * i
        i = i+1
    print(f'The factorial of {user} is {res}.')
else:
    print("Invalid input")
print()


#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
print('numbers from 1 to 100 that are divisible by 3 and 5 are :')
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print(i,end=" ")
print()


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
print(' ')
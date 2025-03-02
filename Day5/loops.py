#Print all numbers from 1 to 100 using a for loop.
print('1) print 1 to 100 Numbers')
for i in range(1, 101):
    print(i,end=' ')
print()
print()


#Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
print('2) Sum of first n natural numbers')
user = input('Enter a range of number : ')
if(user.isdigit()):
    num = int(user)
    print(f' sum of first {user} numbers is : {(num*(num+1))//2}' )
else:
    print("Invalid input")
print()


#Print all even numbers between 1 and 50 using a while loop.
print('3) all even and odd numbers between 1 and 50')
even = []
odd = []
i = 0
while i <= 50:
    if(i % 2 == 0):
        even.append(i)
        i=i+1
    else:
        odd.append(i)
        i=i+1
print('even numbers : ',even)
print('odd numbers : ',odd)
print()


#Write a program to display the multiplication table of a given number. First 20
print("4) multiplication of given number upto 20 multiples")
mul = input('Enter a number for table first 20 multiples : ')
if mul.isdigit() or (mul.count('.') < 2 and mul.replace('.', '', 1).isdigit()):
    table = float(mul)
    for i in range(1, 21):
        result = i * table
        if result.is_integer():
            print(int(table), 'x', i, '=', int(result)) 
        else:
            print(table, 'x', i, '=', format(result, '.1f')) 
else:
    print('Invalid input')
print()


#Reverse a number using a while loop. 1. Also can we get the sum of all the digits.
print('5) Reverse a number and its sum')
user= input("Enter a number for reverse : ")
if user.isdigit():
    user_num=int(user)
    i = 0
    sum = 0
    while user_num > 0:
        last = user_num % 10
        sum = sum+last
        i = i * 10 + last
        user_num =  user_num // 10
    print(f'Reversed number of {user} is ', i)
    print(f'Sum of digits in {user} is ', sum)
else:
    print('Invalid input')
print()


#program to count the number of digits in a given number using a while loop.
print('6) Count the digits of a number')
user6= input("Enter a number : ")
if user6.isdigit():
    user=int(user6)
    i = 0
    while user > 0:
        i=i+1
        user = user // 10
    print(f'Total no of digits in {user6} is {i}')
else:
    print('Invalid input')
print()

#program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.
print('7) Enter a numbers until enter a negitive numbers')
while "jagan" == "jagan":
    user = input("Enter a number: ")
    if user.isdigit() or (user.startswith('-') and user[1:].isdigit()):
        wish = int(user)
        if (wish < 0):
            print("Negative number entered. Exiting loop.")
            break
    else:
        print("Invalid input. Please enter a valid number.")

print()




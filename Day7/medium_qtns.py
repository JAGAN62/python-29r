#choose to: 1. Find the square of a number. 2. Find the cube of a number. 3. Exit.
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
            print()
        elif(num == 2):
            c = int(input('Enter a number to find a cube : '))
            print(f'cube of {c} is {c ** 3}')
            print()
        elif(num == 3):
            print('Exit a loop')
            break
    else:
        print('Invalid input')
        print()
print(' ')


#check a number is palindrome or not
try:
    palin = int(input('Enter a number to check palindrome or not: \n'))
except ValueError:
    print('Please enter a valid non negaitve numbers')
else:
    p = palin
    reverse_number = 0
    while p>0:
        remainder = p % 10
        reverse_number = reverse_number * 10 + remainder
        p = p // 10
    if (palin == reverse_number):
        print(f'{palin} is a palindrom.')
    else:
        print(f'{palin} is not a palindrom.')
print(' ')


#check a number is perfect or not
try:
    perfect = int(input('Enter a number to check perfect or not: \n'))
except ValueError:
    print('Please enter valid non negaitve numbers only')
else:
    if(perfect < 2):
        print('Not a perfect number')
    else:
        sum = 0
        for i in range(1,perfect):
            if(perfect % i == 0):
                sum+=i
        if(perfect == sum):
            print(f'{perfect} is a perfect number')
        else:
            print(f'{perfect} is not a perfect number')
print(" ")


#find LCM(Least Common Multiple) of two numbers
print('LCM(Least Common Multiple) of two numbers')
try:
    first = int(input("enter first number:\n"))
    second = int(input("enter a second number:\n"))
except ValueError:
    print("Please enter a valid non negative number")
else:
    if first > second:
        greater = first
    else:
        greater = second
    while True:
        if (greater % first==0) and (greater % second == 0):
            lcm = greater
            break
        greater += 1
    print('LCM of {0} and {1} is : {2}'.format(first,second,lcm))
print(" ")                


#find GCD(Greatest Common Divisor) of Two numbers
print("GCD(Greatest Common Divisor) of Two numbers:")
try:
    a , b = map(int,input("Enter two numbers seperated by space:\n").split())
except ValueError:
    print("Please enter a valid non negative number")
else:
    def gcd(a,b):
        if( b == 0):
            return a
        else:
            while b:
                a,b = b, a % b
            return a
    print(F'GCD of {a} and {b} is:',gcd(a,b))
print(" ")


#To calculate total allocated budget for all even numbered Teams members
try:
    even = int(input("Enter a total no.of even number teams:\n"))
except ValueError:
    print('Invalid')
else:
    def budget(n):
       sum=0
       for i in range(2,n+1,2):
           sum=sum+i*100
       return sum
           
    print('Total allocated budget:',chr(0x20B9),budget(even)) 
print()


#Write a program to find the greatest of three numbers.
print('1) Greatest of three numbers')
a , b , c = input("Enter three nums seperated by space : ").split()
if a.isdigit() and b.isdigit() and c.isdigit():
    a1,b1,c1 = int(a),int(b),int(c)
    if (a1 > b1 ) and (a1 > c1):
        print(f'{a1} is greater')
    elif (b1 > a1) and (b1 > c1):
        print(f'{b1} is greater')
    else:
        print(f'{c1} is greater')
else:
    print('Invalid input')
print()


#Check if a year is a leap year
print('2) check Leap year')
years = input('Enter a year : ')
if (years.isdigit()):
    year = int(years)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
else:
    print('Invalid input')
print()


#classify a character entered by the user as a vowel, consonant, or neither.
print('Classify Characters')
vowles = 'aeiou'
char = input('Enter a character : ').lower()
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
print()


#Calculate the grade  1. 90-100 : Grade A 2. 80-89 : Grade B 3. 70-79 : Grade C 4. <70 : Fail.
print('4) Grade Calculation')
user_marks = input('Enter your marks : ')
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
print()


#Write a program to check if three sides length form a valid triangle.
print('5) Check valid triangle')
s1,s2,s3 = input("Enter length of three sides seperated by space : ").split()
if s1.isdigit() and s2.isdigit() and s3.isdigit():
    side1,side2,side3 = int(s1),int(s2),int(s3)
    if((side1+side2) > side3 and (side2+side3) > side1 and (side3+side1) > side2):
        print(f'Form a valid Triangle with side lengths {side1},{side2},{side3}.')
    else:
        print(f'Not form valid Triangle with side lengths {side1},{side2},{side3}.')
else:
    print('Invalid Input')





        


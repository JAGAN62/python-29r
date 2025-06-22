import re

#Task1 --> Reverse a string
def reverse_string(string):
    res = ""
    for i in string:
        res = i + res
    return res
print('Reverse string: ',reverse_string(input("Enter a string: ")))


#Task2 --> Temparature convertion
def convertion():
    try:
        temp = int(input("Enter a temparature:"))
        unit = input('Enter the unit (C for Celsius),(F for fahrenheit)').lower().strip()
        if unit == "c":
            fahrenheit = (temp*(9/5))+32
            return f"{temp} celsius is equal to {fahrenheit} Fahrenheit"
        elif unit == 'f':
            celsius = (temp-32)*5/9
            return f"{temp} fahrenheit is equal to {celsius} celsius"
        else:
            return ("Enter proper Units")
    except ValueError:
        return ("Invalid inputs")
print(convertion())


#Task3 --> Email validation
def valid_mail():
    try:
        user = input('Please enter Email: ')
        pattern = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, user) is None:
            raise ValueError('Invalid Email')
        return 'Valid Email'
    except Exception as e:
        return str(e)
print(valid_mail())


#Task4 --> Calculator
def cal():
    try:
        a = input("Enter Number1 : ")
        b = input("Enter Number2 : ")
        user = int(input("choose a num for operation : \n 1 : + \n 2 : - \n 3 : * \n 4 : / \n 5: % \n"))
        if a.isdigit() and b.isdigit():
            num1 = int(a)
            num2 = int(b)
            if user == 1:
                return num1+num2
            elif user == 2 :
                return num1 - num2
            elif user == 3:
                return num1 * num2
            elif user == 4:
                if num2 == 0:
                   raise ZeroDivisionError("Cannot divide by zero")
                return num1 / num2
            elif user == 5:
                return num1 % num2
            else:
                return "Invalid option"
        else:
            return "Invalid input"
    except ValueError:
        return "Invalid input"
print(f"Answer : {cal()}")


#Task5 --> Palindrome checker
def palin(user):
    user = user.lower()
    if len(user) <=1 :
        return True
    if user[0] == user[-1]:
        return palin(user[1:-1])
    return False
print(palin(input("Enter a string to check palindrome: ")))


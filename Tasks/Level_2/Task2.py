import random

#Task1 --> Guess game
def guess():
    random_number = random.randint(1,100)
    while True:
        try:
            user = int(input("Enter a number between 1 and 100 : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if user < random_number:
            print("Too Low")
        elif user > random_number:
            print("Too High")
        else:
            print("Your guess is Correct!")
            break
guess()


#Task2 --> number guess
def guess_number():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start >= end:
            print("Invalid range! Start must be less than end.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return
    random_number = random.randint(start+1,end-1)
    while True:
        try:
            user = int(input(f"Guess a number between {start} and {end}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if user < random_number:
            print("Too Low")
        elif user > random_number:
            print("Too High")
        else:
            print("Your guess is Correct!")
            break  
guess_number()


#Task4 --> Fibinocci series
def fib():
    try:
        user = int(input("Enter a number for Fibinocci series: \n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 
    a,b = 0,1
    if user <= 0:
        print("Please enter a positive number.")
        return
    for _ in range(user):
        print(a,end=" ")
        a,b = b,a+b
fib()


#Task5 --> file handling
def file_handling():
    try:
        with open("Tasks/textfile.txt", "r") as file: 
            data = file.read().split(" ")
            ans = {}
            sorted_words = sorted(data,key=str.lower)
            count = 0
            for i in sorted_words:
                count+=1
                ans[i]=count
            print(ans)
    except FileNotFoundError:
        print("The file was not found.")
file_handling()


print('Reverse a Number program, written in functions')
def reverse(num):
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = reverse * 10 + remainder
        temp //= 10
    print(f'reverse number is : {reverse}')
    if num == reverse:
       return ('It is palindrom')
    else:
       return ('It is not palindrom')
print(reverse(int(input('Enter a number to reverse: '))))


print('factorial of a number program,written in functions')
def fact(num):
    return 1 if num <= 1 else num * fact(num - 1)
    '''
    res = 1
    i = 1
    while num > 0:
        res *= i
        i+=1
        num-=1
    return (res)
    '''
print(fact(int(input('Enter a number to Factorial: '))))


print('count occurence characters in a string')
def char_count(s):
    chars={}
    for i in s:
        if i in chars:
            chars[i]+=1
        else:
            chars[i]=1
    #   chars[i]=s.count(i)
    return chars
print(char_count(input('Enter a string count characters: ')))

def list_reverse(my_list):
    # temp = []
    # for i in my_list:
    #     temp.insert(0,i)
    # return temp

    # emp=[]
    # for j in range(len(my_list)-1,-1,-1):
    #     emp.append(my_list[j])
    # return (emp)

    # low = 0
    # high = len(my_list)-1
    # while low < high:
    #     my_list[low],my_list[high] = my_list[high] , my_list[low]
    #     low+=1
    #     high -= 1
    # return my_list

    # low = 0      
    # high = (len(my_list)//2)-1 #len(my_list)-1
    # while low < high:
    #     my_list[low],my_list[high] = my_list[high] , my_list[low]
    #     low+=1
    #     high -= 1

    n=len(my_list)
    for i in range(n//2):
        my_list[i],my_list[n - i - 1] = my_list[n - i - 1],my_list[i]
    return my_list
print(list_reverse([1,2,3,'jagan',4,5,6]))

print('Revere Half of elements in a list')
def half_list(newlist):
    low = len(newlist)//2    #0
    high = len(newlist)-1   #len(newlist)//2-1
    while low < high:
        newlist[low],newlist[high] = newlist[high],newlist[low]
        low+=1
        high-=1
    return newlist
print(half_list([4,3,2,'jagan',1,0]))


def max_min():
    print('Find maximum and minimum values in list')
    print([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    list3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    maximum_number = minimum_number = list3[0]
    sec_maximum_number = float('-inf') 
    sec_minimum_number = float('inf')  

    for i in list3:
        if i > maximum_number:
            sec_maximum_number = maximum_number  # First update sec_max
            maximum_number = i
        elif i > sec_maximum_number and i != maximum_number:
            sec_maximum_number = i
        
        if i < minimum_number:
            sec_minimum_number = minimum_number  # First update sec_min
            minimum_number = i
        elif i < sec_minimum_number and i != minimum_number:
            sec_minimum_number = i

    print('Minimum number is: ', minimum_number)
    print('Maximum number is: ', maximum_number)
    print('Second minimum number is: ', sec_minimum_number)
    print('Second maximum number is: ', sec_maximum_number)
max_min()


print('Assumed list:',['jagan',8,7,6,5,4,5,3,2,1])
def index_value(index1):
    index_list= [9,8,7,6,5,4,5,3,2,1]
    if index1 < len(index_list) and index1 >= -1 * len(index_list):
        return (index_list[index1])
    else:
        return ('out of range')
print(index_value(int(input('Enter a index value to extract element : '))))

def duplicates_uniques():
    new_list = [2,3,4,4,1,1,1,5,5,22]
    duplicates = []
    uniques = []
    for num in new_list:
        if num not in uniques and num not in duplicates:
                uniques.append(num)
        elif num in uniques:
                duplicates.append(num)
                uniques.remove(num)
    #   if num in duplicates:
    #           duplicates.append(num)
    print('duplicate values : ',duplicates)
    print('unique values : ',uniques)
duplicates_uniques()


def odd_sum(num):
    print('"sum of odd numbers in a number"')
    try:
        t = num
        sum = 0
        while t > 0:
            rem = t % 10
            if rem % 2 == 1:
                sum = sum + rem
            t = t // 10
        print(sum)
    except ValueError:
        print('Enter numbers only')
print(int(input('Enter a number: ')))

#find GCD(Greatest Common Divisor) of Two numbers
def gcd():
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
gcd()
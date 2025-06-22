#swap
a,b = -1,-2
a , b = 'hi','bye'
# a,b = b,a

# temp = a
# a = b
# b = temp
# print(a,b)

# a = a+b
# b = a - b
# a = a - b
# print(a,b)

# n ^ 0 = n
# n ^ n = 0
# a = a ^ b  #1 ^ 2
# b = a ^ b  # (1 ^ 1) ^ 2   0 ^ 2   2
# a = a ^ b  #  1 ^ (2 ^ 2)   1 ^ 0  1
# print(a,b)

#ascending
lst = [1,2,3]
def ascen(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
           return False
    return True

def descen(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
           return False
    return True

def sort():
   return ascen(lst) or descen(lst)
print(sort())
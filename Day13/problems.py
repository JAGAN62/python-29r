def sum(num):
    sum =0
    while num > 0:
        rem = num % 10
        sum += rem
        num//=10
    return sum

def even(num):
    sum =0
    while num > 0:
        rem = num % 10
        if rem%2 == 0:
          sum += rem
        num//=10
    return sum

def dup(num):
    duplicate = []
    while num > 0:
        rem = num % 10
        if rem in duplicate:
            return True
        duplicate.append(rem)
        num//=10
    return False

def increase(num):
    last1 = num % 10 
    num //= 10
    while num > 0:
        last2 = num % 10
        if last2 >= last1:
            return False
        last1 = last2
        num //=10
    return True

def not_increase(num):
    pre = 10
    while num > 0:
        digit = num % 10
        if digit > pre:
            return False
        pre = digit
        num //= 10
    return True


list = []
length = int(input('Array length : '))
for i in range(length):
    list.append(int(input('Enter a element into list:')))
print('your list : ',list)

ans = []
ans2 = []
ans3 = []
ans4 = []
ans5 = []
for i in list:
    ans.append(sum(i))
    ans2.append(even(i))
    ans3.append(dup(i))
    ans4.append(increase(i))
    ans5.append(not_increase(i))

print()
print('sum list : ',ans)
print()
print('even sum',ans2)
print()
print('duplicates exits : ',ans3)
print()
print('check ascending order of elements : ',ans4)
print()
print('check order of elements : ',ans5)


arr1 = [1,2]
arr2 = [3,4]
def subset(arr1,arr2):
 for i in arr1:
    if i in arr2:
        return('arr1 is subset of arr2')
    return('arr1 is not subset of arr2')
print(subset(arr1,arr2))
# #Find the sum of all elements in a nested list.
# def sum_nestedlist(arr):
#     # for i in range(len(arr)):
#     #     sum=0
#     #     for j in arr[i]:
#     #         sum+=j
#     #     result_array.append(sum)

#     result_array=[]
#     sum=0
#     for _ in arr:
#         sum+=_
#     result_array.append(sum)
#     return(result_array)


# # Find the minimum and maximum values in a nested list.
# def max_min_nestedarray(arr):
#     max=arr[0]
#     min=arr[0]
#     result=[]
#     for i in arr:
#         if i > max:
#             max=i
#         elif i < min:
#             min=i
#     result.append(f'min= {min}')
#     result.append(f'max= {max}')
#     return(result)


# # parameters
# l = [[1,2,3,4],[11,12,0],[7,8,9]]
# print('Example list :',l)
# ans = []
# ans2=[]
# for i in l:
#    ans.append(sum_nestedlist(i))
#    ans2.append(max_min_nestedarray(i))
# print('Sum of Nested List: ',ans)
# print('Minimum & Maximum of Nested List: ',ans2)


# Find the missing numbers - In the between max and min digits in the given inputs, find the missing digits.
# Input: 34571      Outpur : 26 missing
# def sum(temp):
#     num = temp
#     list=[]
#     while num > 0:
#         rem = num % 10
#         list.append(rem)
#         num//=10
#     max=list[0]
#     min=list[0]
#     for  i in list:
#         if max < i:
#             max=i
#         elif min > i:
#             min =i
#     for i in range(min,max):
#         if i not in list:
#             print(i,end='')

# clinet = int(input('Enter a number to find missing digits: '))
# sum(clinet)

# def even(temp):
#     maxi = max(temp)
#     mini = min(temp)
#     for i in range(mini,maxi):
#         if i % 2 == 0:
#             if i not in temp:
#                 print(i)

# even([-4,-2,2,6,8,12])






#2. Second largest element or second smallest element in a given list
# def sec_max_min(lst):
#     max1 = lst[0]
#     min1 = lst[0]
#     max2 = lst[0]
#     min2 = lst[0]
#     for i in lst:
#         if max1 < i:
#             max2 = max1
#             max1 = i
#         elif min1 > i:
#             min2 = min1
#             min1 = i
#     print('maximum number : ',max1)
#     print('Second Maximum: ',max2)
#     print('minimum number : ',min1)
#     print('Second minimum: ',min2)
# a = input('Enter a number')
# user = [int(i) for i in list(a)]
# print(user)
# sec_max_min(user)


# Given array of N integer, the task is to replace each element of the array  by its rank in the array
#    Input: 20 15 26 2 98 6       Output:4 3   5   1  6 2
# length = int(input('Enter a length of list'))
# user = input('Enter a numbers seperated by space: ').split()
# _user = list(map(int,user))
# sort_user = sorted(_user)
# ans = []
# for i in _user:
#     ans.append(sort_user.index(i)+1)
# print(user)
# print(ans)

    

    
# my_list = [1,2,3,4,5]
# for i in my_list:
#     print(i)
# print(' ')

# list2 = [1,2,3,4,0,55,-1]
# sum = 0
# min = list2[0]
# max = list2[0]
# second_max = []
# second_min = []
# for i in list2:
#     sum+=i
#     if max < i:
#         second_max = max
#         max = i
#     elif(min > i):
#         second_min = min
#         min = i
    
    
# print(sum,max,second_max,min,second_min)
# print(' ')

# i=0
# while len(list2) > i:
#     print(list2[i])
#     i+=1


# index_list= [9,8,7,6,5,4,5,3,2,1]
# index1 = int(input('Enter index: '))
# if index1 < len(index_list) and index1 >= -1 * len(index_list):
#     print(index_list[index1])
# else:
#     print('out of range')


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
           

# for i in range(len(new_list)):
#     flag = True
#     for j in range(len(new_list)):
#         if new_list[i] == new_list[j] and i != j:
#             flag = False
#             print(new_list[i],'duplicates')
#             break
#     if flag:
#         print(new_list[i])


# print("Unique numbers:", uniques)
# print("Duplicate numbers:",duplicates)
# print("Duplicate numbers:",dup_val)


d = []
u = []

#Given a list of numbers, return a dictionary of elements that appear more than once along with their counts.
list = [3,4,1,2,4,3,-1]
ans  = {}
for i in list:
    if i not in ans:
        ans[i]=1
    else:
        ans[i]+=1
ans2 = {}
for i,j in ans.items():
    if j > 1:
        ans2[i]=j
print(ans2)
print()


# Count Occurrences of Each Digit
number = 1223334444
print('Number : ',number)
dict1 = {}
while number > 0:
    rem = number % 10
    if rem not in dict1:
       dict1 = {rem: 1, **dict1}
    else:
        dict1[rem]+=1
    number//=10
print('Count Occurrences of Each Digit',dict1)
print()


# Finding the frequency of elements in an array.
#     arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2
my_list =[10, 30, 10, 20, 10, 20, 30, 10] 
print('Example list :',my_list)
dict2 = {}
for i in my_list:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i]+=1
print('frequency of elements in an list : ',dict2)
print()


# # Wap to print the number of pairs formed by the array of elements
# #  Input: 30 50 30 50 20 50 50 20 50 50    Output : 5 pairs
nums = [30, 50, 30, 50, 20, 50, 50 ,20, 50,50]
print('example list ',nums)
pairs = 0
ans = {}
for i in nums:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
for j in ans.values():
        pairs += j//2
print('No of pairs: ',pairs)




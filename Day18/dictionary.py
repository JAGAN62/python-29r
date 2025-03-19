# Questions that we will discuss for today:

# 5. Swap keys and values of a dictionary. Store keys in a list.
# 6. Given a dictionary, find the key with the highest value.
# 8. Given two dictionaries, merge them into one. If a key exists in both, sum their values.
# 9. Find if 2 strings are anagrams

dict = {'1':29,"str":3,'apple':4,'ball':4}
dict2 = {'1':30,'2':100}
# max = float('-inf')
# max_key = ''
# for i,j in dict.items():
#     if max < j:
#         max = j
#         max_key = i   
# if max != float('-inf'):
#     print(max_key,max)
# else:
#     print('dictionary empty')

# dict1={}
# for i,j in dict.items():
#     if j in dict1:
#         dict1[j].append(i)
#     else:
#         dict1[j]=[i]
# print(dict1)

# merged = {**dict,**dict2}
output = {}
for i,j in dict.items():
    output[i]=j
for i,j in dict2.items():
    if i in output:
        output[i]+=j
    else:
        output[i]=j
print(output)


#angram
s1 = 'silenit'
s2 = 'loisten'
answer = {}
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    dict1 = {}
    for i in s1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1

    for j in s2:
        if j not in dict1:
            return False
        else:
            dict1[j] -=1
    for i,j in dict1.items():
        if j != 0:
            return False
    return True

    # dict2 = {}
    # for i in s2:
    #     if i not in dict:
    #         dict2[i]+=1
    #     else:
    #         dict2[i]=1
    # if dict1 == dict2:
    #     return True
    # return False
print(anagram(s1,s2))
  



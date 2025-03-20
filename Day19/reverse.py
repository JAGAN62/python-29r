# s = 'jagan'
# print(s[: : -1])
# #loop
# ans = ''
# for i in s:
#     ans = i + ans
# print(ans)

# ans2 = ''
# for i in range(len(s)-1,-1,-1):
#     ans2+=s[i]
# print(ans2)

# #recursion
# def rev(s):
#     if len(s)<=1:
#         return s
#     return s[-1]+rev(s[0:-1])
# print(rev(s))

#palindrome

# s='omou'
# def palin(s):
#     low = 0
#     high = len(s)-1
#     while low < high:
#         if s[low] != s[high]:
#             return False
#         low+=1
#         high-=1
#     return True
# print(palin(s))


# s1 = '{a+((b-c)}+d)'
# ans2 = ''
# count = 0
# open = 0
# close = 0
# for i in s1:
#     if i in ['(',')',"[",']','{',"}"]:
#         count+=1
#     if i in ["(","{","["]:
#         open+=1
#     if i in [')',"}","]"]:
#         close+=1
# print(count)
# print(open)
# print(close)


vowles = 'aeiou'
# s = 'take u forward is awesome'
# dict = {}
# for i in s:
#     if i in vowles:
#         if i not in dict:
#             dict[i]=1
#         else:
#             dict[i]+=1
# print(dict)
# for i,j in dict.items():
#     if j == 1 :
#       print(i,end=" ")
 


    
   
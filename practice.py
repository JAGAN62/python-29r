# #check palindrome
# s = 'racecar'
# ans = ''
# for i in s:
#     ans = i + ans
# if s == ans:
#     print('palindrome')
# else:
#     print('not palindrome')


# #remove vowles form string
# vowles = 'aeiou'
# s = 'hello world'
# ans = ''
# for i in s:
#     if i not in vowles:
#         ans+=i
# print(ans)


# #sum of natural numbers
# sum = 0
# n = 5
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# #foctors of a number
# n = 6
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end=" ")
# print()


# #count words in sentsence
# s = 'python is awesome'
# string = s.split()
# count = 0
# ans = []
# for i in string:
#     if i not in ans:
#         count+=1
#     else:
#         count=1
# print(count)


# #star pattern
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

# #number pattern
# count =1
# for i in range(n):
#     for j in range(i+1):
#         print(count,end= " ")
#         count+=1
#     print()

# #0 and 1 pattern
# n=4
# for i in range(1,n+1):
#     print('i value',i)
#     for j in range(i):
#         print('j value',j)
#         print((i+j)%2,end=" ")
#     print()

# #vowles moves last to string
# s = 'jagan'#'Hyderabad'
# vowels = 'aeiou'
# ans1= ''
# ans2 = " "
# for i in s:
#     if i not in vowels:
#         ans1+=i
#     else:
#         ans2+=i
# print(ans1+ans2)
    




# #sum of digits in a number
# n = 187
# sum = 0
# def digits(n):
#     while n > 0:
#         remainder = n % 10
#         sum+=remainder
#         n//=10
# print(sum)


# list = [(2,3,4),(9,10,11)]
# t = 5
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         if t < list[i][j]:

# string = 'my name'
# sub_str = []

# for i in range(len(string)): 
#     for j in range(i+1, len(string)):  
#         sub_str.append(string[i:j]) 

# print(sub_str)



# class Solution(object):
def containsDuplicate(str1,str2):
    
    
    s={}
    t={}
    count=0
    
    for i in range(len(str1)):
        if (str1[i] not in s) and (str2[i] not in t):
            count=1
            s[str1[i]]=count
            t[str2[i]]=count
        else:
            count+=1
            s[str1[i]]=count
            t[str2[i]]=count
  
            
    for k1,k2 in zip(s,t):
        print("value:",s[k1] ,"|", "value:",t[k2])
      
        
    print(s)
    print(t)
            
         
containsDuplicate(str1="geg",str2='eed')
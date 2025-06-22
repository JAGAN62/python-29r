
# Find the word with max length in a string
# string = 'Google docs are much better than word docs'
# input = string.split()
# print('example string : ',string)
# answer = []
# max_length = input[0]
# min_length = input[0]
# for i in range(len(input)):
#     if len(max_length) < len(input[i]):
#          max_length = input[i]
#     elif len(min_length) > len(input[i]):
#          min_length = input[i]

# for i in input:
#      if len(i) > len(max_length):
#           answer.append(i)
#           answer.clear()
#           max_length = i
#      elif len(i) == len(max_length):
#           answer.append(i)
# print("maximum length word : ",answer) 
# print("minimum length word : ",min_length)
print()


#['aaaaaaaaa', 'bbbbbb', 'cabde'] - Sort strings based on lengths using bubble sort
#['cabde', 'bbbbbb', 'aaaaaaaa']
# input = ['eeeee','bb','ccc','dddd','a']
# print('Exaple list : ',input)
# for i in range(len(input)):
#      for j in range(len(input)-i-1):
#           if len(input[j]) > len(input[j+1]):
#                input[j],input[j+1] = input[j+1],input[j]
# print(input)


#longest palindrome in a string  ; a b c cc bccb cbc 

def palin(s):
    low = 0
    high = len(s)-1
    while low < high:
        if s[low] != s[high]:
            return False
        low+=1
        high-=1
    return True
     
s = 'abccbc'
palin_list = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
         if palin(s[i:j]):
              palin_list.append(s[i:j])

max_palin = palin_list[0]
for i in palin_list:
     if len(i) > len(max_palin):
          max_palin = i
print(palin_list)
print(max_palin)

              
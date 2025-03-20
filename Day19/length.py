
# Find the word with max length in a string
string = 'Google docs are much better than word documents'
input = string.split()
print('example string : ',string)

max_length = input[0]
min_length = input[0]
for i in range(len(input)):
    if len(max_length) < len(input[i]):
         max_length = input[i]
    elif len(min_length) > len(input[i]):
         min_length = input[i]
print("maximum length word : ",max_length) 
print("minimum length word : ",min_length)



#['aaaaaaaaa', 'bbbbbb', 'cabde'] - Sort strings based on lengths using bubble sort
#['cabde', 'bbbbbb', 'aaaaaaaa']
input = ['eeeee','bb','ccc','dddd','a']
for i in range(len(input)):
     for j in range(len(input)-i-1):
          if len(input[j]) > len(input[j+1]):
               input[j],input[j+1] = input[j+1],input[j]
print(input)

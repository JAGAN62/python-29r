l = [[1,2,3,1,2],[4,5,6,3,2],[7,8,9,5,2]]
s = [[-1,0,2],[0,4,7],[-3,-4,-2]]
print(s)
# sum=0
# for i in l:
#     for j in i:
#         sum+=j
# print(sum)

# for i in l:
#     for j in i:
#         print(j,end=' ')
#     break

# for i in range(0,len(l)):
#     for j in range(0,len(l[i])):
#        if i==0 or i==1 or i==2:
#          print(l[i][j],end=' ')
#     print()
   
# sum=0
# for i in range(0,len(l)):
#     for j in range(0,len(l[i])):
#        if i==0 or i==(len(l)-1) or j==0 or j==(len(l[i])-1):
#          print(l[i][j],end=' ')
#          sum+=l[i][j]
#        else:
#           print(' ',end=' ')
          
#     print()
# print('boundary sum :',sum)        


# diagonal =0 
# d =0
# all =0     
# for i in range(len(s)):
#    for j in range(len(s[i])):
#       if i==j:
#          diagonal+=s[i][j]
#       if i+j == len(s)-1:
#          d+=s[i][j]
#       if i==j or i+j == len(s)-1:
#          all+=s[i][j]
         

# print(diagonal)
# print(d)
# print(all)
        
t =  [[-1,0,2],[0,4,7],[-3,-4,-2]]

for i in range(len(s)):
   for j in range(len(s[i])):
      if i <= j:
         t[i][j],t[j][i]=t[j][i],t[i][j]
print(t)
   
    
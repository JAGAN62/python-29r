# n = 15
# c = 1
# for i in range(1,6):
#    for j in range(1,i+1):
#       print(c,end=' ')
#       c+=1
#    print()
# n=5
# for i in range(n):
#     for j in range(1,n-i):
#         print(" ",end= '')
#     for k in range(n):
#         if i >= k:
#            print("*",end=" ")
#     print()
# for i in range(n,0,-2):
#     for j in range(1,n-i):
#         print(" ",end= '')
#     for k in range(n):
#         if i >= k:
#            print("*",end=" ")
#     print()
    
n=5
# for i in range(n):
#     for j in range(1,n-i):
#         print('',end=' ')
#     for k in range(n):
#         if k == 0 or i == n-1 or i==k:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#invert
for i in range(n,0,-1):
    for j in range(1,n-i):
        print('',end=' ')
    for k in range(n):
        if k == 0 or i == n-1 or i==k:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



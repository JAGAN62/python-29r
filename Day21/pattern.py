n = 5
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()
# print()

# #hollow square
# for i in range(n):
#     for j in range(n):
#         if i ==0 or j == 0 or i == n-1 or j == n-1:
#             print('*',end= " ")
#         else:
#             print(' ',end=' ')
#     print()
# print()

# #lower triangle
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print('*',end=' ')
#     print()
# print()

# #upper triangle
# for i in range(n):
#     for j in range(n):
#         if i <= j:
#             print('*',end=' ')
#         else:
#             print(' ',end= ' ')
#     print()
# print()

#pyramid
for i in range(n):
    for j in range(i):
            print('*',end=' ')
    print()
for i in range(n,1,-1):
    for j in range(i-1):
            print('*',end=' ')
    print()



#diagonal left diagonal
# for i in range(n):
#     for j in range(n):
#         if i==j  or i ==0 or j == 0 or i == n-1 or j == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()


#diagonal right diagonal
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1 or i ==0 or j == 0 or i == n-1 or j == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
#right and left diagonals
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j == n-1 or i ==0 or j == 0 or i == n-1 or j == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
#horizontal shiva
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j == n-1 or j == 0  or j == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#vertical shiva
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j == n-1 or i==0 or i == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()











#left diagoal i == j
#right diagonal i + j == n-1
#lower Triangle  i >= j
# upper riangle i <= j

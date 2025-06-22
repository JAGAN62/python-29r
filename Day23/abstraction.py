#abstraction classes
# from abc import ABC,abstractmethod
# class a(ABC)
n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ',end=' ')
#     for k in range(1,2*i):
#            print(i,end=' ')
#     print()
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    start = i+1
    reverse= False
    for k in range(i *2 + 1):
        print(start,end=" ")
        # print('*',end=" ")
        if start == 1:
            reverse = True
        start=start-1 if reverse==False else start+1
        # if not reverse:
        #     start-=1
        # else:
        #     start+=1

    print()
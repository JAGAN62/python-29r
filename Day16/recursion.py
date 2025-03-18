# def rec(n):
#     if n==1:
#         return 1
#     return n*rec(n-1)
# print(rec(5))

# def numbers(n):
#     if n==10:
#         return 10
#     print(n,numbers(n-1))
# numbers(10)

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(5))

# def exp(b,p):
#     if p==0:
#         return 1
#     return b * exp(b,p-1)
# print(exp(4,2))




# def sum(n):
#    if n==0:
#      return 0
#    return(n+sum(n-1))
# print(sum(10))


n=123
ans = 0
while n > 0:
   digit = n % 10
   ans = ans * 10 + digit
   n//=10
print(ans)

    
   


   
   

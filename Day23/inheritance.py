
#multilevel
# class User:
#     def a(self):
#         print('this is user')
#     def teach(self):
#         print('user is teacher')
# class Teacher(User):
#     def teach(self):
#         print('this is teacher')
# class Admin(Teacher):
#     # def teach(self):
#     #     print('admin is teacher')
#     pass
# ad1 = Admin()
# ad1.a()
# ad1.teach()

#multiple parents
# class Lion():
#     def roar(self):
#         print('roar')
#     def hunt(self):
#         print('lion hunt')
# class Tiger():
#     def hunt(self):
#         print('hunt')
#     def roar(self):
#         print('tiger roar')
# class Liger(Tiger,Lion):
#     # def hunt(self):
#     #     print('Liger hunting')
#     pass
# i=Liger()
# i.hunt()
# i.roar()

# #method reslution order
# print(Liger.mro())

#polymorphism
#operator overloading,method overriding,method overloading
# print((2).__add__(3))
# class poly:
#     def __init__(self,n_side):
#         self.side = n_side

#     def __add__(self,other):
#         return self.side + other.side
    
    
#     def __mul__(self,other):
#         return self.side - other.side
# p = poly(5)
# q = poly(6)
# print(p+q)#p.__add__(q)
# print(p*q)
# print(chr(100))
# print(ord('d'))
# print('\n')
# n , a ,b = 5,0,1
# for i in range(n):
#     for j in range(i+1):
#         print(a,end=' ')
#         a,b = b,a+b
#     print()

# #upper case alplabets
# n , char ,small = 5,65,97
# for i in range(n):
#     for j in range(i+1):
#         print(chr(char),end=' ')
#         char+=1
#     print()

# #lower case alphabets
# n ,small = 5,97
# for i in range(n):
#     for k in range(i+1):
#         print(chr(small),end=' ')
#         small+=1
#     print()


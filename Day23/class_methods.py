# class Polygon:
#     total = 0
#     def __init__(self,side):
#         self.side= side
#         Polygon.total+=1
#         print('polygon is created')
#     def area(self):
#         print('area',self.side ** 2)

#     def change(self,new_sides):
#         self.sides = new_sides
#         print('number of sides',self.sides)

#     @classmethod
#     def reset(cls):
#         cls.total = 0
#         print('zero')
#     @staticmethod
#     def info():
#         print('this is a polygon with n sides')

# p1 = Polygon(2)
# p2 = Polygon(3)
# print(Polygon.total)
# Polygon.reset()
# Polygon.info()
# p2.change(3)
# p1.area()


# #constructer called
# class A:
#     def __init__(self,name1,age1):
#         self.name = name1
#         self.age = age1
#         print('constructer of class A')
# class B(A):
#     def __init__(self,name1,age1):
#         super().__init__(name1,age1)
#         print('constructer of class B',self.name,self.age)
# t = B('a','c')

#patterns




# s =  "abcabcbb"
# sub = []
# uniq = []


# l=0

# def long(s):
#     global l
    
   
   
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             sub.append(s[i:j+1])
#             if len(s[i:j+1]) == len(set(s[i:j+1])):
#                 uniq.append(s[i:j+1])
   
#     for i in uniq:
        
#         if len(i) > l:
#             l= len(i)
#     return l

    
        
        
            
# long(s)
# print(sub)
# print(uniq)
# print(l)




# sets=set( "pwwkew")
# for i in s:
#     if i in sets and i not in sub:
#         print(i)
#         sub.append(i)
# print(sub)





l = [1,2,2,9]
d=[]
sol=[]
for i in l:
    s=i+1
    if i < 9:
        if i == l[(len(l)-1)]:
           l[(len(l)-1)]+=1
           break
   
    elif  i >= 9:
        if i == l[(len(l)-1)]:
           
            # l.delete(len(l)-1)
           
            while s >0:
                
                  r=s%10
                
                  
                  l.append(r)
                  s=s//10
        break


    
        # d.extend(sol[::-1])
        # l[(len(l)-1)]=d
                  
         
print(l)
print(sol)
print(d)
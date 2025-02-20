
print('1) Data types')
print()
print('{0} is an int Datatype'.format(62))
print('{0} is a string Datatype'.format('hello'))
print('{0} is a float Datatype'.format(6.2))
print('{0} is a complex Datatype'.format(6+2j))
print('{0} is a boolean Datatype'.format(True))
print(f'{[1,2,3,4,5]} is {type([1,2,3,4,5])} Datatype')
print(f'{(1,2,3,4,5)} is {type((1,2,3,4,5))} Datatype')
print(f'{{1,2,3,4,5}} is {type({1,2,3,4,5})} Datatype')
print(f"{{1:'aa',2:'bb',3:'cc'}} is {type({1:'aa',2:'bb',3:'cc'})} Datatype")
print(f'{range(5)} is a {type(range(5))}')
print()


print('2) Arthmetic Operators:')
print()
print('12 + 5 = ',12 + 5)
print('12 - 5 = ',12 - 5)
print('12 * 5 = ',12 * 5)
print('12 / 4 = ',12 / 4)
print('22 % 3 = ',22 % 3)
print('2 ** 3 = ',2 ** 3)
print('7 // 3 = ',7 // 3)
print()

print('3) Assignment Operators:')
print()
print('a=10')
a=10
print('a += 5 = ',15)
print('a -= 5 = ',5)
print('a *= 5 = ',50)
print('a /= 4 = ',2.5)
print('a %= 3 = ',1)
print('a **= 3 = ',1000)
print('a //= 3 = ',3)
print()

print('4) Comparison Operators')
print()
print('4 == 5 is',4 ==5)
print('4 != 5 is',4 !=5)
print('4 > 5 is',4 > 5)
print('4 < 5 is',4 < 5)
print('4 >= 5 is',4 >=5)
print('4 <= 5 is',4 <=5)
print()

print('5) Logical Operators')
print()
print('4 > 3 and 5 < 10 is ',4 > 3 and 5 < 10)
print('2 > 2 or 3 <4 is ',2 > 2 or 3 <4)
print('not(9 > 3 and 9 < 10) is ',not(9 > 3 and 9 < 10))
print()

print('6) Bitwise Operators')
print()
print('10 & 3 is ',10 & 3)
print( '85 | 4 is ',85 | 4)
print('5 ^ 79 is ',5 ^ 79)
print('~59 is ',~59)
print('3 << 7 is ',3 << 7)
print('6 >>5 is ',6 >> 5)
print()

print('7) If statement')
if(10 > 5):
    print('10 is greater than 5')
print()

print('8) IF else statement')
if(10 > 5):
    print("10 is greater than 5")
else:
    print('10 is lessthan 5 ')
print()

print('8) if elseif statement')
if(5 == 4):
    print('equal')
elif(5 > 4):
    print('greater')
else:
    print('lesser')
print()

print('9) for loop')
ans = ''
for i in range(len('jagan')):
    ans='jagan'[i] + ans
print(ans)
print()

print('10) while loop')
a = 0
while a<=5:
    print("*"," ",end=" ")
    a=a+1
print()

print('11) Break')
for i in range(1, 10):
    if i == 6:
        break
    print(i," ",end="")
    print()
print()

print('12) continue')
for i in range(1, 15):
    if i == 10:
        continue
    print(i," ",end='')
    print()
print()

print('13) pass')
for i in "python":
    if i == 't':
        pass
    else:
        print(i)
        print()

print()
print('14) Functions')
def a(a,b):
    return a ** b
print(a(2,3))




   

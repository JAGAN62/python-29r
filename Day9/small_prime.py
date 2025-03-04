#Programme to print the sum of odd digits in a number
print('"sum of odd numbers in a numbers"')
try:
    t=int(input('Enter a number: '))
except(ValueError):
    print('Enter numbers only')
else:
    sum = 0
    while t > 0:
        rem = t % 10
        if rem % 2 == 1:
            sum = sum+rem
        t=t//10
    print(sum)

#a program that finds the smallest prime digit (2, 3, 5, or 7) in a given number.
print('finds the smallest prime digit in a security PIN')
try:
 length = int(input('Enter a length of PIN:\n'))
except(ValueError):
  print('Enter a valid numberd PIN')
else:
 def check_small_prime(para):
    pin = []
    for i in range(para):
        pin.append(int(input('enter pin:')))
    listed = []
    for i in pin:
       if is_prime(i):
          listed.append(i)
    if not listed:
      print('Your password is weak, as it does not contain at least one prime number.')
    else:
        min_prime = listed[0]
        for i in range(len(listed)):
         if min_prime > listed[i]:
            min_prime = listed[i]
        print(f'your password contains least prime number {min_prime}: , your password is strong')
     
 def is_prime(num):
  if num <= 1:
    return False
  for i in range(2,num):
    if num % i == 0:
      return False
  return True
check_small_prime(length)
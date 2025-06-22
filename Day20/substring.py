#to find substring in string ,print substring of first index
s = 'takeuforwardfor'
sub = 'for'
flag = False
for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if sub == s[i:j]:
                print(i)
                flag = True
                break
        if flag == True:
             break
# for i in range(len(s)):
#     if sub == s[i: i+len(sub)]:
#          print(i)
#          break
    

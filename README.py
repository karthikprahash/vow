#vow
x=input('enter the letter')
print(x)
import string
a=list(string.ascii_lowercase)
s=('a','e','i','o','u')
if x in s:
    print('vowel')
elif x in a :
    print('consonent')
else:
    print('invalid input')





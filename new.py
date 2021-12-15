import string

a = "String12"

print(a.endswith("#"))

n = "9841523523"
#
# for i in range(10):
#     print( str(i) in a)

num1 = "984123232"
print(a.isalnum())
print(n.isdigit())
email = "abc@gmail.co.np"

uname, rest = email.split('@')[0], email.split('@')[1]
co = ''
if len(rest.split('.')) ==2 :
    domain, com = rest.split('.')
else:
    domain, com, co = rest.split('.')

print(uname, domain, com,co)

import email
print(help(email))
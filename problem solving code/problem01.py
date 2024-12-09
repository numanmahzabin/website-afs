# problem: Caesar Cipher
shift = int(input())
s = input()
result = ''
for i in s:
    if i.islower():
        order = (ord(i) - 96) - shift
        if order < 1:
            order = 26 + order
        result += chr(96 + order)
    elif i.isupper():
        order = (ord(i) - 64) - shift
        if order < 1:
            order = 26 + order
        result += chr(64 + order)
    else:
        result += i
        
print(result)
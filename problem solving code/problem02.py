# problem: Is Anagram
a = input()
b = input()


if len(a) != len(b):
    print('No')
else:
    if sorted(a) == sorted(b):
        print('Yes')
    else:
        print('No')
        
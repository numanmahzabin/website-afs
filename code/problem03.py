# problem: N-th Prime
''' 
I faced CPU Limit Exceeded for this problem. couldn't make it more efficient
'''

def g(a):
    b = [True] * (a + 1)
    c = 2
    while c * c <= a:
        if b[c]:
            j = c * c
            while j <= a:
                b[j] = False
                j += c
        c += 1
    
    primes = []
    n = 2
    while n <= a:
        if b[n]:
            primes.append(n)
        n += 1
    
    return primes

def f(n):
    import math
    if n == 1:
        return 2
    else:
        a = int(n * math.log(n * math.log(n)))
        if n <= 5:
            a = 15

    while True:
        t = g(a)
        if len(t) >= n:
            return t[n - 1]
        else:
            a *= 2

x = int(input())
print(f(x))

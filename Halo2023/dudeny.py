def sumdig(s):
    sm = 0
    for i in s:
        sm += int(i)
    return sm

def rnd(n, d = 0.0001):
    if abs(n - round(n)) < d:
        return round(n)

for i in range(1, 20000):
    if sumdig(str(i)) == rnd(i**(1/3)):
        print(i)

import sys

n, r, c = map(int, sys.stdin.readline().split(' '))

x = 0
y = 0

result = 0

def z_find():
    global n, x, y, result
    if n == 0:
        return
    n -= 1
    if r < x + 2**n and c < y + 2**n:
        z_find()
    elif r < x + 2**n and c >= y + 2**n:
        y += 2**n
        result += 4**n
        z_find()
    elif r >= x + 2**n and c < y + 2**n:
        x += 2**n
        result += (4**n) * 2
        z_find()
    elif r >= x + 2**n and c >= y + 2**n:
        x += 2**n
        y += 2**n
        result += (4**n) * 3
        z_find()



z_find()

print(result)
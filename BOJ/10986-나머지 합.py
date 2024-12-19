import sys
m, n = map(int, sys.stdin.readline().split(' '))

prefix_sum = []
remainder = [ 0 for _ in range(n) ]

result = 0

check = True

temp = 0

numbers = list(map(int, sys.stdin.readline().split(' ')))

for number in numbers:
    temp += number
    prefix_sum.append(temp)

for i in prefix_sum:
    remainder[i%n] += 1

for i in remainder:
    if check:
        check = False
        result += i*(i+1)/2
    else:
        result += (i-1)*i/2

print(int(result))

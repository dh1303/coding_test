import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split(' ')))
numbers.sort()

sp = 0
ep = 1

good = 0

for i in range(N):
    sp = 0
    ep = N - 1
    while sp < ep:
        if sp == i:
            sp += 1
            continue
        elif ep == i:
            ep -= 1
            continue

        if numbers[sp] + numbers[ep] < numbers[i]:
            sp += 1
        elif numbers[sp] + numbers[ep] > numbers[i]:
            ep -= 1
        else:
            print(numbers[sp], numbers[ep], numbers[i])
            good += 1
            break


print(good)
import sys

gear = []

for i in range(4):
    gear.append(sys.stdin.readline().strip())

point = [0, 0, 0, 0]

def one_reverse(i):
    if i == 1:
        return -1
    else: 
        return 1

def gear_spin(g, s, direction):
    if g > 0 and direction != 1 and gear[g][(point[g] + 6) % 8] != gear[g - 1][(point[g - 1] + 2) % 8]:
        gear_spin(g - 1, one_reverse(s), -1)
    if g < 3 and direction != -1 and gear[g][(point[g] + 2) % 8] != gear[g + 1][(point[g + 1] + 6) % 8]:
        gear_spin(g + 1, one_reverse(s), 1)
    point[g] += s
    if point[g] < 0:
        point[g] += 8

count = int(sys.stdin.readline().strip())

for i in range(count):
    gear_select, spin = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    gear_spin(gear_select - 1, one_reverse(spin), 0)

result = 0

for i in range(4):
    if gear[i][point[i] % 8] == '1':
        result += 2**i
    
print(result)


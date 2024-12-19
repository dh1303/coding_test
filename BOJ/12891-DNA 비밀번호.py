import sys

S, P = map(int, sys.stdin.readline().split(' '))

DNA_code = sys.stdin.readline().strip()

A, C, G, T = list(map(int, sys.stdin.readline().split(' ')))

sliding_window = DNA_code[0:P]

DNA_result = [0, 0, 0, 0]

result = 0

def DNA_check(DNA_str, count):
    global result
    for DNA_char in DNA_str:
        if DNA_char == 'A':
            DNA_result[0] += count
        elif DNA_char == 'C':
            DNA_result[1] += count
        elif DNA_char == 'G':
            DNA_result[2] += count
        elif DNA_char == 'T':
            DNA_result[3] += count
    if count == 1:
        if DNA_result[0] >= A and DNA_result[1] >= C and DNA_result[2] >= G and DNA_result[3] >= T:
            result += 1


DNA_check(sliding_window, 1)
            

for i in range(S-P):
    DNA_check(DNA_code[i], -1)
    DNA_check(DNA_code[i+P], 1)

print(result)

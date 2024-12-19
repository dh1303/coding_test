import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split(' ')))
numbers.sort()

start_index = 0
end_index = N - 1

result = 0

while start_index < end_index:
    if numbers[start_index] + numbers[end_index] > M:
        end_index -= 1
    elif numbers[start_index] + numbers[end_index] < M:
        start_index += 1
    else:
        start_index += 1
        end_index -= 1
        result += 1


print(result)
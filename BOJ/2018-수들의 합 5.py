import sys

N = int(sys.stdin.readline())

start_index = 0
end_index = 1

result = 0

temp = 0

prefix_sum = [(temp:=i+temp) for i in range(N)]

while end_index != len(prefix_sum):
    if prefix_sum[end_index] - prefix_sum[start_index] > N:
        start_index += 1
    elif prefix_sum[end_index] - prefix_sum[start_index] < N:
        end_index += 1
    else:
        result += 1
        end_index += 1
result += 1

print(result)
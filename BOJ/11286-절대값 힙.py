import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    value = int(sys.stdin.readline())

    if value == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(heap, (abs(value), value))
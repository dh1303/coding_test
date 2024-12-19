import sys
from collections import deque
from queue import PriorityQueue

N, L = map(int, sys.stdin.readline().split())

numbers = [ int(x) for x in sys.stdin.readline().split() ]

sliding_window = deque()

for end_idx in range(0, N):
    if end_idx > 0:
        if sliding_window[0][1] == end_idx - L:
            sliding_window.popleft()
        
        while sliding_window and sliding_window[-1][0] >= numbers[end_idx]:
            sliding_window.pop()
            
    sliding_window.append((numbers[end_idx], end_idx))

    print(sliding_window[0][0], end=' ')
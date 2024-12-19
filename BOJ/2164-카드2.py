import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque( i for i in range(1, N+1) )

for x in range(N-1):
    cards.popleft()
    if x != N-2:
        cards.append(cards.popleft())

print(cards[0])
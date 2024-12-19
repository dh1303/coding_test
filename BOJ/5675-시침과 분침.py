import sys

for i in sys.stdin.read().splitlines():
    print('N' if int(i) % 6 else 'Y')
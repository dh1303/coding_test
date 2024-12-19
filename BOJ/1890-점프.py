import sys

N = int(sys.stdin.readline())

game_map = [ [ int(i) for i in sys.stdin.readline().strip().split() ] for _ in range(N) ]

before_block = [[-1, -1]]

search_count = [[ -1 for _ in range(N)] for _ in range(N)]

x = 0
y = 0

result = 0

def research(x, y):
    while True:
        b_x, b_y = before_block[-1]
        if b_x == -1:
            return b_x, b_y
        if x != b_x:
            value = game_map[b_y][b_x]
            if b_y + value < N:
                x = b_x
                y = b_y + value
                return x, y
        x, y = before_block.pop()
            

while True:
    if x == -1:
        break
    jump_value = game_map[y][x]

    if x == N-1 and y == N-1:
        for block in before_block[2:]:
            b_x = block[0]
            b_y = block[1]
            search_count[b_y][b_x] += 1
        result += 1
    
    elif jump_value == 0:
        pass

    elif search_count[y][x] == -1:
        search_count[y][x] = 0
        
        if x + jump_value < N:
            before_block.append([x, y])
            x += jump_value
            continue
        
        elif y + jump_value < N:
            before_block.append([x, y])
            y += jump_value
            continue
    
    elif search_count[y][x] != 0:
        result += search_count[y][x]
        for block in before_block[2:]:
            b_x = block[0]
            b_y = block[1]
            search_count[b_y][b_x] += search_count[y][x]
            
    x, y = research(x, y)


print(result)
import sys
from itertools import combinations

def distance_check(x:tuple, y:list):
    result = []
    for house in y:
        result.append(abs(x[0] - house[0]) + abs(x[1] - house[1]))
    return result

    

m, n = map(lambda x: int(x), sys.stdin.readline().split(' '))

map_var = [[x for x in map(int, sys.stdin.readline().strip().split(' '))] for _ in range(m)]

house_location = []
chickens_location = []
chicken_distance = []
result = sys.maxsize



for x in range(m):
    for y in range(m):
        if map_var[x][y] == 1:
            house_location.append((x, y))
        elif map_var[x][y] == 2:
            chickens_location.append((x, y))


for chicken in chickens_location:
    chicken_distance.append(distance_check(x=chicken, y=house_location))


for comb in combinations(chicken_distance, n):
    temp_result = 0
    house_distances = [ [ comb[i][j] for i in range(len(comb)) ] for j in range(len(comb[0])) ]

    for house_distance in house_distances:
        temp_result += min(house_distance)
    
    if result > temp_result:
        result = temp_result
    

print(result)
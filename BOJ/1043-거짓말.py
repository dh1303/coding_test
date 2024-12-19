import sys

N, M = map(int, sys.stdin.readline().split(' '))

_, *true_people = map(int, sys.stdin.readline().split(' '))

party = []

searched_people = []

graph = [ [] for _ in range(N+1) ]

result = 0

for i in range(1, M+1):
    _, *people = map(int, sys.stdin.readline().split(' '))

    party.append(people)

    for target_human in people:
        for human in people:
            if target_human == human:
                continue
            if human not in graph[target_human]:
                graph[target_human].append(human)



for true_human in true_people:
    for target_human in graph[true_human]:
        if target_human not in true_people:
            true_people.append(target_human)


for p in party:
    check = True
    for true_human in true_people:
        if true_human in p:
            check = False
            break
    if check:
        result += 1



print(result)
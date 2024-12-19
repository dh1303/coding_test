import sys

test_case = int(sys.stdin.readline())

result = sys.maxsize

count = 0

avoid_duplication = [[test_case, sys.maxsize]]

def check(x:int):
    global count, result

    if x == 1 or result <= count:
        if result > count:
            result = count
        return 0

    duplication_check = 0

    for value in range(len(avoid_duplication)):
        if avoid_duplication[value][0] == x:
            duplication_check = 1
            if avoid_duplication[value][1] > count:
                avoid_duplication[value] = [x, count]
                break
            else:
                return 0
    
    if duplication_check == 0:
        avoid_duplication.append([x, count])
    
    if x % 3 == 0:
        count = count + 1
        check(x / 3)
        count = count - 1

    if x % 2 == 0:
        count = count + 1
        check(x / 2)
        count = count - 1

    count = count + 1
    check(x - 1)
    count = count - 1



check(test_case)

print(result)
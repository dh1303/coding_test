import sys

numbers = [ list(map(int, sys.stdin.readline().split(' '))) for _ in range(3) ]

goal_sum = 0

diagonal1 = [numbers[0][0], numbers[1][1], numbers[2][2]]
diagonal2 = [numbers[0][2], numbers[1][1], numbers[2][0]]

if diagonal1 == [0, 0, 0] or diagonal2 == [0, 0, 0]:
    zeroline_sums = [0, 0, 0]
    for idx, numberlist in enumerate(numbers):
        zeroline_sums[idx] = sum(numberlist)
    
    max_sum = max(zeroline_sums)
        
    for idx, numberlist in enumerate(numbers):
        zeroline_sums[idx] = max_sum - zeroline_sums[idx]
    
    for idx, numberlist in enumerate(numbers):
        numberlist[numberlist.index(0)] = int(zeroline_sums[idx] + (max_sum - sum(zeroline_sums)) / 2)

else:
    for idx1, number1 in enumerate(numbers):
        check = [True, True]
        for idx2, number2 in enumerate(number1):
            if number2 == 0:
                check[0] = False
            if numbers[idx2][idx1] == 0:
                check[1] = False
        
        if check[0] or check[1] == True:
            goal_sum = max(sum(number1), sum([numbers[0][idx1], numbers[1][idx1], numbers[2][idx1]]))
            break
    
    if not goal_sum:
        if 0 not in diagonal1:
            goal_sum = sum(diagonal1)
        elif 0 not in diagonal2:
            goal_sum = sum(diagonal2)
    

    for numberlist in numbers:
        if numberlist.count(0) == 1:
            value = goal_sum - sum(numberlist)
            numberlist[numberlist.index(0)] = value
    

    for i in range(3):
        numberlist = numbers[0][i], numbers[1][i], numbers[2][i]
        if numberlist.count(0) == 1:
            value = goal_sum - sum(numberlist)
            numbers[numberlist.index(0)][i] = value

        


for numberlist in numbers:
    for number in numberlist:
        print(number, end=" ")
    print()
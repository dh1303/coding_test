import sys

grade_table = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

score_sum = 0
grade_sum = 0

for _ in range(20):
    input_str = sys.stdin.readline().strip().split(' ')

    score = float(input_str[1])
    grade = input_str[2]

    if grade != 'P':
        grade_score = grade_table[grade]
        grade_sum += score * grade_score
        score_sum += score



print(grade_sum / score_sum)



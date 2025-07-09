'''
#1: Climbing Stairs
You can climb either 1 or 2 steps at a time. Given n steps, how many distinct ways can you climb to the top?

Input: n = 5
Output: 8
Explanation: (1,1,1,1,1), (1,2,1,1), (2,1,1,1), (1,1,2,1), etc.

Input: n = 2
Expected Output: 2
Explanation: [1,1], [2]

Input: n = 3
Expected Output: 3
Explanation: [1,1,1], [1,2], [2,1]

Input: n = 4
Expected Output: 5
Explanation: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]

Input: n = 5
Expected Output: 8

Input: n = 10
Expected Output: 89

Input: n = 45
Expected Output: 1836311903

solution logic:
total steps 0: possible ways 0
total steps 1: possible ways (1)
total steps 2: possible ways (1,1) (2)
total steps 3: possible ways (1,1,1) (1,2) (2,1)
total steps 4: possibe ways (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2)
total steps 5: possibe ways (1,1,1,1,1) (1,1,1,2) (1,1,2,1) (1,2,1,1) (2,1,1,1) (2,2,1) (2,1,2) (1,2,2)
see the series: 1,2,3,5,8 ----> fibbonoci series
'''

def find_distinct_ways(total_steps):
    if total_steps <= 0:
        return 0
    base_point = 0
    starting_step = 1
    calculating_steps = [base_point,starting_step]
    for step in range(1,total_steps+1):
        calculating_steps.append(calculating_steps[step]+calculating_steps[step-1])
    return calculating_steps[-1]

n = -10
answer = find_distinct_ways(n)
print(answer)
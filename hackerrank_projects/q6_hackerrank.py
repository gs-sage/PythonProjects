"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n.
The second line contains an array A[] of n integers each separated by a space.

Constraints

2
≤
𝑛
≤
10
2≤n≤10

−
100
≤
𝐴
[
𝑖
]
≤
100
−100≤A[i]≤100

Output Format

Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Explanation 0

Given list is [2, 3, 6, 6, 5].
The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score.
"""

n_list = [11,11,14,14,13]

n_list.sort()

print(n_list)

highest_value = 0
second_high_value = 0

for i in range(len(n_list)):
    if(n_list[i] > highest_value):
        highest_value = n_list[i]

n_list.remove(highest_value)

print(n_list)

for j in range(len(n_list)):
    if(n_list[j] > second_high_value and n_list[j] != highest_value):
        second_high_value = n_list[j]

print(f"The second highest value is {second_high_value}")

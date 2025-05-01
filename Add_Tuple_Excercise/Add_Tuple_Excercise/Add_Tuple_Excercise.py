#Add Tuple Exercise Solution
def Summation(n1, n2, sum_result):
    for i in range(2):
        for j in range(3):
         sum_result[i][j] = n1[i][j] + n2[i][j]
n1 = ((1, 2, 3), (4, 5, 6))
n2 = ((10, 20, 30), (40, 50, 60))
sum_result = [[0, 0, 0], [0, 0, 0]]
Summation(n1, n2, sum_result)
print("Summation result:", sum_result)


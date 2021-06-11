# import copy
# import sys
# input = sys.stdin.readline
# import numpy as np


tateretu, yokoretu = map(int, input().split())
question = [list(map(int, input().split())) for i in range(tateretu)]
# gyouretu = np.arange(tateretu * yokoretu).reshape((tateretu,yokoretu))
gyouretu = [[0]*yokoretu for i in range(tateretu)]

sum = gyouretu[:]

sumTate = [0]*yokoretu
sumYoko = [0]*tateretu


for i in range(yokoretu):
    for j in range(tateretu):
        sumTate[i] += question[j][i]
        sumYoko[j] += question[j][i]
    # sum[j][i] = sumYoko[j] + sumTate[i] - question[j][i]

# for i in range(yokoretu):
#     for j in range(tateretu):
#         sumYoko[j] += question[j][i]


for i in range(yokoretu):
    for j in range(tateretu):
        # sum[i,j] = sumYoko[i] + sumTate[j] - question[i][j]
        sum[j][i] = sumYoko[j] + sumTate[i] - question[j][i]

for i in range(tateretu):
    print(' '.join(map(str, sum[i])))
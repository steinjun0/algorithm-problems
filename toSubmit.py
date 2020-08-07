'''
200803 18:42 ~ 19:02, 20:06 ~ 20:38,(20:38 문제 잘못 읽은걸 깨달음)
N은 행의 개수
M은 열의 개수
N, M < 50
'''

import sys
from sys import stdin, stdout

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
ramps = []

for i in range(N):
    ramps.append(list(map(int, sys.stdin.readline().rstrip())))

K = int(sys.stdin.readline().rstrip())

row_sums = [M for i in range(N)]

for i in range(N):
    for j in range(M):
        row_sums[i] -= int(ramps[i][j])
    
row_sums.sort()



categroized_rows = []
temp_zeros = []
temp_searched_col = []


def make_group(uncategorized_list, searched_col):
    global ramps
    global categroized_rows
    global temp_zeros

    zeros = []
    ones = []

    
    for row_number in uncategorized_list:
        if int(ramps[row_number][searched_col]) == 1:
            ones.append(row_number)
        elif int(ramps[row_number][searched_col]) == 0:
            zeros.append(row_number)
    
    if searched_col+1 == M:
        if len(ones) > 1:
            categroized_rows.append(ones)

        if len(zeros) > 1:
            categroized_rows.append(zeros)

    elif searched_col+1 < M:
        if len(ones) > 1:
            if len(ones) > 1:
                temp_zeros.append(zeros)
                temp_searched_col.append(searched_col)
                make_group(ones, searched_col + 1)
                
            if len(temp_zeros) > 0:
                zeros = temp_zeros.pop()
                searched_col = temp_searched_col.pop()

            if len(zeros) > 1:
                make_group(zeros, searched_col + 1)
        elif len(zeros) > 1:
            if len(zeros) > 1:
                make_group(zeros, searched_col + 1)
    

make_group([i for i in range(N)], 0)


length_categorized_rows = []

for i in categroized_rows:
    length_categorized_rows.append(len(i))

length_categorized_rows.sort()


if len(length_categorized_rows) > 0:
    if length_categorized_rows[0] > row_sums[0]:
        print(length_categorized_rows[0])
    else:
        print(row_sums[0])

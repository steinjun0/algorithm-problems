'''
200803 18:42 ~ 19:02, 20:06 ~ 20:38,(20:38 문제 잘못 읽은걸 깨달음)
23:19 => 포기. 딕셔너리를 좀 더 연습해서 오든지, 알고리즘을 좀 더 연습해서 오든지
실패(3시간 33분 소모)

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

if K == 0:
    exit()

# print(ramps)

# row_sums = {1:0}
# row_sums = {0 for i in range(N)}

row_sums = [M for i in range(N)]

for i in range(N):
    # row_sums[i] = M
    for j in range(M):
        row_sums[i] -= int(ramps[i][j])
    

print("row_sums: "+str(row_sums)) 


'''
K_sum = 0
count = 0
for i in row_sums:
    if K_sum + i > K:
        print(count)
        break

    elif K_sum + i < K:
        K_sum += i
        count += 1
    
    elif K_sum + i == K:
        K_sum += i
        count += 1
        print(count)
        break
'''

categroized_rows = []
temp_zeros = []
temp_searched_col = []

count = 0
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
    

row_sums.sort()


make_group([i for i in range(N)], 0)

print("categorized_rows: "+str(categroized_rows))

length_categorized_rows = []

if len(categroized_rows) > 0:
    for i in categroized_rows:
        length_categorized_rows.append(len(i))

    length_categorized_rows.sort()



print("length_categorized_rows:"+str(length_categorized_rows))
if len(length_categorized_rows) > 0:
    if length_categorized_rows[0] > row_sums[0]:
        print("length_categorized_rows[0]: "+str(length_categorized_rows[0]))
        min = length_categorized_rows[0]

    else:
        print("row_sums[0]: "+str(row_sums[0]))
        min = row_sums[0]

        if min <= K:
            print(K)
        else:
            print(0)

else:
    print("row_sums[0]: "+str(row_sums[0]))
    min = row_sums[0]

    if min <= K:
        print(K)
    else:
        print(0)
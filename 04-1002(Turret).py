'''
200804 15:08 ~ 15:41(takes 33min)

1002 Turret

T 테스트 케이스
x1, y1, r1, x2, y2, r2
'''
import math
import sys
from sys import stdin, stdout


def getDistance(x1, y1, x2, y2):
    return(math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)))


T = int(sys.stdin.readline().rstrip())
Cases = []

for i in range(T):
    Cases.append(list(map(int,sys.stdin.readline().rstrip().split())))

result = []

for i in Cases:
    distance = getDistance(i[0], i[1], i[3], i[4])

    # if 하나가 포함될 때
    if(distance<i[2] or distance<i[5]):
        if distance > abs(i[5]-i[2]):
            result.append(2)
        elif distance == abs(i[5]-i[2]):
            if i[0] == i[3] and i[1] == i[4]:
                result.append(-1)
                continue
            result.append(1)
        elif distance < abs(i[5]-i[2]):
            result.append(0)
    # else 중심이 서로 바깥에 있을 때

    else:
        if distance > (i[2]+i[5]):
            result.append(0)
        elif distance == (i[2]+i[5]):
            result.append(1)
        elif distance < (i[2]+i[5]):
            result.append(2)

for i in result:
    print(i)
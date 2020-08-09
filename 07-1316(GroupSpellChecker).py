# 200809 20:52 ~ 21:11 (takes 19 mins)

# 1. 반복되는 글자가 없다. -> 그룹단어
# 2. 반복되는 글자가 있다.
#       3. 반복되는 글자가 모두 연속한다. -> 그룹 단어
#       4. 반복되는 글자가 하나라도 연속하지 않는다. -> 그룹단어 아님

# O(n^2) 이지만 단어의 길이가 100 이하여서 그대로 진행하였음
# 무식하게 단순비교로 진행하니 연산속도는 느리지만 코딩속도는 아주 빨랐음(코드도 간결)
# 
# 순위권 코드
# ... ??????
# cnt=0;exec('l=input();cnt+=[*l]==sorted(l, key=l.find);'*int(input()));print(cnt)
'''
cnt=0
exec('
        l=input();
        cnt+=[*l]==sorted(l, key=l.find);' * int(input()))
print(cnt)
'''

import sys
from sys import stdin, stdout

N = int(sys.stdin.readline().rstrip())

words = []
count = 0

for i in range(N):
    input = sys.stdin.readline().rstrip()
    if len(input) == len(set(input)):
        count += 1
        continue
    words.append(input)


for word in words:
    cnt_flag = True

    for i, spell in enumerate(word):
        flag = -1
        for j, compare in enumerate(word[i:]):
            if spell == compare and flag == -1:
                flag = j

            elif spell == compare and flag == j-1:
                flag = j

            elif spell == compare and flag < j-1:
                cnt_flag = False
                break
            
        if cnt_flag == False:
            break
    if cnt_flag == True:
        count += 1

print(count)
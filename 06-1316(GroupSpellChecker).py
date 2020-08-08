# 200808 11:15
# 11:57(after 42 mins) 문제 잘못 이해한걸 깨달음
# 
# 0. 단어 내에 중복되는 글자가 없다 -> 단어가 그룹단어 1개
# 1. 연속하는 글자를 묶는다.
# 2. 단어 내에 중복되는 글자가 있다
#       3. 중복글자가 모두 연속한다면 1개로 취급한다
#       4. 중복글자가 연속하지 않는다면 중복글자를 기준으로 단어를 분리한다.
#       
# 12:05 네트워크 문제 중단 13:02 재개
# 13:21 포기(리스트로 하다가 너무 꼬임)
# takes 68 mins, 내일 문자열 자료형으로 다시 도전

import sys
from sys import stdin, stdout

N = int(sys.stdin.readline().rstrip())

words = []

count = 0

temp = []
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    if len(list(set(temp))) == len(temp):
        count += 1
        continue
    words.append(temp)

print(words)

seperate_words = []
word_set = set()
word_list = []



for i in words:
    before = '0'
    continue_count = 0
    seperate_word = []
    temp = ""
    flag = True

    for j in i:
        for k in word_list:
            if continue_count == 0 and k == j:
                flag = False
        if before == '0':
            seperate_word.append(j)
            before = j
            continue
        
        elif j == before:
            if continue_count == 0:
                temp.append(seperate_word.pop())
            continue_count += 1
            temp.append(j)
            word_set.add(j)
            before = j
            continue

        elif continue_count > 0 and j != before:
            seperate_word.append(temp)
            word_list.append(before)
            temp = ""
            continue_count = 0
            before = j
            seperate_word.append(j)
            continue

        seperate_word.append(j)
        before = j
    
    if len(temp) != 0:
        seperate_word.append(temp)
        temp = []


    seperate_words.append(seperate_word)

print(seperate_words)

for i in seperate_words:
    p = set(i)
    if len(list(set(i))) == len(i):
        count += 1
    

print(count)
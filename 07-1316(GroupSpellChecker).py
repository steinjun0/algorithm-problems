# 200809 20:52 ~ 21:11 (takes 19 mins) 문제 풀기(어제 풀다 실패한)
# 200809 21:11 ~ 22:16 (takes 65 mins) 순위권 코드 공부

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

# 덜 매운 맛
'''
cnt = 0
for i in range(int(input())):
    word = input()
    cnt += list(word) == sorted(word, key=word.find)
print(cnt)

출처: https://leedakyeong.tistory.com/entry/백준-1316번-그룹-단어-체커-in-python [슈퍼짱짱]

'''

# 여기서 배울 수 있는 코드
# 1. 
#       for i in range(int(input())):
#   이런 식으로 첫 줄 N번 반복은 한 줄로 처리 가능하다
#
# 2. 
#       cnt += list(word) == sorted(word, key=word.find)
#   조건문을 우변에 놓을 수 있다.
#
# 3. 
#       cnt += list(word) == sorted(word, key=word.find)
#   sorted(list)는 원본 list를 변경하지 않으면서 sorting된 list를 반환한다.
#       *String을 sorted하면 list가 된다
#
# 4.
#       cnt += list(word) == sorted(word, key=word.find)
#           Python 은 True는 [0 이외의 숫자], False는 [0] 이다
#           True를 대수 연산하면 1로 취급한다.
#           False를 대수 연산하면 0으로 취급한다.
#               C랑 같다!! (C도 음수를 1로 취급했나?)
#
# 5.
#       cnt += list(word) == sorted(word, key=word.find)
#   sorted 또는 sort(list 한정) 는 key를 가지고 정렬할 수 있다.
#   *** 여기서 사용된 find는 str만 가지고 있는 함수여서 list에는 적용이 불가능 하다.
#   *** sorted(str, key=str.find)
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

'''

a = [1,2,3,4]
b = [1,2,3,4]
c = [4,3,2,1]
d = sorted(c)
#f = sorted(c, key=c.find)

print("a",a)
print("b",b)
print("c",c)
print("d",d)
#print("e",e)

print("a==b " , a==b)
print("a==c " , a==c)
print("a==d " , a==d)
#print("a==e " , a==e)
#print("a==f " + a==f)

# c.sort() 
#   c를 정렬한다(c자체가 변경)
# d = sorted(c)
#   d에 정렬한 c를 넣는다

str1 = 'abcd'
str2 = 'abcd'
str3 = 'dcba'
str4 = sorted(str3)
str5 = sorted(str3, key=str3.find)
###### str6 = str1.sort() !!! sort()는 list만 가지고 있는 함수이다

print("str1",str1)
print("str2",str2)
print("str3",str3)
print("str4",str4)
print("str5",str5)

print("str1 == str1",str1 == str1)
print("str1 == str2",str1 == str2)
print("str1 == str3",str1 == str3)
print("str1 == str4",str1 == str4)
print("str1 == str5",str1 == str5)
print("str1 == ''.join(str4)",str1 == ''.join(str4))

count = 1
count += False*2
if -0:
    count += True

print(count)
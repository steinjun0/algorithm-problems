# 200807 20:23 ~ 20:59
# takes 00:36


# 1. "-"가 나오면 앞의 글자와 세트로 한 글자로 취급한다     X   -> O
# 2. "lj", "nj" 는 모두 한 글자로 취급한다                X   -> O

# 3. "="이 나오면 앞의 글자와 세트로 한 글자로 취급한다     X
# 4. "dz="은 한 글자로 취급한다                           X

import sys
from sys import stdin, stdout

input = sys.stdin.readline().rstrip()

length = len(input)
length = length - input.count('-') - input.count('lj') - input.count('nj')


index = -1
while True:
    index = input.find('=', index+1)

    if index == -1:
        break
    str_dz = input[index-2:index]
    if str_dz == "dz":
        length = length - 2
    else:
        length = length - 1

print(length)
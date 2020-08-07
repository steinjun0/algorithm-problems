# takes 00:46 mins

import math
import sys
from sys import stdin, stdout

N = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(N):
    numbers.append(sys.stdin.readline().rstrip())

#print(N)
#print(numbers)

k = math.ceil(math.log2(N))

numbers_k = []
numbers_k_set = []

len_nubmers = len(set(numbers))
for i in range(1,len(numbers[0])+1):
    numbers_k = []
    for j in range(N):
        numbers_k.append(numbers[:][j][-i:])

    #print(numbers_k)
    #print(len(set(numbers_k)))
    if len(set(numbers_k)) == len_nubmers:
        break

print(i)
print(len_nubmers)
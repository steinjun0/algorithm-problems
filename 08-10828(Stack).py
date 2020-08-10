# 08-10828 Stack [Silver 4]
# 200810 17:36~17:48
# 18:29 ~ 18:42
# 12+13 = takes 25 mins

import sys
from sys import stdin, stdout

class Stack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        try:
            print(self.stack.pop())
        except IndexError:
            print(-1)
        
    def size(self):
        print(len(self.stack))

    def empty(self):
        print(int(len(self.stack) == 0))

    def top(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print(-1)

stack = Stack()

input = []

for i in range(int(sys.stdin.readline().rstrip())):
    input.append(list(sys.stdin.readline().rstrip().split()))

for j in range(i+1):
    if input[j][0] == 'push':
        stack.push(input[j][1])
    elif input[j][0] == 'pop':
        stack.pop()
    elif input[j][0] == 'size':
        stack.size()
    elif input[j][0] == 'empty':
        stack.empty()
    elif input[j][0] == 'top':
        stack.top()
# 08-10828 Stack [Silver 4]
# 200810 17:36~17:48
# 18:29 ~ 18:42
# 12+13 = takes 25 mins


# 순위권 코드
'''
from sys import stdin

stack = []
next(stdin)                     # next(iterable) => iterable한 객체에서 인자 하나를 빼내는 메소드. 연속으로 쓰면 index를 늘리면서 출력된다
                                # 여기서는 N번 반복되는 횟수를 사용하지 않기에, 값을 버리기 위해 사용

for line in stdin:              # for line in stdin: => 이렇게 작성하면 한 줄씩 들어오는 입력을 받아서 line에 넣을 수 있다.
                                # stdin.readline() 을 하면 딱 한 번만 받지만 stdin은 게속해서 받고 ^Z를 입력받아야 멈춘다.
                                # 본 문제에서는 반복을 멈출 필요가 없어서 중단점을 없애고 계속 입력을 받는다
    command = line.split()      # 이 뒤는 나와 코드가 같다
    if command[0] == 'push':
        stack.append(command[1])

    ~~~~~~

    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
'''
# (위 코드는 입력과 출력이 혼재해서 출력되는데 그래도 통과는 되나보다)

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
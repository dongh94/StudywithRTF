import sys
sys.stdin = open("3190_뱀.txt")
input = sys.stdin.readline
from collections import deque
#우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
arr = [[0]*(N) for _ in range(N)]

# 사과의 위치
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = -1
# 방향 정보
orders = dict()
L = int(input())
for _ in range(L):
    i, s = input().split()
    orders[int(i)] = s

#방향 전환 함수
def Direct(d, k):
    if k == "D":
        d = (d + 1) % 4
        return d
    else:
        d = (d - 1) % 4
        return d

# 명령어
x = y = 0
arr[x][y] = 1
Q = deque([(x,y)])
d = 0
#움직이면서~ 방향체크해야하므로 if 방향정보
move = 0
while Q:
    #이동
    x += dr[d]
    y += dc[d]
    move += 1
    #벽 안 이면서~!
    if 0 <= x < N and 0 <= y < N and arr[x][y] != 1:
        #사과면 먹고 1로 남겨
        if arr[x][y] == -1:
            arr[x][y] = 1
            Q.append((x,y))
            # 방향 바꿔
            if orders.get(move):
                d = Direct(d, orders[move])
        #사과없으면 앞으로 전진 1, 꼬리 0 으로 바꿔!
        elif arr[x][y] == 0:
            arr[x][y] = 1
            Q.append((x,y))
            tx, ty = Q.popleft()
            arr[tx][ty] = 0
            if orders.get(move):
                d = Direct(d, orders[move])
    else:
        break
print(move)
# orders.get(1) = None 입니다.
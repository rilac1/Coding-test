import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
dice = range(1,7)

def move(x,y,n,d):
    nx, ny = x+dx[n], y+dy[n]
    if not 0<=nx<N or not 0<=ny<M:
        return d
    if graph[nx][ny] == 0:
        graph[nx][ny]

# 0 2 0
# 4 1 3
# 0 5 0
# 0 6 0

# 동쪽으로
# 1 3 6 4
# 북쪽으로
# 1 2 6 5

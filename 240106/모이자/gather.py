import sys
n = int(input())
houses = [*map(int, input().split())]

min_dist = sys.maxsize

for t in range(n):
    tmp = 0
    for f in range(n):
        tmp += abs(f-t) * houses[f]
    min_dist = min(tmp, min_dist)

print(min_dist)
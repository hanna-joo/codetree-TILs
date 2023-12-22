from collections import deque
q = deque([1, int(input())])
print(q[0], q[1], end=' ')
while q[-1] < 999:
    q.append(q[0]+q[1])
    q.popleft()
    print(q[-1], end=' ')
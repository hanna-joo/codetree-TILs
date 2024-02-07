"""
1. 문제
- 시간 소요 : 1초에 한 칸 이동
- 방향 전환 : 벽에 부딪히면 반대 방향으로 전환
- 구슬 삭제 : 이동 이후 한 칸에 구슬이 2개 이상인 경우
- return : T줄에 걸쳐 해당 테스트 케이스에 남아 있는 구슬의 수 출력

2. 입력 및 제한
- 테스트 케이스 개수 T (1<=T<=100)
- 각 테스트 케이스에 대한 정보
    - N, M (1<=N<=50, 0<=M<=N*N)
    - M개의 줄에 걸쳐 구슬 위치인 행, 열, 방향 (1<=x<=N, 1<=y<=N, d=[U,D,R,L])

3. 로직
- 반복 : 구슬 이동 -> 2개 이상인 칸은 구슬 없애기 -> 구슬 개수 세기 -> 종료 여부 확인
- 종료 조건
    - 구슬의 개수가 0 / 1개일 때 종료
    - 구슬이 제자리로 올 때까지 구슬 개수가 그대로면 종료 (2*N+2초 뒤)
"""

T = int(input())
command = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
change = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
for _ in range(T):
    N, M = map(int, input().split())
    ans = M
    balls_pos = []
    balls_cnt = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x), int(y)
        balls_pos.append([x, y, d])
        balls_cnt[x][y] += 1
    time, prev_total = 0, M
    while True:
        if time == 2 * N + 2:
            if prev_total == total:
                ans = total
                break
            time = 0
            prev_total = total

        tmp_pos = []
        for cx, cy, cd in balls_pos:
            nx, ny = cx + command[cd][0], cy + command[cd][1]
            # 다음 위치가 벽이라면 방향 전환
            if nx <= 0 or nx > N or ny <= 0 or ny > N:
                tmp_pos.append([cx, cy, change[cd]])
                continue
            # 구슬 이동
            balls_cnt[cx][cy] -= 1
            balls_cnt[nx][ny] += 1
            # 새로운 위치 저장
            tmp_pos.append([nx, ny, cd])
        # 구슬 개수 세기
        total = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                # 구슬 개수 2개 이상이면 구슬 삭제
                if balls_cnt[i][j] >= 2:
                    balls_cnt[i][j] = 0
                    # 저장해 둔 구슬 위치도 삭제
                    tmp_pos_2 = [k for i, k in enumerate(tmp_pos) if k[:2] != [i, j]]
                    tmp_pos = tmp_pos_2
                    continue
                total += balls_cnt[i][j]
        if total in [0, 1]:
            ans = total
            break
        balls_pos = tmp_pos
        time += 1
    print(ans)
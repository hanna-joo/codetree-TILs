# 세 수의 최대 곱
# keyword : 가능한 상황을 나열하기

'''
1. 문제
- 3개의 숫자를 적절하게 골라 나올 수 있는 곱의 최댓값

2. 해결1 -> 모든 상황을 나열한 것이 아님
- case1 : 모두 양수
- case2 : 2개 음수

3. 해결1 보완
- case1 : 최댓값 양수
    - 양수 3개 이상 > 뒤 3개
    - 양수 1개 + 음수 2개 > 뒤 1개 + 앞 2개
- case2 : 최댓값 음수일 때
    - 양수 0개 > 뒤 3개
- case3 : 최댓값 0일 때
    - 양수 0개, 0 1개 > 0 하나만 넣으면 됨
'''

n = int(input())
nums = sorted(map(int, input().split()))
case1 = nums[-1] * nums[-2] * nums[-3]
case2 = nums[0] * nums[1] * nums[-1]
print(max(case1, case2))
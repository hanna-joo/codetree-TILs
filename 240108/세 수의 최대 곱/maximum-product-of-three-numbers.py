# 3개의 숫자를 적절하게 골라 나올 수 있는 곱의 최댓값
'''
1. 해결 방법
- case1 : 모두 양수
- case2 : 2개 음수
'''

n = int(input())
nums = sorted(map(int, input().split()))
case1 = nums[-1] * nums[-2] * nums[-3]
case2 = nums[0] * nums[1] * nums[-1]
print(max(case1, case2))
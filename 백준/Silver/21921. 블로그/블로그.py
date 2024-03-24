import sys
input = sys.stdin.readline

n, x = list(map(int, input().rstrip().split())) #블로그 총 운영 날짜 n , 기간 x
nums = list(map(int, input().rstrip().split())) 

res = sum(nums[:x])
temp = res
days = 1
for i in range(x, n):
    temp -= nums[i - x]
    temp += nums[i]
    if res < temp:
        res = temp
        days = 1
    elif res == temp:
        days += 1

if res > 0:
    print(res)
    print(days)
else:
    print('SAD')
money = int(input())
num = int(input())
sum = 0
for i in range(num):
    price, cnt = map(int, input().split())
    sum+=(price*cnt)

if money ==sum:
    print("Yes")
else:
    print("No")
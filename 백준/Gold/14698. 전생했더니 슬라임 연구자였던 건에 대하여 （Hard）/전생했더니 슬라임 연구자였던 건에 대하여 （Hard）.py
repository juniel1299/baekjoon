import sys
import heapq # 우선순위 큐 쓰기 위해서 import 
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    slime = [*map(int, input().split())]
    heapq.heapify(slime)
    result = 1
    divide = 1000000007 # 최종 나눌 값 
    
    while len(slime) > 1: # 슬라임이 2개 이상 일 때만 가능하므로 . 
        s1 = heapq.heappop(slime) # 홀수 슬라임 
        s2 = heapq.heappop(slime) # 짝수 슬라임
        result *= s1 * s2 % divide # 에너지 값은 슬라임의 에너지의 곱을 계속 곱해줘야 하므로 result 값을 계속 갱신함.  -> 최종 에너지 값을 구해야 함 
        
        heapq.heappush(slime, s1*s2) # 슬라임 값은 둘의 곱이므로 그대로 push 하면 됨 . 
        
        
    print(result % divide) # 최종 출력은 에너지 값의 divide 값이다.  
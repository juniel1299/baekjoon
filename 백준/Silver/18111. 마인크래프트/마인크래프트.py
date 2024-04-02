import sys
input = sys.stdin.readline
 
h,w,box = map(int,input().split())
height_info = {n : 0 for n in range(257)}
 
arr = []
for i in range(h):
    temp = list(map(int,input().split()))
    arr.append(temp)
    for j in temp :
        height_info[j] += 1
 
height_info = list(height_info.items())
 
time_list = []
for i in range(257):
    under = [(key,val) for key,val in height_info if key < i and val!=0]
    over = [(key,val) for key,val in height_info if key > i and val!=0]
    time,block = 0,0
    block += box
    
    for height,count in over:
        time += 2*(height-i)*count
        block += (height-i)*count
    for height,count in under:
        time += (i-height)*count
        block -= (i-height)*count
 
    if block < 0:
        break
    time_list.append(time)
    
max_height_idx = [idx for idx,t in enumerate(time_list) if t == min(time_list)]
max_height = max(max_height_idx)
min_time = min(time_list)
 
print(min_time,max_height)
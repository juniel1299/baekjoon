num = int(input()) # 몇개 숫자 받을건지 
num_list = list(map(int,input().split())) # 리스트 생성
cnt = int(input()) # 찾을 숫자
print(num_list.count(cnt))
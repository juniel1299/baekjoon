import sys 
n, m = map(int, input().split()) # 영어 지문에 나오는 단어의 개수 , 외울 단어의 길이 기준 
note = dict() # 딕셔너리 사용 (자바로 치면 HashMap 이용 )
for _ in range(n): # 단어 개수만큼 반복문
    s = sys.stdin.readline().strip() # 단어 앞 뒤를 자르고 입력 받음 -> 외울 단어 기준은 1부터 세는데 파이썬은 0부터 세기 때문에 . 
    if len(s) >= m: # s의 길이가 외울 단어 길이 기준보다 같거나 크면 노트에 +1 추가됨 
        if s in note:
            note[s] += 1
        else:
            note[s] = 1
note = sorted(note.items(), key=lambda x: (-x[1],-len(x[0]),x[0])) #sorted 를 이용해 다중 조건 정렬 
for i in note:
    print(i[0])
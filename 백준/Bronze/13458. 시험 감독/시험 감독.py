def calculate_supervisors():
    # 입력 받기
    n = int(input())  # 시험장 개수
    applicants = list(map(int, input().split()))  # 각 시험장의 응시자 수
    b, c = map(int, input().split())  # 총감독관(B), 부감독관(C) 감시 가능 인원

    # 필요한 감독관 수
    total_supervisors = 0

    # 각 시험장에서 필요한 감독관 수 계산
    for a in applicants:
        # 1. 총감독관 배치
        total_supervisors += 1
        remaining = a - b

        # 2. 남은 인원 부감독관으로 감시
        if remaining > 0:
            total_supervisors += (remaining // c)
            if remaining % c > 0:
                total_supervisors += 1

    # 결과 출력
    print(total_supervisors)


# 실행
calculate_supervisors()
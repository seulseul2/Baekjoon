import sys
input = sys.stdin.readline

T = int(input())
for TC in range(T):
    N = int(input())
    result = N
    lst = []
    for i in range(N):
        resume, interview = map(int, input().split())
        lst.append([resume, interview])
    lst.sort()
    standard = lst[0]
    for applicant in lst[1:]:
        # 기준 변경
        if standard[1] > applicant[1]:
            standard = applicant
            continue
        # 면접점수도 낮은 경우
        result -= 1
    print(result)
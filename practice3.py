from collections import deque

T = int(input())
for TC in range(T):
    N, M = map(int, input().split())
    papers = deque(list(map(int, input().split())))
    cnt = 0
    while papers:
        maxV = max(papers)
        paper = papers.popleft()
        M -= 1

        # 만약 출력된 paper가 target이라면 M < 0 이라는 조건이 달성될 것입니다.
        if maxV == paper:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        # 그렇지 않은데 M이 0보다 작다면, 맨 뒤로 보낸 다음 다시 M을 배정해줄 필요가 있습니다.
        else:
            papers.append(paper)
            if M < 0:
                M = len(papers) - 1
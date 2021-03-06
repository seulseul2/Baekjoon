def merge(left, right):
    lp = rp = 0
    result = []
    while lp < len(left) and rp < len(right): # 둘 중 하나가 먼저 끝나니까!
        if left[lp] < right[rp]:
            result.append(left[lp]) # 두개중에 작은거를 result에 넣어두고 다음거 보러가기
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    # if lp<len(left): # 왼쪽이 남았으면
    while lp<len(left):
        result.append(left[lp])# 왼쪽 데이터를 result에 넣는다
        lp += 1

    # if rp<len(right): # 오른쪽이 남았으면
    while rp<len(right):# 오른쪽 데이터를 result에 넣는다
        result.append(right[rp])
        rp += 1
    
    return result

def mergeSort(lst):
    if len(lst) <= 1: # 빈 리스트가 있을 수 있기 때문에 <도 들어가야 함
        return lst

    #중간지점을 계산
    m = len(lst) // 2
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])
    result = merge(left, right)
    return result

lst = [69, 10, 30, 2, 16, 8, 31, 22]
result = mergeSort(lst)
print(result)
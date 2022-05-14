# 이분 탐색 - 입국심사

def binarySearch(arr, target, left, right):
    mid = (left+right)//2
    if target == arr[mid]:
        print('answer {}'.format(mid))
    elif arr[mid] > target:
        binarySearch(arr, target, left, mid-1)
    elif arr[mid] < target:
        binarySearch(arr, target, mid+1, right)
    else: 
        return False

def solution(n, times):
    answer = 0
    return answer
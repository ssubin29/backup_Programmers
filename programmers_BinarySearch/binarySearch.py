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
target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

print(m_list)
binarySearch(m_list,target,0,right)
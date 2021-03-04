#정수 삼각형

def triangle_sum(arr, i, n, count):
    tmp = arr[i-n]
    if(count==1):
        return

    if(arr[i] > arr[i-1]):
        arr[i-n] += arr[i]
    else:
        arr[i-n] += arr[i-1]
    count -= 1  

    triangle_sum(arr, i-1, n, count)


def solution(triangle):
    answer = 0
    size = len(triangle)
    arr = []
    for i in range(0, size):
        for j in range(0, len(triangle[i])):
            arr.append(triangle[i][j])
    idx = len(arr)-1

    for i in range(size, 0, -1): # 
        triangle_sum(arr, idx, i, i)

        idx -= i
    answer = arr[0]
    return answer
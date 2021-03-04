#등굣길

def solution(m, n, puddles):
    arr = []
    answer = 0
    for i in range(0, n):
        tmp = []
        for j in range(0,m):
            tmp.append(-1)
        arr.append(tmp)

    for i in puddles:
        arr[i[1]-1][i[0]-1] = 0
    
    arr[0][0]=1
    
    for i in range(0, n):
        for j in range(0, m):
            if(i==0 and j==0):
                continue
            if(arr[i][j]==0):
                continue

            if(i-1 < 0):
                up_value = 0
            else:
                up_value = arr[i-1][j]
            if(j-1<0):
                left_value = 0
            else:
                left_value = arr[i][j-1]
            arr[i][j] = left_value + up_value
    return arr[n-1][m-1] % 1000000007
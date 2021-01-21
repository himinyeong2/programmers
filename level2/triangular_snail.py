def snail(arr, num, dir,i, j): #전체 arr, 넣을 number[1,2,3,4,5], 방향 
    last_j_idx = j
    last_i_idx = i
    result = []

    if(dir=="right"):
        for x in range(0, len(num)):
            arr[i][j+1]=num[x]
            j+=1
            last_j_idx = j
    if(dir=="up"):
        for x in range(0, len(num)):
            arr[i-1][j]=num[x]
            i-=1
            last_i_idx = i
    if(dir=="down"):
        if(i==0 and j==0):
            for x in range(0, len(num)):
                arr[i][j]=num[x]
                last_i_idx = i
                i+=1
        else:
            j=j-len(num)
            for x in range(0, len(num)):
                arr[i+1][j] = num[x]
                i+=1
                last_i_idx = i
                last_j_idx = j
    result.append(last_i_idx)
    result.append(last_j_idx)
    return result

def solution(n):
    count=n
    number=1
    arr=[]
    num = []
    dir = []
    answer=[]
    result=[0,0]
    direction = ["down","right","up"]

    #넣을 데이터 
    for i in range(0,n):
        tmp = []
        for j in range(0,count):
            tmp.append(number)
            number+=1
        count-=1
        num.append(tmp)

    # 방향
    for i in range(0,n):
        dir.append(direction[i%3])

    for i in range(0,n):
        tmp=[]    
        for j in range(0,n):
            tmp.append(0)
        arr.append(tmp)    
        
    for i in range(0, n):
        result = snail(arr, num[i],dir[i],result[0],result[1])

    for i in arr:
        for j in i:
            if(j!=0):
                answer.append(j)    
    return answer  

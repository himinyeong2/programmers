def get_0_count(arr, row, size):
    count = 0
    for i in range(0, size):
        if(arr[row][i]==0):
            count+=1
    return count

def solution(m,v):

    # v = [2,3,1]
    answer=0
    count = 0
    board=[]

    for i in range(0,m):
        tmp=[]
        for j in range(0, m):
            tmp.append(0)
        board.append(tmp)

    for x in v:
        for i in range(0, m):
            count = get_0_count(board,i,m)
            if(count>= x):
                for j in range(0, x):
                    board[i][m-count+j]=1
                break
            else:
                continue
    for i in board:
        if(i[0]!=0):
            answer+=1  
    return answer

print(solution(4, [3,3,3,1]))
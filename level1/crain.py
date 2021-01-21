# 게임개발자인 죠르디는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
# 죠르디는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

# 0 0 0 0 0
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1
def solution(board, moves):
    answer = 0
    bucket = []

    for i in range(0, len(moves)):
        i_idx = -1
        j_idx = moves[i]-1
        tmp = -1
        for x in range(0, len(board[0])):
            if(j_idx==-1):
                break
            if(board[x][j_idx]!=0):
                i_idx = x
                tmp = board[i_idx][j_idx]
                board[i_idx][j_idx] = 0
                bucket.append(tmp)
                if(len(bucket)>=2):
                    if(bucket[len(bucket)-1]==bucket[len(bucket)-2]):
                        del(bucket[len(bucket)-1])
                        del(bucket[len(bucket)-1])
                        answer+=2
                break      
    return answer

(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4 ]))
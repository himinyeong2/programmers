# "CBD" 	["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    init_prev = -999
    init_next = 999
    
    for tree in skill_trees:
        chk = True
        for i in range(0, len(skill)-1):
            prev = init_prev
            next = init_next
            for j in range(0, len(tree)):
                if(skill[i]==tree[j]):
                    prev = j
                if(skill[i+1]==tree[j]):
                    next = j
                
            if( prev > next ) :
                chk = False
                break
            elif(prev == init_prev and next != init_next):
                chk = False
                break
            else:
                chk=True

        if(chk==True):
            answer += 1
    return answer

print(solution("CAD" ,["CAD"]))
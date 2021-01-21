
#pass
def solution(s):
    answer = ''
    tmp = ''
    cnt = 0
    word = []
    
    for i in range(0,len(s)):
        if(s[i]!= " "):
            tmp += s[i]
        else:
            word.append(tmp)
            cnt += 1
            tmp = ''
    
    word.append(tmp)
    for i in range(0, len(word)):
        for j in range(0, len(word[i])):
            if(j%2==0):
                answer += word[i][j].upper()
            else:
                answer += word[i][j].lower()
        
        if(i != len(word)-1):
            answer += " "
    return answer

# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

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
            if(j==0):
                answer+=word[i][j].upper()
            else:
                answer+=word[i][j].lower()
        if(i != len(word)-1):
            answer += " "

    return answer

print(solution("test~^^"))
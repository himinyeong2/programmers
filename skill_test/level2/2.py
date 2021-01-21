#non-pass
import math
def solution(numbers, target):
    answer = 0
    oper_arr = []
    max_number = int(math.pow(2,len(numbers)))
    
    for i in range(0, max_number):
        oper_arr.append(format(i,'b'))

    for i in range(0, max_number):
        count = len(oper_arr[i])
        if(count<len(numbers)):
            tmp = ''
            for j in range(0, len(numbers)-count):
                tmp += "0"
            oper_arr[i] = tmp + oper_arr[i]
            
    for i in range(0, max_number):
        tmp = ''
        for j in range(0, len(oper_arr[i])):
            if(oper_arr[i][j]=="0"):
                tmp += "-" 
            else:
                tmp += "+"
            tmp += str(numbers[j])
        if(eval(tmp)==target):
            answer+=1
    return answer

print(solution([1,1,1,1,1],3))
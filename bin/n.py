# n 으로 표현

# def solution(n, number):
#     answer = 0
#     return answer

# solution(5,12)

def number_to_1(n,m,sign):
    if(n>111*n):
        # print("return = 111 + number_to_1(",n-111,")")
        return sign+ str(111*m) + str(number_to_1(n-111,m,sign))
    elif(n>11):
        # print("return = 11 + number_to_1(",n-11,")")
        return sign+ str(11*m) + str(number_to_1(n-11,m,sign))
    elif(n>1):
        if(11-n < n):
            # print("return = 11 + number_to_1(",11-n,")")
            return sign+ str(11*m) + str(number_to_1(11-n,m,"-"))
        else:
            # print("return = 1 + number_to_1(",n-1,")")
            return sign+ str(1*m) + str(number_to_1(n-1,m,sign))
    else:
        # print("return n=",n)
        return sign + str(n*m)

# print(number_to_1(12,"+"))

def namuge(n,namuge):
    value = int(namuge / n)
    susik = ''
    for i in range(0, value):
        susik += "+"+str(n)
    value2 = namuge - (n*value)

    for i in range(0, value2):
        susik += "+("+str(n)+"/"+str(n)+")"
    return susik


def hello(n,number,max,cnt):
    susik=''
    namuge_value = ''
    if(number==0):
        return 0

    if(number % n==0):
        count = int(number/n)
        plus = ''
        for i in range(0, count):
            susik += "+"+str(n)
    else:
        susik = number_to_1(number,n,"+")
        susik = "("+susik+")/"+str(n)
        
    namuge_value = namuge(n, cnt)
    susik = susik + namuge_value
    max[cnt] = susik.count(str(n))
    cnt+=1
    return 1 + hello(n,number-1,max,cnt)


n = 2
number = 11
max = []

for i in range(0,number):
    max.append(-1)

hello(n,number,max,0)
return min(max)
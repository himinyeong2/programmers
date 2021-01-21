
#non-pass

arr = ["번호", "이름", "학번", "학년"]      
tmp = ''
result = []
for i in range(0, len(arr)):
    tmp =''
    for j in range(i, len(arr)):
        tmp += ","+arr[j]
    result.append(tmp)
print(result)
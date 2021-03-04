def travel(point, v, e,d): 
    # point 는 현재 정점이 뭔지?
    # v는 정점 리스트
    # e는 간선 리스트

    next_point = e[point]['next'] #다음 정점을 가르킴 예를들어 point 가 1이라면 next_point는 5가 되겟쥬?
    
    if(next_point==0):
        return d

    if(v[next_point]['status']=="fresh"):
        e[point]['status']="vistied"
        v[next_point]['status']="visited"
        return 1 + travel(next_point, v, e,d)
    else:
        e[point]['status']="back"
        return  d

def init(v, e):

    for i in range(1, len(v)):
        v[i]['status']="fresh"
        e[i]['status']="fresh"


def solution(arr):

    answer = 0
    v = [0]
    e = [0]
    max_v = -1
    max = -1
    size = len(arr)

    for i in range(0, size):
        tmp = dict()
        tmp["deep"] = 1
        tmp["status"]="fresh"
        tmp["number"]=i+1

        v.append(tmp)

    for i in arr:
        tmp = dict()
        tmp["next"] = i
        tmp["status"]="fresh"

        e.append(tmp)

    for i in range(1, len(v)):
        v[i]['status']="visited"
        v[i]['deep'] = travel(i, v, e,v[i]['deep'])
        if(max < v[i]['deep']):
            max_v = i
            max = v[i]['deep']
        elif(max==v[i]['deep']):
            if(max_v < i):
                max_v = i

        init(v, e)
        
    print (max_v)


    return answer



arr = [6,10,8,5,8,10,5,1,6,7]

solution(arr)
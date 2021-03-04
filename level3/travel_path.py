#여행경로

fresh = -999
visited = -1000

def is_connect(edge, edge_idx, start, end):
    if(edge[edge_idx]['start'] == start and edge[edge_idx]['end'] == end):
        return True
    else:
        return False

def dfs(node, edge, idx,last_edge , connect):
    if(last_edge!=-1):
        while(not is_connect(edge,last_edge, connect[-1]['point'],  idx)    ):
            edge[connect[-1]['edge']]['status']=fresh
            del(connect[-1])
    tmp={}
    tmp['edge'] = last_edge
    tmp['point'] = idx
    connect.append(tmp)

    for i in node[idx]['edge']:
        if(edge[i]['status']==fresh):
            edge[i]['status'] = visited
            dfs(node, edge, edge[i]['end'],i,connect)

# 알파벳순으로 넣기
def insert_edge(node, edge, idx, edge_idx):
    count = 0
    for i in node[idx]['edge']:
        op_data = node[edge[i]['end']]['name']
        if(op_data >= node[edge[edge_idx]['end']]['name']):
            break
        count+=1
    node[idx]['edge'].insert(count, edge_idx)

def solution(tickets):
    answer = []
    node = []
    edge = []
    airport = {}
    connect=[]
    count = 0
    for i in tickets:
        if not i[0] in airport.keys():
            airport[i[0]] = count
            count+=1
        if not i[1] in airport.keys():
            airport[i[1]] = count
            count+=1
    for i in tickets:
        tmp = {}
        tmp['start'] = airport[i[0]]
        tmp['end'] = airport[i[1]]
        tmp['status']=fresh
        edge.append(tmp)

    for i in airport:
        tmp = {}
        tmp['name'] = i
        tmp['status'] = fresh
        tmp['edge'] = []
        node.append(tmp)

    for i in range(0, len(edge)):
        node_idx = edge[i]['start']
        insert_edge(node, edge, node_idx, i)

    dfs(node, edge, airport['ICN'] ,-1 ,connect)

    for i in connect:
        answer.append(node[i['point']]['name'])
    
    return answer
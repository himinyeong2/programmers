#단어 변환

fresh = -999
visit = -1000
init = 999
def one_word_differ(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    count = 0

    if(str1_len >= str2_len):
        big_str = str1
        small_str = str2
    else:
        big_str = str2
        small_str = str1
    
    if(str1_len == str2_len):
        for i in range(0, str1_len):
            if(big_str[i] == small_str[i]):
                count += 1
        if(str1_len - count == 1):
            return True
    
    elif(len(big_str) - len(small_str) == 1):
        for i in range(0, len(small_str)):
            if(small_str[i] == big_str[i]):
                count+=1
        if(len(small_str) == count):
            return True

    return False
    

def init_node(node,words):

    for i in range(0, len(words)):
        tmp = {}
        tmp['number'] = i
        tmp['word'] = words[i]
        tmp['edge'] = []
        tmp['deep'] = init
        node.append(tmp)

def init_edge(node, edge):
    for i in range(0, len(node)):
        for j in range(i+1, len(node)):
            if(one_word_differ(node[i]['word'], node[j]['word'])):
                tmp = [node[i]['number'], node[j]['number']]
                edge.append(tmp)

def insert_edge(node, edge_idx):
    node['edge'].append(edge_idx)    

def opposite(node, edge):
    if(edge[0] == node['number']):
        return edge[1]
    else:
        return edge[0]

def get_connect_node(cur_node,edge):

    edges = cur_node['edge']
    return_node = []

    for eg in edges:
        op_node = opposite(cur_node, edge[eg])
        return_node.append(op_node)
    return return_node
    
def remove_min(q):
    
    min = q[0]['key']
    min_idx = 0
    return_value = q[0]['value']

    for i in range(0, len(q)):
        if(q[i]['key'] < min):
            min = q[i]['key']
            min_idx = i
            return_value = q[i]['value']

    q.pop(min_idx)

    return return_value

def is_empty(q):
    if(len(q)==0):
        return True
    return False

def init_queue(q,node):
    for i in node:
        tmp = {}
        tmp['key'] = i['deep']
        tmp['value'] = i['number']
        q.append(tmp)
def update_queue(q, idx,deep):

    for queue in q:
        if(queue['value'] == idx):
            queue['key'] = deep

def update_deep(nodes, edges, start):

    q=[]
    nodes[0]['deep'] = 0
    init_queue(q, nodes)

    while(not is_empty(q)):
        node_idx = remove_min(q)
        connect_nodes = get_connect_node(nodes[node_idx],edges)
        while(not is_empty(connect_nodes)):
            idx = connect_nodes.pop(0)

            if(nodes[idx]['deep'] > nodes[node_idx]['deep'] + 1):
                nodes[idx]['deep'] = nodes[node_idx]['deep'] + 1
                update_queue(q, idx, nodes[idx]['deep'])

def solution(begin, target, words):
    answer = 0
    node = []
    edge = []
    target_idx = init

    words.insert(0, begin)

    init_node(node, words)
    init_edge(node, edge)

    for i in range(0, len(edge)):
        left_idx = edge[i][0]
        right_idx = edge[i][1]
        insert_edge(node[left_idx], i)
        insert_edge(node[right_idx], i)
    
    update_deep(node, edge, begin)

    for idx in range(0, len(node)):
        if(node[idx]['word'] == target):
            target_idx = idx
    if(target_idx == init or node[target_idx]['deep'] == init):
        answer = 0
    else:
        answer = node[target_idx]['deep']

    return answer
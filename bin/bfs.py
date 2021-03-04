fresh = -10000
visit = -555

def is_empty(q):
    if(len(q)==0):
        return True
    else:
        return False

def bfs(node, edge):
    print("- - - - - - BFS START - - - - - -")
    Q=[[0]]
    i=0
    node[0]['status']=visit

    while(not is_empty(Q[i])):
        while(not is_empty(Q[i])):
            node_idx = Q[i].pop(0)
            op_nodx_idx = get_opposite_node(node, edge, node_idx)
            tmp = []
            for idx in op_nodx_idx:
                if(node[idx]['status']==fresh):
                    tmp.append(idx)
                    node[idx]['status']=visit
            Q.append(tmp)
            
        i+=1    


def get_opposite_node(node, edge, idx):
    return_node = []
    
    for i in node[idx]['edge']:
        op_node = opposite_node(edge[i], idx)
        return_node.append(op_node)
    return return_node



def opposite_node(edge, node_idx):
    if(edge[0]==node_idx):
        return edge[1]
    else:
        return edge[0]

def insert_edge(node, edge, node_idx, edge_idx):
    ins_node = opposite_node(edge[edge_idx], node_idx)
    count = 0
    for i in node[node_idx]['edge']:
        op_node = opposite_node(edge[i], node_idx)
        count+=1
        if(op_node >= ins_node):
            break
    node[node_idx]['edge'].insert(count, edge_idx)
        

def init_edge(node, edge):

    for i in range(0, len(edge)):
        left_node = edge[i][0]
        right_node = edge[i][1]

        insert_edge(node, edge, left_node, i)
        insert_edge(node, edge, right_node, i)


def init_node(n):
    node = []
    for i in range(0, n):
        tmp = {}
        tmp['number'] = i
        tmp['status'] = fresh
        tmp['edge'] = []
        node.append(tmp)
    return node
if __name__ == "__main__":

    n = 6
    edge = [[0,1],[0,2],[0,3],[1,2],[1,4],[2,3],[2,4],[2,5],[3,5]]
    node = []

    node = init_node(n)
    init_edge(node, edge)

    for i in node:
        print(i)


    bfs(node,edge)

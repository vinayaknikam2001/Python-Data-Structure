def add_node(v):
    global node_count
    if (v in graph):
        print(f'Node {v} is already present in a graph. ')
    else:
        node_count += 1
        graph[v] = []
        

def add_edge(v1,v2):
    if (v1 not in graph):
        print(f'Vertex {v1} is not present in graph. ')
        return
    if (v2 not in graph):
        return
        print(f'Vertex {v2} is not present in graph. ')
    else:
        graph[v1].append(v2)
    

def delete_node(v):
    if (v not in graph):
        print(f'Node  {v} is not present in the graph. ')
    else:
        graph.pop(v)
        for i in graph:
            lst = graph[i]
            if (v in lst):
                lst.remove(v)

def delete_edge(v1,v2):
    if (v1 not in graph):
        print(f'Vertex {v1} is not present in graph. ')
        return
    if (v2 not in graph):
        return
        print(f'Vertex {v2} is not present in graph. ')
        
    else:
        if(v1 in graph[v2]):
            graph[v2].remove(v1)
        if(v2 in graph[v1]):
            graph[v1].remove(v2)
        

def DFS(node,visited,graph):
    if node not in graph:
        print('\nGiven node is not present in a graph. ')
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph) 
        
                



if(__name__ == '__main__'):
    graph = {}
    node_count = 0
    ch = 1
    while (ch):
        ch = int(input('\n Enter your choice 0)Quit   1)Add node   2)Add edge   3)Delete node   4)Delete edge   5)Display graph. '))
        if(ch == 1):
            val = input('\n Enter value to add. ')
            add_node(val)
        elif(ch == 2):
            v1,v2 = map(str,input('\n Enter nodes to add edge between ').split())
            add_edge(v1,v2)
        
        elif(ch == 3):
            val = input('\n Enter value to delete. ')
            delete_node(val)
        elif(ch == 4):
            v1,v2 = map(str,input('\n Enter nodes to delete edge between ').split())
            delete_edge(v1,v2)   
        elif(ch == 5):
            print(graph)
        elif(ch == 6):
            visited = set()
            node = input('\nEnter node to start searching ')
            DFS(node,visited,graph)
    
    

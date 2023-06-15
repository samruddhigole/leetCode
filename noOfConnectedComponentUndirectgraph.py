def countComponent(n,edges):
    count=0
    graph = [[] for _ in range(n+1) ]
    vis = [False for _ in range(n+1)]
    arr=[]
    for a,b in edges:
        print(a,"value a")
        graph[a].append(b)
        print(b,"value b")
        graph[b].append(a)
        print(graph)
    
    def dfs(node):
        for adj in graph[node]:
            if not vis[adj]:
                arr.append(adj)
                vis[adj]=True
                dfs(adj)

    for i in range (n):
        if not vis[i]:
            arr.append(i)
            count += 1
            vis[i] = True
            dfs(i)
    print(arr)
    print(graph)
    print (count)

        # graph = [[] for _ in range (n)]
        # vis=[False for _ in range (n)]
        # arr=[]
        # print(graph)
        
        # for a,b in paths:
        #     graph[a].append(b)
            
        #     graph[b].append(a)
            
        # def dfs(node):
        #     for index in graph[node]:
        #         if not vis[index]:
        #             vis[index]=True
        #             arr.append(index)
        #             dfs(index)
            
        
        # for index in range(n):
        #     if not vis[index]:
        #         vis[index]=True
        #         arr.append(index)
        #         dfs(index)
        # return arr

# countComponent(3,[[1,2],[2,3],[3,1]])
# countComponent(5,[[0,1],[1,2],[3,4]])
countComponent(4,[[1,2],[3,4]])


# def countComponents( n, edges):
#         count = 0
#         graph = [[] for _ in range(n)]
#         seen = [False for _ in range(n)]
        
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
            
#         def dfs(node):
#             for adj in graph[node]:
#                 if not seen[adj]:
#                     seen[adj] = True
#                     dfs(adj)
                    
#         for i in range(n):
#             if not seen[i]:
#                 count += 1
#                 seen[i] = True
#                 dfs(i)
#         print(count)
#         return count
# countComponents(5,[[0,1],[1,2],[3,4]])

    #   graph = [[] for _ in range (n)]
    #     vis=[False for _ in range (n)]
    #     arr=[]
        
    #     for a,b in paths:
    #         a,b=a+1,b+1
    #         graph[a].append(b)
    #         graph[b].append(a)
    #     # print(graph)
            
    #     def dfs(node):
    #         for index in graph[node]:
    #             if not vis[index]:
    #                 print(index)
    #                 arr.append(index)
    #                 vis[index]=True
                    
    #                 dfs(index)
            
        
    #     for index in range(1,n-1):
            
    #         if not vis[index]:
    #             print(index)
    #             arr.append(index)
    #             vis[index]=True
                
    #             dfs(index)
    #     return arr
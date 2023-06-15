def noOfIsland(n,m,grid):
    count=0
    graph = [[] for _ in range (n)]
    vis = [False for _ in range (m)]
    if(n== 1 and m==1 and grid[0][0] == "1" ):
        count+=1
        print(count)
        return count
    elif(n== 1 and m==1 and grid[0][0] == "0" ):
        print(count)
        return count
    if(n== 0 and m==0 ):
        return count
    if(n==1 and m==0):
        return count
    if(m==1 and n==0):
        return count
   
    

    for a in range(n):
        for b  in range (len(grid[a])):
            # print(grid[a][b])
            if(grid[a][b] == "1"):
                graph[a].append(b)
                # graph[b].append(a)
    
  

    def dfs(node):
        # print(node)
        # print(graph[node])
        if(node<n):
            for i in graph[node]:
                if not vis[i]:
                    vis[i]=True
                    dfs(i)

    for i in range (n):
        if not vis[i]:
            count+=1
            vis[i] = True
            # print(vis)
            # print(i)
            dfs(i)
    # return count
    # print(graph)
    print(count)
    # print(vis)

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
grid=[["1"]]
noOfIsland(1,1,grid)

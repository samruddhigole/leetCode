def townJudge(trust,N):
    if len(trust) < N - 1:
        return -1
    indegree = [0] * (N + 1)
    outdegree = [0] * (N + 1)
    print(indegree,outdegree)
    for a, b in trust:
        print(a,b)
        outdegree[a] += 1
        indegree[b] += 1
    print(indegree,outdegree)
    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i
    return -1
    



trust = [[1,3],[2,3],[4,3],[4,1],[5,3],[5,1],[5,4]]
array=[2,5,4,3,56,7,78,5,3,67,6,980,7,5]
print(sorted(array))
res = townJudge(trust,5)
print(res)
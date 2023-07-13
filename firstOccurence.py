def firstOccurence(str1,s):
    n=len(str1)
    m=len(s)
    for i in range(n-m+1):
        for j in range(m):
            if (s[j] != str1[i+j]):
                break
            if(j==m-1):
                return i
    return -1


res = firstOccurence("leetcode","leeto")
print(res)
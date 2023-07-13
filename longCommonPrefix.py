def longestCommonPrefix(strs):
    # if(len(strs) == 1):
    #     return strs[0]
    # elif(len(strs)>1):
    #     res=''
    #     flag=0
    #     for index1 in range(0,len(strs[0])):
    #         string=strs[0][index1]
    #         for index in range (0,len(strs)):
    #             if((string) == strs[index][index1]):
    #                 flag =1
    #                 continue
    #             else:
    #                 return res
    #         if (flag==1):
    #             res = res+string
                
    #     return res

    if(len(strs) == 1):
        return strs[0]
    elif(len(strs)>1):
        res=''
        flag=0
        string=strs[0]
        for index1 in range(1,len(strs)):
                # while(strs[index1])
            index=0
            while(len(string)!=0):  
            # for index in range (0,len(string)):
                string1=strs[index1][index]
                if((string1) == string[index]):
                    flag =1
                    index+=1
                    continue
                else:
                    return res
            if (flag==1):
                res = res+string      
        return res
    
res = longestCommonPrefix(['ab','a'])
print (res)



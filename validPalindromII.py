def validPalindromII(str):
    def checkPalindrom(str,start,end):
        while(start<end):
            if(str[start]!=str[end]):
                return False
            start+=1
            end-=1
        return True
    if(len(str)==0):
        return False
    if(len(str)==1):
        return True
    strt=0
    end=len(str)-1
    while(strt<end):
        if(str[strt]!=str[end]):
            return checkPalindrom(str,strt,end-1) or checkPalindrom(str,strt+1,end)
        strt+=1
        end-=1
    return True

res=validPalindromII("abc")
print(res)
#replace chars in the same string

def res(Str):
    start = 0
    end = len(Str)-1
    if(len(Str) == 0):
        return None
    if(len(Str)==1):
        return Str
    elif(len(Str)>1):
        if(len(Str)%2==0):
            while(start != end):
                Str[start],Str[end] = Str[end],Str[start]
                start+=1
                end-=1
            return Str
        elif(len(Str)%2!=0):
            while(start < end):
                Str[start],Str[end] = Str[end],Str[start]
                start+=1
                end-=1
            return Str
        
str = "samruddhi"
str=list(str)
rev=res(str)
rev=(''.join(rev))
print(rev)

def findChar(String,char1):
    if(len(String) == 0):
        return False
    if(len(String) == 1):
        if(String == char1):
            return True
        return False
    index=0
    length = len(String)-1
    if(length):
        while(len(String) > index):
            if(String[index] == char1):
                return True
            else:
                index+=1
                length-+1
        return False
    
res = findChar("Samruddhi", 'p')
if(res == True):
    print("Found")
elif(res==False):
    print("not Found")
def isPalindrome( s):
        """
        :type s: str
        :rtype: bool
        """
        def isPal(s,left,right):
            if(left>=right):
                return True
            
            if(s[left].lower()!=s[right].lower()):
                return False
            if(not s[left].isalnum() and not s[right].isalnum()):        
                return isPal(s,left+1,right-1)
        return isPal(s,0,len(s)-1)
s="A man, a plan, a canal: Panama"
# s=s.replace(" ","")
# s=s.replace(",","")
# s=s.replace(":","")
# print(s)
result= isPalindrome(s)
print(result)
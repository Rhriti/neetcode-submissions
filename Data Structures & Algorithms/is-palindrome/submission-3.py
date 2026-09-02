class Solution:
    def isPalindrome(self, s: str) :
        i=0
        j=max(0,len(s)-1)
        while j>=i:
            while i<len(s)  and not s[i].isalnum():i+=1
            while j>=0 and not s[j].isalnum():j-=1
            if not j>=i:return True
       
            if s[i].lower()!=s[j].lower():return False
            i+=1
            j-=1
        return True
        
        
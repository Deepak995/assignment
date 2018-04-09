class palindrome:
    
    def rev(self,s):
        r=""
        p=len(s)-1
        while p>=0:
            """r=r+s[p]
            
            p-=1"""
            if (s[p]>='a' and s[p]<='z') or(s[p]>='A' and s[p]<='Z') or(s[p]>='0' and s[p]<='9'):
                r=r+s[p]
            
            p-=1
        return r
        
    def rem(self,s):
        v=""
        p=len(s)-1
        i=0
        while i<=p:
            """v=v+s[i]
            i+=1"""
            
            if (s[i]>='a' and s[i]<='z') or(s[i]>='A' and s[i]<='Z')or(s[i]>='0' and s[i]<='9'):
                v=v+s[i]
            i+=1
        return v
        
    def com(self,a,b):
        if (a.lower()==b.lower()):
            print("the string is palindrom")
        else: 
            print("the string is not palindrom")
            
            
b="1A man, a plan, a canal: Panama1" 

ob=palindrome()
revers=ob.rev(b)
#print(revers)

straight=ob.rem(b)
#print(straight)
ob.com(straight,revers)



        
        
        
    


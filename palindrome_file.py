class palindrome:
    
    def rev(self,s):# to reverse the given input string
        r=""
        p=len(s)-1
        while p>=0:
            """r=r+s[p]
            
            p-=1"""
            if (s[p]>='a' and s[p]<='z') or(s[p]>='A' and s[p]<='Z') or(s[p]>='0' and s[p]<='9'):
                r=r+s[p]
            
            p-=1
        return r
        
    def rem(self,s): # to ignore the special cherecter from input string
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
        
    def com(self,a,b):# to compare the reverse and straight strings
        if (a.lower()==b.lower()):
            print("the string is palindrom")
        else: 
            print("the string is not palindrom")
            
    def call_fun(self,line):# passing input string
        revers=ob.rev(line)# calling the reverse function
    #print(revers)

        straight=ob.rem(line)
    #print(straight)
        ob.com(straight,revers)
        
ob=palindrome()
wr=open("palindrome1.txt","w")# this is to create a text file which contans input strings.
list=['ye wah he ra\n','anana\n','A man, a plan, a canal: Panama\n']# creating a list with the delimeter \n
wr.writelines(list)
wr.close()


be=open("palindrome1.txt","r")
b=be.read().split("\n") #spliting the input strings from where the line is changing
#print(b)
for line in b: #passing the string line by line fron the list 
    
    if line=='':
        break
    else:
        ob.call_fun(line)
        
be.close()


        
        
        
    


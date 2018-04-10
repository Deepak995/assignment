class revorder:
    def order(self,s):# this function will reverse the order of input string and will save it in a list
        h=[]
        g=s.split(" ")
        for i in reversed(g):
            #print(i)
            h+=[i]
            #print(h)
        return h #returning a list 
s=input("enter a String ")
ob=revorder()
k=ob.order(s)
st=""
for i in k:# converting a list into a string
    st=st+" "+i
print(st)
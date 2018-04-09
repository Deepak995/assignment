class subarray:
    array =[2,1,-3,4,-1,2,1,-5,4]
    sum=0
    maxsum=0
    k=0
    #f=[]
    h=[]
    while k<len(array):
        j=k
        while j<len(array):

            sum=sum+array[j]
            #print()


            h+=[array[j]]
            if(sum>=maxsum):
                maxsum=sum
                f = h
                h=[]



            j+=1
        h = []
        k+=1
        sum = 0

    print(maxsum)
    print(f)


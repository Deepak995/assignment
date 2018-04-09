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

            sum=sum+array[j]# adding the sum of every sub array
            #print()


            h+=[array[j]]
            if(sum>=maxsum):# in every iteration if the sun is greater  then maxsum then save sum into maxsum
                maxsum=sum
                f = h # saving the sunarray into new variables
                h=[] # emptying the previous sub array



            j+=1
        h = []
        k+=1
        sum = 0

    print(maxsum)
    print(f)


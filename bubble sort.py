def bubblesort(ls):
    n=len(ls)
    for i in range(n):
        if j in range(0,i-n-1):
            if(ls[j]>ls[j+1]):
                tmp=ls[j+1]
                ls[j+1]=ls[j]
                ls[j]=tmp
            return(ls)


if __name__=="__main__":
    ls=[1,7,4,9,2,0,4]
    r=[]
    r=bubblesort(ls)
    print("sorted list is:",r)

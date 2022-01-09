#challenge 5
#sort the array of 0,1,2 elements without using sorting method
def sortArray(arr,n):
    #print(arr,n)
    l=0  #low pointer
    m=0  #mid pointer
    h=n-1  #high pointer
    while( m<=h ):
        if (arr[m]== 0):
            #swap m & l th element
            temp= arr[m]
            arr[m]= arr[l]
            arr[l]= temp

            #increase m & l
            m=m+1
            l=l+1

        elif (arr[m]== 1):
            #no need to swaping here
            #increase m only
            m=m+1
        
        elif (arr[m]== 2):
            #swap m & h th element
            temp= arr[m]
            arr[m]= arr[h]
            arr[h]= temp

            #decrease h
            h=h-1
    print(arr)

array=[0,1,2,0,1,2,1,0,0]
n=len(array)

sortArray(array,n)
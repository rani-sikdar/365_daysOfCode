#challenge9
#Minimise the maximum difference between heights 
def maxDiff(arr,n,k):

    #print(arr,n,k)
    maxi= arr[n-1]-arr[0]   #initial maximum= last element - first element
    smallest= arr[0] + k   
    largest= arr[n-1] - k

    for i in range(0,n-1):
        m1= (min(smallest, arr[i+1]-k))
        m2= (max(largest, arr[i]+k))
        if(m1<0): continue

        maxi= min(maxi, (m2-m1) )
    
    return maxi

#array=[8, 1, 5, 4, 7, 5, 7, 9, 4, 6]
#array=[1, 5, 15, 10]
#array=[4, 6]
array=[1, 10, 14, 14, 14, 15]
k=6
array.sort() #sort the arrray

print('maximum difference is {}'.format(maxDiff(array,len(array),k)))



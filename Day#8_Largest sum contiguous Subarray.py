#challenge7
#find Largest sum contiguous Subarray
#kadane's algorithm
def subarray(arr,n):
    #print(arr,n)
    sum=0
    maxi= arr[0]
    for i in range(0,n):
        sum= sum+arr[i]
        if(sum >maxi):
            maxi=sum
        if(sum< 0):
            sum=0

    print (maxi)

array=[-2, -3, 4, -1, -2, 1, 5, -3]
#array=[4,2,-3,5,7]
n=len(array)

subarray(array,n)
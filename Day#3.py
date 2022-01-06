#challenge3
#find kth largest/smallest element in an array.

def kthSmallest(arr,n,k):
    #print(arr,n,k)
    arr.sort()
    #print(arr)

    print('{}th smallest element in given array is {}'.format(k,arr[k-1]))

def KthLargest(arr,n,k):
    arr.sort(reverse=True)
    #print(arr[k-1])

    print('{}th largest element in given array is {}'.format(k,arr[k-1]))

array=[3,7,12,1,29,30,5]
n=len(array)
k=3  #let k=3
print(array)

kthSmallest(array,n,k)
KthLargest(array,n,k)

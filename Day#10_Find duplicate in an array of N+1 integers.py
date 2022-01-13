#challenge10
#find duplicates in an array in O(1) complexity
def duplicate(arr,n):
    #print(arr,n)
    if(n<=1) :
        return -1
    slow=arr[0]
    fast=arr[arr[0]]

    while(fast!=slow):
        slow=arr[slow] #1 step for slow

        fast=arr[arr[fast]] #2 steps for fast

    fast=0
    while(slow!=fast):
        slow=arr[slow]
        fast=arr[fast]
    return slow

#array=[1, 2, 3, 4, 5, 6, 3]
#array=[1, 2, 3, 4, 5,3, 6, 7,8]
array=[1,2,5,8,2,9]

print(duplicate(array,len(array)))
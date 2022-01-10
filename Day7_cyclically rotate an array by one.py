#Chanllenge7
#program to rotate the array by an element

def rotateArray(arr,n):
    temp= arr[n-1]

    for i in range(n-1,0,-1):
        #print(i,arr[i])
        arr[i]= arr[i-1]
    arr[0]=temp
    print(arr)        

arr=[1,2,3,4,5,8,9,10]
n=len(arr)
print(arr)
rotateArray(arr,n)

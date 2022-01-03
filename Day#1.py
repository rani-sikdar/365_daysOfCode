def reversedArray(arr):
    newArray=list()
    for i in range(len(arr)-1,-1,-1):
        
        newArray.append(arr[i])
        
    print('Reversed Array-')
    print(newArray)

array=[1,2,3,4,5,6,7,8,9,10]
print('Original Array-')
print(array)

reversedArray(array)``


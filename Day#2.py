#challenge_2
#Maximum & Minimum for an array

def findMax(arr):
    max=arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > max):
            max = arr[i]
    
    #print('Maximum of Array -{}'.format(max))

    print('Maximum of Array ')
    print(max)

def findMin(arr):
    min=arr[0]
    for i in range(1, len(arr)):
        if(arr[i] <min):
            min=arr[i]
    #print('Minimum of Array -{}'.format(min))

    print('Minimum of Array ')
    print(min)


array=[1,2,3,4,0,5,6,17,8,9,10]
findMax(array)
findMin(array)

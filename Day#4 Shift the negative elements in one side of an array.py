#Challenge 4
#Shift the negative elements in one side of an array

def shiftElements(arr,n):
    #print(arr,n)
    j=0
    for i in range(n):
        #check for the negative elements
        if (arr[i]<0):
            #swap the elements at i and j
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j=j+1
    print('The shifted array is-')
    print(arr)
        

array= [-1,2,-3,-4,-5]

n=len(array)
shiftElements(array,n)

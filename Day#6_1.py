#challenge6
#union & intersection of an sorted array
def unionArray(arr1,arr2,m,n):
   # print(arr1,arr2,m,n)
    i=0; j=0; prev=None

    while (i<m and j<n):
        if (arr1[i] < arr2[j]):
            if(arr1[i]!= prev ):
                print(arr1[i],end=' ')
                prev= arr1[i]
                union.append(arr1[i])
            i +=1

        elif (arr1[i] > arr2[j]):
            if(arr2[j]!= prev ):
                print(arr2[j],end=' ')
                prev= arr2[j]
                union.append(arr2[j])
            j +=1

        else:
            if(arr1[i]!= prev ):
                print(arr1[i],end=' ')
                prev= arr1[i]
                union.append(arr1[i])
            j +=1; i+=1

    while (i<m):
        if(arr1[i]!= prev ):
            print(arr1[i],end=' ')
            prev= arr1[i]
            union.append(arr1[i])
        i+=1

    while (j<n):
        if(arr2[j]!= prev ):
            print(arr2[j],end=' ')
            prev= arr2[j]
            union.append(arr2[j])   
        j +=1
        
    print(union)
union=[]
arr1=[1, 2, 2, 2, 3]
arr2=[2, 3, 4, 5]
m=len(arr1)
n=len(arr2)

unionArray(arr1,arr2,m,n)
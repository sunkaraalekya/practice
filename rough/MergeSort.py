





def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

arr=[12,45,9,2,34]
print("Given array is", end="\n")
printList(arr)
mergesort(arr)
print("Sorted array is:", end="\n")
printList(arr)

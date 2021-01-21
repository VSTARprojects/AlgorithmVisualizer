#function to do insertion sort
def insertion_sort(arr):
    
    #iterating elements from 1 till last
    
    for i in range(1,len(arr)):
        
        #assigning ith element to key
        
        key=arr[i]
        j=i-1
        
        #moving elements ahead that are greater tha key
        
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

#driver code
arr=[4,3,2,10,12,1,5,6]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])
        
    
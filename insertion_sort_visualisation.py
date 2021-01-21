#importing required modules for the program

import pygame, random

width=1280
height=720
gap=2

#defining array size and storing random elements in array

arrsize=80
rectw=width/arrsize-gap
#arr=[random.randrange(50,500) for i in range(50)]

arr=[400,300,200,110,120,130,500,60]
#initialising pygame

pygame.init()
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("insertion sort")


#specifying different colors for keyvalue and other array elements

def displayarr(arr,key):
    window.fill((0,0,0))
    for p in range(len(arr)):
        if arr[p]==key:
            color=(255,0,0)
        else:
            color=(0,255,0)
        pygame.draw.rect(window,color,(p*(rectw+gap),height-arr[p],rectw,arr[p]))
    pygame.display.update()
    pygame.time.wait(20)
    

#logic for insertion sort

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        displayarr(arr,key)
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        displayarr(arr,key)
    #for val in arr:
        #print(val)



#driver code        
if __name__=="__main__":
    running = True
    firsttime=True
    while running:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running=False
        if firsttime:
            insertionsort(arr)
        firsttime=False
    
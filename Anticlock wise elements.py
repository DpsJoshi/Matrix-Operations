arr1=([[1,2,3],
       [4,5,6],
       [7,8,9]])
x=int(input("Enter total rotation: "))
def num_rotation(x,arr):
    for i in range(x):
        anticlock_one(arr)
    mat_pr(arr)
def anticlock_one(arr):
    if len(arr)==0:
        return
    top=0
    bottom=len(arr)-1
    left=0
    right=len(arr)-1


    while top<bottom and left<right:

        prev = arr[top][left +1]

        for i in range(top,bottom+1):
            cur=arr[i][left]
            arr[i][left]=prev
            prev=cur
        left+=1

        for i in range(left,right+1):
            cur=arr[bottom][i]
            arr[bottom][i]=prev
            prev=cur
        bottom-=1

        for i in range(bottom,top-1,-1):
            cur=arr[i][right]
            arr[i][right]=prev
            prev=cur
        right-=1

        for i in range(right,left-1,-1):
            cur=arr[top][i]
            arr[top][i]=prev
            prev=cur
        top+=1

def mat_pr(arr):
    for row in arr:
        print(row)


num_rotation(x,arr1)
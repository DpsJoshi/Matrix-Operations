arr=([[1,2,3,4],
      [4,5,6,7],
      [7,8,9,10],
      [11,12,13,14]])
num=int(input("Enter total rotation: "))
def rotate_one(arr):
    result=[]
    for i in range(len(arr)):
        prev=arr[i][len(arr)-1]
        for j in range(len(arr)):
            cur=arr[i][j]
            arr[i][j]=prev
            prev=cur
    return arr
def print_mat(result):
    for row in result:
        print(row)
def n_rotate(num,arr):
    for i in range(num):
        rotate_one(arr)
    print_mat(arr)

n_rotate(num,arr)
arr1=([[0,1,2,3,4],
       [5,6,7,8,9],
       [10,11,12,13,14],
       [15,16,17,18,19],
       [20,21,22,23,24]])

def swap_rows(arr):
    if len(arr)==0:
        return
    result=[]
    for i in range(len(arr)):
        result.append([0]*len(arr))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i%2==0 :
                if i<len(arr)-1:
                    result[i][j]=arr[i+1][j]
                else:
                    result[i][j]=arr[i][j]
            else:
                result[i][j]=arr[i-1][j]

    for row in result:
        print(row)
swap_rows(arr1)
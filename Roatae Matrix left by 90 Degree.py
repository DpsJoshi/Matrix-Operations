def rotate_left_90(arr):
    result=[]
    for i in range(len(arr)):
        result.append([0]*len(arr))             # Creating zero matrix shape of given matrix

    for i in range(len(arr)):
        for j in range(len(arr[0])):            # Transpose a given matrix
            result[i][j]=arr[j][i]

    print()
    for i in range(len(arr)):
        for j in range(len(arr[0])):            # Swaping the elemets to each other
            arr[i][j]=result[len(arr)-1-i][j]

    for row in arr:
        print(row)                              # For printing modified array elements



arr1=([[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
       [13,14,15,16]])
rotate_left_90(arr1)




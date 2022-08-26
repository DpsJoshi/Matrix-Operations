def matrix_clockwise(arr):
    if len(arr)==0:
        return
    top=0
    left=0                                  #Intialize the values of corners
    right=len(arr)-1
    bottom=len(arr) - 1
    new_prev = 0                            #Intialize for previous element condition

    while top<=bottom:

        if len(arr)%2==0 and top==0:           #For even rows matrix last element should be 1st of last rowth.
            prev=arr[bottom][left]
        elif len(arr)%2==1 and top==0:         #For odd rows matrix last element should be last of last rowth.
            prev=arr[bottom][right]
        else:
            prev=new_prev
            new_prev-=prev

        for i in range(left,right+1):           #Swaping the elements of even lines
            cur=arr[top][i]
            arr[top][i]=prev
            prev=cur

        top+=1
        if top>bottom:                           #Break the loop if there is no more rows
            break

        for i in range(len(arr)-1,-1,-1):
            cur=arr[top][i]
            arr[top][i]=prev                     #Swaping the elemts of odd rows
            prev=cur
            if i==0:
                new_prev+=prev
        top+=1
        if top>bottom:                            #Break the loop if there is no more rows
            break

    for row in arr:
        print(row)                                 #For printing the new array

arr1=([[1,2,3],
       [4,5,5],
       [6,7,8]])

matrix_clockwise(arr1)


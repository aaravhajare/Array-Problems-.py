
def rotation(arr , n , al) :

    for i in range(n) :
        rotate(arr , al) 

def rotate(arr , al) :

    temp = arr[0] 

    for i in range(al - 1) :

        arr[i] = arr[i+1]

        arr[al-1] = temp

def p_arr(arr , al) :

    for i  in range(al) :

        print(arr[i] , end= " ")
    print("\n")

a = [ 1,2,3,4,5,5,6,6,]
n = 2

p_arr(a , len(a))

rotation(a , 2 , len(a))
p_arr(a , len(a))


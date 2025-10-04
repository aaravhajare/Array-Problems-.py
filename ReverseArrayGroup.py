
def reverse(arr , arr_l , n) :

    temp = 0

    while temp < arr_l :
         start = temp

         
         end = min(temp + n - 1 , arr_l - 1)

         while start < end :
              
            arr[start] , arr[end] = arr[end] , arr[start]
            start += 1 
            end -= 1
        
         temp += n 

a = [1,2,3,4,5,6,7,8]

n = 2

l = len(a)

reverse(a , l , n)

for i in range(0 , l) :
    print(a , end = " ")

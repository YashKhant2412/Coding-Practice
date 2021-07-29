def solve(A, B):
        arr=A[:B]               #Array of present sum
        val=sum(A[:B])  
        imax=val
        for i in range(0,B):
            rem=arr.pop()       #Remove the last element from arr
            add=A.pop()         #Last element of A
            val=val-rem+add     #Remove the last element of arr and replace it with last element of A
            imax=max(imax,val)
        return imax
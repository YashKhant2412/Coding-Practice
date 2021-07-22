'''Kth Row of Pascal's Triangle
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
Note : k is 0 based. k = 0, corresponds to the row [1].'''

class Solution:    
    # @param A : integer
    # @return a list of integers
    def permi(self,i,j):
        if j==0 or i==j:
            return 1
        else:
            x,y,z=1,1,1
            for a in range(1,i+1):
                x*=a
            for b in range(1,j+1):
                y*=b
            for c in range(1,i-j+1):
                z*=c
            return int((x/(y*z)))

    def getRow(self, A):
        lst = []
        for i in range(A+1):
            lst.append(self.permi(A,i))
        return lst

#Second and efficient Solution
class Solution:
    # @param A : integer
    # @return a list of integers

    def getRow(self, A):
        lst = [0 for _ in range(A+1)]
        lst[0]=1
        a = A
        for i in range(1,A+1):
            lst[i] = int((lst[i-1]*a)/i)
            a-=1

        return lst        
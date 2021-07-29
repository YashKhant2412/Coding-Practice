'''Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the count of special elements.



Example Input
Input 1:

 A = [2, 1, 6, 4]
Input 2:

 A = [5, 5, 2, 5, 8]


Example Output
Output 1:

 1
Output 2:

 2'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        x=y=x1=y1=0
        for i in range(len(A) ):
            if i%2==0:
                x+=A[i]
            else:
                y+=A[i]
        count=0
        for i in range(len(A) ):
            if i%2==0:
                x-=A[i]
                if x+y1==y+x1:
                    count+=1
                x1+=A[i]
            else:
                y-=A[i]
                if x+y1==y+x1:
                    count+=1
                y1+=A[i]
        return count

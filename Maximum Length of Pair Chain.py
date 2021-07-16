'''You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order. 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].'''

class Solution:
    def findLongestChain(self, pairs):
        op = sorted(pairs, key=lambda x:x[0])
        
        res = 1
        
        temp = []
        
        for data in op:
            if not temp: 
                temp = data
                continue
                
            if temp[1] < data[0]:
                res += 1
                temp = data
                continue
                
            if temp[1] >= data[1]:
                temp = data
                continue
            
        return res
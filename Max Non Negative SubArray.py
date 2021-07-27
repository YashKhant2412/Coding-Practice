class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        total = 0
        c = []
        cs = []
        for i in A:
            if i>=0:
                c.append(i)
            elif i<0:
                cs.append(c)
                c = []
                total = 0
        if(len(c)>0):
            cs.append(c)
        bestc = []
        bestsum = -1
        for i in cs:
            if(sum(i)>bestsum):
                bestc = i
                bestsum = sum(i)
        return bestc
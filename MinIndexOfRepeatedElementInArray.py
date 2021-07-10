import numpy as np

lst1 = np.array([int(i) for i in input().split()])
lst2 = np.array([-1 for _ in range(9999)])
minIndex = 99999
for i in range(len(lst1)):
    if(lst2[lst1[i]]!=-1):
        minIndex = min(minIndex,lst2[lst1[i]])      
    else:
        lst2[lst1[i]]=i

print(minIndex)
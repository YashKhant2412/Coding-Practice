def check_anagram(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    dt1 = {}
    dt2 = {}
    for i in range(len(str1)):
        if(str1[i] in dt1):
            dt1[str1[i]]+=1
        else:
            dt1[str1[i]]=1
        if(str2[i] in dt2):
            dt2[str2[i]]+=1
        else:
            dt2[str2[i]]=1
    return dt1==dt2


#Solution2
from collections import Counter
def check_anagram(str1,str2):
    return Counter(str1)==Counter(str2)
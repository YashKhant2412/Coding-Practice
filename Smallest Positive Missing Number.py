'''You have given an array arr[] of N integer including 0. The task is to find the smallest positive number missing from the array.'''

def func(x):
    lst = [False for _ in range(int(1e5))]
    for i in range(len(x)):
        if x[i] > -1:
            lst[x[i]] = True
    j = 0
    while lst[j] == True:
        j += 1
    print(j)


x = [0, -9, 1, 3, -4, 5]
func(x)
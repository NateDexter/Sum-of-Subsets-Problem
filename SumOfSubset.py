import numpy as np
w=list(map(int,input('Enter integers\n').split()))
Sum=int(input('SUM:'))
w=np.asarray(w)
l=len(w)
def display(s1):
    print('Solution found: ')
    print(s1,"\n")

subset=set()
def sos(i):
    for k in range(i,l):
        subset.add(w[k])
        if sum(subset)==Sum:
            display(subset)
            subset.remove(w[k])

        elif (sum(subset)<Sum) & (k!=(l-1)):
            sos(k+1)
            subset.remove(w[k])
            
        else:
            subset.remove(w[k])
        
           
sos(0)
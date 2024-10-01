import numpy as np
from math import sqrt

def std_loops(lst):
    sum=0
    length=0

    for num in lst:
        sum+=num
        length+=1

    mean=sum/length
    
    sum2=0
    
    for num in lst:
        sum2+=num**2
        
    meanSquares=sum2/length

    deviation2=meanSquares-mean**2

    deviation=sqrt(deviation2)
    
    return deviation

def std_builtin(lst):
    mean=sum(lst)/len(lst)
    
    num_lst = [1, 2, 3, 4, 5]

    squares=np.array(num_lst)
    
    meanSquares=sum(squares**2)/len(lst)
    
    deviation2=meanSquares-mean**2

    deviation=sqrt(deviation2)
    
    return deviation


num_lst = [1, 2, 3, 4, 5]

print(std_loops(num_lst))
print(std_builtin(num_lst))
print(np.std(num_lst))

    
    
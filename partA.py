import numpy as np
from math import sqrt

def std_loops(lst):
    """
    Compute standard deviation of x using loops.
    Parameters
    ----------
    x: Sequence of numbers
    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    sum = 0
    
    length = 0

    for num in lst:
        sum+=num  
        length+=1

    mean = sum/length
    
    sum2 = 0
    
    for num in lst:
        sum2+=num**2
        
    meanSquares = sum2/length

    deviation2 = meanSquares-mean**2

    deviation = sqrt(deviation2)
    
    return deviation

def std_builtin(lst):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().
    Parameters
    ----------
    x: Sequence of numbers
    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    mean = sum(lst)/len(lst)
    
    sum2 = 0
    
    for num in lst:
        sum2+=num**2
    
    meanSquares = sum2/len(lst)
    
    deviation2 = meanSquares-mean**2

    deviation = sqrt(deviation2)
    
    return deviation

if __name__ == '__main__':
    num_lst = [1, 2, 3, 4, 5]
    
    print(f'Standard deviation of the list: {num_lst} using loops is: {std_loops(num_lst):.3f}')
    print(f'Standard deviation of the list: {num_lst} using sum() and len() is: {std_builtin(num_lst):.3f}')
    print(f'Standard deviation of the list: {num_lst} using NumPY is: {np.std(num_lst):.3f}')
    
    
        
    
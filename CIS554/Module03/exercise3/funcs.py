"""
Module with range-based for-loop functions.

Author: William R. Lange
Date: 2026-01-18
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1
    
    0! is 1.  Factorial is undefined for integers < 0.
    
    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120
    
    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """

    a=1

    if n<0:
        return 
    else:
        for i in range(1, n+1):
            a *=i

    return a



def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)
    
    Note that this tuple is the reverse of tuple(range(a,b))
    
    Parameter a: the "start" of the range
    Precondition: a is an int <= b
    
    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    pass

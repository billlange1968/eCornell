"""  
A function to check the validity of a numerical string

Author: William R. Lange
Date: 2026-01-16
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    
    result = False
    l=len(s)

    if l==1 and s[0]=='0': # Handle one zero
        result = True
    elif l>1 and s[0]=='0': # Handle leading zero
        result = False
    elif l<=3 and introcs.isnumeric(s)==True: # Handle 1 through 999
        result = True
    elif l==4: # Handle only four characters
        result = False
    elif l>4 and s[-4]!=',': # Handle no comma in 4th position when more than 4 chars
        result = False
    elif l<=7: # Handle 1,000 to 999,999
        t=s[0:-4]
        if introcs.isnumeric(t)==True:
            result = True

    return result
    

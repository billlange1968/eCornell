"""
The functions for the course project.
Author: William R. Lange
Date: 12/15/2025
"""
import introcs

def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """ 

    assert type(s)==str, "Precondition violation."

    # The function matching_parens is actually the trickiest of the two to implement,
    # so we will get you started with some pseudocode. To complete this function,
    # you should read the specification for find_str in the string functions for 
    # the IntroCS API. Note that this function returns -1 if a string is not found. 
    # So if you search for something after a failed search, you are restarting the 
    # search at position 0.
    
    #With this in mind, implement this function using the following pseudocode

    # Search for the first open parens '('
    # Search for the first close parens ')' AFTER the open parens
    # Compare both searches to -1 and return True if BOTH are not -1  

    pos1 = introcs.find_str(s,'(',start=0)
    pos2 = introcs.find_str(s,')',start=pos1+1)
    return pos1!=-1 and pos2!=-1

def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """

    assert type(s)==str, "Precondition violation."
    assert matching_parens(s)==True, "Precondition violation."

    pos1 = introcs.find_str(s,'(',start=0)
    pos2 = introcs.find_str(s,')',start=pos1+1)
    return s[pos1+1:pos2]

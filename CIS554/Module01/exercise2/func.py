"""  
A function to extract names from e-mail addresses.

Author: William R. Lange
Date: 2026-01-14
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.
    
    We assume (see the precondition below) that the e-mail address is in one of
    two forms:
        
        last.first@megacorp.com
        first.last@mompop.net
    
    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed 
    to be exactly as shown.
    
    The function preserves the capitalization of the e-mail address.
    
    Examples: 
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'
    
    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-else statement in this function.
    
    result =''

    if 'megacorp.com' in s:
        a=introcs.find_str(s,'@')
        d=introcs.find_str(s,'.')
        result=s[d+1:a]
    elif 'mompop.net' in s:
        d=introcs.find_str(s,'.')
        result=s[0:d]
    
    return result

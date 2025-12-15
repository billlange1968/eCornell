"""
The test script for the course project.
Author: William R. Lange
Date: 12/15/2025
"""
import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    result = funcs.matching_parens('A (B) C')
    introcs.assert_true(result) 

    result = funcs.matching_parens('A (B) (C)')
    introcs.assert_true(result) 

    result = funcs.matching_parens('A ((B) (C))')
    introcs.assert_true(result) 
    
    result = funcs.matching_parens('(A)')
    introcs.assert_true(result) 

    result = funcs.matching_parens('()')
    introcs.assert_true(result) 

    result = funcs.matching_parens('A )B( C')
    introcs.assert_false(result) 

    result = funcs.matching_parens('')
    introcs.assert_false(result) 
    
    result = funcs.matching_parens(')')
    introcs.assert_false(result) 

    result = funcs.matching_parens('(')
    introcs.assert_false(result) 

def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')

    result = funcs.first_in_parens('A (B) C')
    introcs.assert_equals('B',result) 

    result = funcs.first_in_parens('A (B) (C)')
    introcs.assert_equals('B',result) 

    result = funcs.first_in_parens('A ((B) (C))')
    introcs.assert_equals('(B',result) 
    
    result = funcs.first_in_parens('(A)')
    introcs.assert_equals('A',result) 
    
    result = funcs.first_in_parens('()')
    introcs.assert_equals('',result) 

# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')

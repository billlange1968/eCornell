"""  
A test script for the function iso_8601.

Author: William R. Lange
Date: 2026-01-17
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    
    result = func.iso_8601('09:30:15')
    introcs.assert_equals(True,result)

    result = func.iso_8601('99:99:99')
    introcs.assert_equals(False,result)


if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')

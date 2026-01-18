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
    
    s='09:30:15'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(True,result)

    s='99:99:99'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='12:5:05'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s=('12:05:5')
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='2:05:05'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(True,result)

    s='-2:05:05'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='02:-5:05'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='02:15:-5'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='12:15'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

    s='12:15:99'
    print('Testing: '+s)
    result = func.iso_8601(s)
    introcs.assert_equals(False,result)

if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')

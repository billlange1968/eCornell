"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: William R. Lange
Date:   2025-12-24
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")

    result = currency.before_space("Hello World")
    introcs.assert_equals("Hello", result)

    result = currency.before_space(" Hello World")
    introcs.assert_equals("", result)

    result = currency.before_space("Hello World ")
    introcs.assert_equals("Hello", result)

    result = currency.before_space("Hello  World")
    introcs.assert_equals("Hello", result)

    result = currency.before_space(" Hello")
    introcs.assert_equals("", result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    # after_space('Hello World') returns 'World'
    result = currency.after_space("Hello World")
    introcs.assert_equals("World", result)

    result = currency.after_space(" Hello World")
    introcs.assert_equals("Hello World", result)

    result = currency.after_space("Hello  World")
    introcs.assert_equals(" World", result)

    result = currency.after_space("Hello ")
    introcs.assert_equals("", result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    result = currency.first_inside_quotes('""')
    introcs.assert_equals("", result)

    result = currency.first_inside_quotes('"abc"')
    introcs.assert_equals("abc", result)

    # Example: first_inside_quotes('A "B C" D') returns 'B C'
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals("B C", result)

    # Example: currency.first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    # because it only picks the first such substring.
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals("B C", result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

    result = currency.get_src(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    )
    introcs.assert_equals("2 United States Dollars", result)

    result = currency.get_src(
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'
    )
    introcs.assert_equals("", result)

    result = currency.get_src(
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    )
    introcs.assert_equals("2 United States Dollars", result)

    result = currency.get_src(
        '{"success":false,"src": "","dst":"","error":"Source currency code is invalid."}'
    )
    introcs.assert_equals("", result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

    result = currency.get_dst(
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'
    )
    introcs.assert_equals("", result)

    result = currency.get_dst(
        '{"success":false,"src": "","dst": "","error":"Source currency code is invalid."}'
    )
    introcs.assert_equals("", result)

    result = currency.get_dst(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    )
    introcs.assert_equals("1.772814 Euros", result)

    result = currency.get_dst(
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    )
    introcs.assert_equals("1.772814 Euros", result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")

    # a test with an error message and no spaces after the colon for "error" or "success"
    result = currency.has_error(
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'
    )
    introcs.assert_true(result)

    # a test with no error message and spaces after the colon for "error" or "success"
    result = currency.has_error(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    )
    introcs.assert_false(result)

    # a test with an error message and spaces after the colon for "error" or "success"
    result = currency.has_error(
        '{"success": false,"src":"","dst":"","error": "Source currency code is invalid."}'
    )
    introcs.assert_true(result)

    result = currency.has_error(
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    )
    introcs.assert_false(result)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")

    # a test with valid currencies and non-negative amount
    result = currency.service_response("USD", "EUR", 2.5)
    introcs.assert_equals(
        '{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}',
        result,
    )

    # a test with valid currencies and negative amount
    result = currency.service_response("EUR", "USD", -2.5)
    introcs.assert_equals(
        '{"success": true, "src": "-2.5 Euros", "dst": "-2.8203748390976155 United States Dollars", "error": ""}',
        result,
    )

    # a test with an invalid src and dst currency
    result = currency.service_response("XXX", "XXX", 1000.0)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for currency XXX is not present."}',
        result,
    )

    # a test with an invalid src currency
    result = currency.service_response("XXX", "CNH", 1000.0)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for currency XXX is not present."}',
        result,
    )

    # a test with an invalid dst currency
    result = currency.service_response("PEN", "XXX", 5000.0)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for currency XXX is not present."}',
        result,
    )


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")

    response = currency.iscurrency("USD")
    introcs.assert_true(response)

    response = currency.iscurrency("XXX")
    introcs.assert_false(response)


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")

    response = currency.exchange("USD", "EUR", 2.5)
    introcs.assert_floats_equal(2.2160175, response)

    response = currency.exchange("USD", "EUR", -2.5)
    introcs.assert_floats_equal(-2.2160175, response)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")

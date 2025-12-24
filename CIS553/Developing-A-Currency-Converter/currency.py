"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: William R. Lange
Date:   2025-12-24
"""

import introcs

APIKEY = "UuGTskp8aKGq5tVQcY0XMBd2WW9I8Vdc3Vssb4FYFMge"


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert(type(s) == str)
    assert(introcs.count_str(s, " ") >= 1)

    result = introcs.find_str(s, " ")
    return s[:result]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert(type(s) == str)
    assert(introcs.count_str(s, " ") >= 1)

    result = introcs.find_str(s, " ")
    return s[result + 1 :]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert(type(s) == str)
    assert(introcs.count_str(s, '"') >= 2)

    pos1 = introcs.find_str(s, '"')
    pos2 = introcs.find_str(s, '"', pos1 + 1)
    return s[pos1 + 1 : pos2]


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert(type(json) == str)

    pos = introcs.find_str(json, '"src"')  # Find the position of '"src"'
    src_val = first_inside_quotes(
        json[pos + len('"src"') :]
    )  # Find first substring between quotes after '"src"'
    return src_val


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert(type(json) == str)

    pos = introcs.find_str(json, '"dst"')  # Find the position of '"dst"'
    dst_val = first_inside_quotes(
        json[pos + len('"dst"') :]
    )  # Find first substring between quotes after '"dst"'
    return dst_val


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert(type(json) == str)

    # Find the position of '"error"'
    error_pos = introcs.find_str(json, '"error"')

    # Find first substring between quotes after '"error"'
    error_val = first_inside_quotes(json[error_pos + len('"error"') :])

    return error_val != ""


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    choose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition: src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition: dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """
    assert(type(src) == str and src != "" and introcs.isalpha(src))
    assert(type(dst) == str and dst != "" and introcs.isalpha(dst))
    assert(type(amt) == int or type(amt) == float)

    q = introcs.urlread(
        "https://ecpyfac.ecornell.com/python/currency/fixed?src="
        + src
        + "&dst="
        + dst
        + "&amt="
        + str(amt)
        + "&key="
        + APIKEY
    )
    return q


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert (type(currency) == str and currency != "" and introcs.isalpha(currency))

    response = service_response(currency, currency, 1.0)
    return not has_error(response)


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """
    assert(type(src) == str and iscurrency(src))
    assert(type(dst) == str and iscurrency(dst))
    assert(type(amt) == int or type(amt) == float)

    response = service_response(src, dst, amt)
    result = float(before_space(get_dst(response)))

    return result

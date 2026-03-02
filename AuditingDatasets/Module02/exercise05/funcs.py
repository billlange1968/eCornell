"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: William R. Lange
Date:   2026-03-01
"""

import dateutil.parser
import datetime
import pytz

def str_to_time(timestamp,tzsource=None):
    """
    Returns the datetime object for the given timestamp (or None if timestamp is 
    invalid).
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a time zone, then it should keep that time zone even if
    the value for tzsource is not None.  Otherwise, if timestamp has no time zone 
    and tzsource is not None, then this function will use tzsource to assign 
    a time zone to the new datetime object.
    
    The value for tzsource can be None, a string, or a datetime object.  If it 
    is a string, it will be the name of a time zone, and it should localize the 
    timestamp.  If it is another datetime, then the datetime object created from 
    timestamp should get the same time zone as tzsource.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tzsource: The time zone to use (OPTIONAL)
    Precondition: tzsource is either None, a string naming a valid time zone,
    or a datetime object.
    """
    # HINT: Use the code from the previous exercise and add time zone handling.
    # Use localize if tzsource is a string; otherwise replace the time zone if not None
       
    # Use the parse function in dateutil.parser to
    # convert the timestamp to a datetime object.
    
    try:
        dt = dateutil.parser.parse(timestamp)
    except:
        return None
    
    if tzsource == None:
        return dt

    if dt.tzinfo != None:
        return dt

    # The value for tzsource can be None, a string, or a datetime object.    
    
    # tzsource == None is already handled.

    # Handle tzsource as string
    if isinstance(tzsource,str):
        tz = pytz.timezone(tzsource)
        ndt = tz.localize(dt)
        return ndt

    # Handle tzsource as datetime
    if isinstance(tzsource,datetime.datetime):
        ndt = dt.replace(tzinfo=tzsource.tzinfo)
        return ndt

    # If we get here, something went amiss
    return None

def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day, False otherwise (and 
    returns None if a key does not exist in the dictionary).
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.
    
    A daycycle dictionary has keys for several years (as strings).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects using data from the daycycle dictionary.  Also, if the time
    parameter does not have a timezone, we assume that it is in the same timezone 
    as the daycycle dictionary.
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
  
    year_str = time.strftime("%Y")
    mmdd_str = time.strftime("%m-%d")

    try:
        days = daycycle[year_str]
    except:
        return None
    
    if days==None:
        return None

    try:
        daycycle_tz = daycycle['timezone']
    except:
        return None

    cycle=days[mmdd_str]

    sunrise=cycle['sunrise']    
    sunrise_str = time.strftime("%Y-%m-%d") + "T" + sunrise
    sunrise_dtz = str_to_time(sunrise_str,daycycle_tz)
    #print("Sunrise: " + str(sunrise_dtz))
    
    sunset=cycle['sunset']    
    sunset_str = time.strftime("%Y-%m-%d") + "T" + sunset
    sunset_dtz = str_to_time(sunset_str,daycycle_tz)
    #print("Sunset: " + str(sunset_dtz))

    t_tz = time.tzinfo

    if t_tz == None:
        #print("time doesn't have timezone information")
        tz = pytz.timezone(daycycle_tz)
        time = tz.localize(time)       

    #print("time: " + str(time))

    if time <= sunrise_dtz:
        #print("time <= sunrise_dtz")
        return False
    elif sunset_dtz <= time:
        #print("sunset_dtz <= time") 
        return False
    else:
        #print("time is between sunrise and sunset")   
        return True

import logging
#import datetime
from dateutil.parser import *
from dateutil.tz import *
from datetime import *
#import dateutil.parser
import time
import math
#import timeconverter
from config import dashboard

logger = logging.getLogger(__name__)

def convert_value(value, conversion = None):
    if value == None:
        return 'N/A'
    logger.debug('Converting value:'+str(value))
    if not conversion:
        return str(value)
    if conversion == 'K_C':
        return "{0:.1f}".format(value - 273.15)
    if conversion == 'm_m':
        return "{0:.1f}".format(value)
    if conversion == 'int_str':
        return str(int(value))
    if conversion == '%':
        return str(int(value * 100))
    if conversion == 'Pa_hPa':
        return str(int(value / 100))
    if conversion == 'rad_deg':
        return str(int(math.degrees(value)))
    if conversion == 'm/s_knots':
        return "{0:.1f}".format(value * 1.944)
    if conversion == 'm_NM':
        return "{0:.1f}".format(value / 1852)
    if conversion == 'Z_local_2':
        return tconvert('%H:%M',value)
    if conversion == 'Z_local_3':
        return tconvert('%H:%M:%S',value)
    if conversion == '.x':
        return "{0:.1f}".format(value)
    if conversion == '.xx':
        return "{0:.2f}".format(value)
##Older conversions for backward compability
    if conversion == 'Pa':
        return str(int(value / 100))
    if conversion == 'rad':
        return str(int(math.degrees(value)))
    if conversion == 'm/s':
        return "{0:.1f}".format(value * 1.944)
    if conversion == 'K':
        return "{0:.1f}".format(value - 273.15)
    if conversion == 'm':
        return "{0:.1f}".format(value)
## Default if no conversions was found
    return 'Undef conv.'

def tconvert(printformat,dtvalue, latlon=None):

    # timeoffset=int(dashboard['TZ_default_offset'])
    # l_zone=timezone(timedelta(seconds=timeoffset))
    
    # utc_value=datetime.fromisoformat(utc_time[0:len(dtvalue)-1] + "+00:00")
    # local_value=dtvalue.astimezone(l_zone)

    # return local_value.strftime(printformat)
    
    timeoffset=int(dashboard['TZ_default_offset'])

    delta=timedelta(seconds=timeoffset)
    logger.debug("Date/Time to convert: " + str(dtvalue))
    local_dtvalue=dtvalue+delta

    logger.debug("Data/Time after convert:" + local_dtvalue.strftime(printformat))
    return local_dtvalue.strftime(printformat)

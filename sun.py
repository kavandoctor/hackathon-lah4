from datetime import date, timedelta, datetime, time, tzinfo
import math
import datetime
import pytz
from tzwhere import tzwhere
import time
from geopy.geocoders import Nominatim
from Sun import *

def calculate(s):

    geolocator = Nominatim()
    location = geolocator.geocode(s)
    w = tzwhere.tzwhere()
    if str(location) != 'None':
        timezone_str = w.tzNameAt(location.latitude, location.longitude)
        timezone = pytz.timezone(timezone_str)
        dt = datetime.datetime.now()
        s = str(timezone.utcoffset(dt)).split(",")
        offsethr = 0
        if s[0] == '-1 day':
            offsethr-=24
            s.pop(0)
        tme = s[0].split(':')
        offsethr += int(tme[0])
        offsetmin = int(tme[1])

        coords = {'longitude' : location.longitude, 'latitude' : location.latitude }

        sun = Sun()
        sunrise = sun.getSunriseTime( coords )
        risehr = sunrise['hr']+offsethr
        risemin = int(sunrise['min']+offsetmin)
        sunset = sun.getSunsetTime( coords )
        sethr = sunset['hr']+offsethr-12
        setmin = int(sunset['min']+offsetmin)
        if risemin >= 60:
            risemin -= 60
            risehr += 1
        if setmin >= 60:
            setmin -= 60
            sethr += 1
        if sethr < 0:
            sethr+=24
        if risehr < 0:
            risehr += 24
        risemin = str(risemin)
        setmin = str(setmin)
        if len(risemin) == 1:
            risemin = '0'+risemin
        if len(setmin) == 1:
            setmin = '0'+setmin
        sunrise = 'Sunrise: '+str(risehr)+":"+str(risemin)+' AM'
        sunset = "Sunset: "+str(sethr)+":"+str(setmin)+' PM'
        return [sunrise,sunset,str(location)]
    else:
        return []
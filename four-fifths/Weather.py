"""

0	tornado
1	tropical storm
2	hurricane
3	severe thunderstorms
4	thunderstorms
5	mixed rain and snow
6	mixed rain and sleet
7	mixed snow and sleet
8	freezing drizzle
9	drizzle
10	freezing rain
11	showers
12	showers
13	snow flurries
14	light snow showers
15	blowing snow
16	snow
17	hail
18	sleet
19	dust
20	foggy
21	haze
22	smoky
23	blustery
24	windy
25	cold
26	cloudy
27	mostly cloudy (night)
28	mostly cloudy (day)
29	partly cloudy (night)
30	partly cloudy (day)
31	clear (night)
32	sunny
33	fair (night)
34	fair (day)
35	mixed rain and hail
36	hot
37	isolated thunderstorms
38	scattered thunderstorms
39	scattered thunderstorms
40	scattered showers
41	heavy snow
42	scattered snow showers
43	heavy snow
44	partly cloudy
45	thundershowers
46	snow showers
47	isolated thundershowers
3200	not available

"""

import urllib2,json

def getTemp():
    url=urllib2.urlopen("http://weather.yahooapis.com/forecastrss?w=2459115")
    d=url.read()
    y = "temp="
    x = d.find(y)
    x = d[x+6:x+8]
    return int(x)

def getHigh():
    url=urllib2.urlopen("http://weather.yahooapis.com/forecastrss?w=2459115")
    d=url.read()
    y = "high="
    x = d.find(y)
    x = d[x+6:x+8]
    return int(x)

def getLow():
    url=urllib2.urlopen("http://weather.yahooapis.com/forecastrss?w=2459115")
    d=url.read()
    y = "low="
    x = d.find(y)
    x = d[x+5:x+7]
    return int(x)

def getForecast():
    url=urllib2.urlopen("http://weather.yahooapis.com/forecastrss?w=2459115")
    d=url.read()
    y = "code="
    x = d.find(y)
    x = d[x+6:x+8]
    return int(x)

def getForecastString(code):
    d1 = ["tornado","tropical storm","hurricane","severe thunderstorms","thunderstorms","mixed rain and snow","mixed rain and sleet","mixed snow and sleet","freezing drizzle","drizzle","freezing rain","showers","showers","snow flurries","light snow showers","blowing snow","snow","hail","sleet","dust","foggy","haze","smoky","blustery","windy","cold","cloudy","mostly cloudy (night)","mostly cloudy (day)","partly cloudy (night)","partly cloudy (day)","clear (night)","sunny","fair (night)","fair (day)","mixed rain and hail","hot","isolated thunderstorms","scattered thunderstorms","scattered thunderstorms","scattered showers","heavy snow","scattered snow showers","heavy snow","partly cloudy","thundershowers","snow showers","isolated thundershowers"]
    if code==3200: return "not available"
    return d1[code]


def getForecastURL(code):
    d2 = ["tornado", #???
          "tropical storm", #??? 
          "hurricane", #???
          "thunderstorms.png", #severe ooh
          "thunderstorms.png",
          "mixed rain and snow.png",
          "mixed rain and sleet.png", #make
          "mixed snow and sleet.png", #make
          "freezing drizzle.png", #MAKE THIS
          "drizzle.png",
          "freezing rain.png",
          "showers.png",
          "showers.png",
          "snow flurries.png", #flurries with sun?
          "light snow.png", #MAKE THIS
          "blowing snow.png",
          "snow.png",
          "hail.png",
          "sleet.png",
          "haze.png", #dust?
          "haze.png", #fog?
          "haze.png",
          "haze.png", #smoke?
          "windy.png",
          "windy.png",
          "cold.png", #make with icicles
          "cloudy.png",
          "mostly cloudy.png",
          "mostly cloudy.png",
          "partly cloudy.png",
          "partly cloudy.png",
          "fair night.png",
          "sunny.png",
          "fair night.png",
          "fair.png",
          "mixed rain and hail.png", #MAKE THIS
          "sunny.png", #recolor for yellow ring/rays
          "scattered thunderstorms.png", #scattered with sun like other scattered
          "scattered thunderstorms.png", #ditto
          "scattered thunderstorms.png", #ditto
          "scattered showers.png",
          "snow.png",
          "snow.png", #scattered snow showers with sun?
          "snow.png", #heavier than normal  snow
          "partly cloudy.png",
          "thunderstorms.png",
          "snow.png",
          "thunderstorms.png" #scattered thundershowers with sun as above
          ]
    if code==3200: return "unavailable.png"
    return d2[code]

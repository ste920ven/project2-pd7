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
    d1 = ["tornado",
          "tropical storm", 
          'hurricane',
          "severe thunderstorms",
          "thunderstorms",
          "mixed rain and snow",
          "mixed rain and sleet",
          "mixed snow and sleet",
          "freezing drizzle",
          "drizzle",
          "freezing rain",
          "showers",
          "showers",
          "snow flurries",
          "light snow showers",
          "blowing snow",
          "snow",
          "hail",
          "sleet",
          "dust",
          "foggy",
          "haze",
          "smoky",
          "blustery",
          "windy",
          "cold",
          "cloudy",
          "mostly cloudy (night)",
          "mostly cloudy (day)",
          "partly cloudy (night)",
          "partly cloudy (day)",
          "clear (night)",
          "sunny",
          "fair (night)",
          "fair (day)",
          "mixed rain and hail",
          "hot",
          "isolated thunderstorms",
          "scattered thunderstorms",
          "scattered thunderstorms",
          "scattered showers",
          "heavy snow",
          "scattered snow showers",
          "heavy snow",
          "partly cloudy",
          "thundershowers",
          "snow showers",
          "isolated thundershowers"]
    return d1[code]


def getForecastURL(code):
    d1 = ["tornado", #???
          "tropical storm", #??? 
          "hurricane", #???
          "thunderstorms.png", #severe ooh
          "thunderstorms.png"
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
    return d1[code]

from flask import Flask, render_template, request, redirect, url_for
from ua_parser import user_agent_parser
import extractor, Weather, MTAService

app = Flask(__name__)

@app.route('/')
def main():
    data     = extractor.loadStuySite()
    news     = extractor.getNews(data[0])
    schedule = extractor.getSchedule(data[1],data[2])
    bellDay  = extractor.getBellDay(schedule)
    gymDay   = extractor.getGymDay(schedule)
    date     = extractor.getDate()

    temp           = Weather.getTemp()
    forecastCode   = Weather.getForecast()
    forecastURL    = url_for('static',filename="images/"+Weather.getForecastURL(forecastCode))
    forecastString = Weather.getForecastString(forecastCode)

    delays = ['A','B','fred'] #MTAService.getDelays(MTAService.getSubways())

    #detecting a mobile device
    user_agent_string = request.user_agent.string
    mobile_user_agent_families = ['Firefox Mobile','Opera Mobile','Opera Mini','Mobile Safari','webOS','IE Mobile','Playstation Portable','Nokia','Blackberry','Palm','Silk','Android','Maemo','Obigo','Netfront','AvantGo','Teleca','SEMC-Browser','Bolt','Iris','UP.Browser','Symphony','Minimo','Bunjaloo','Jasmine','Dolfin','Polaris','BREW','Chrome Mobile','UC Browser','Tizen Browser']
    mobile_os_families = ['Windows Phone 6.5','Windows CE','Symbian OS','iOS']
    ua_family = user_agent_parser.ParseUserAgent(user_agent_string)['family']
    os_family = user_agent_parser.ParseOS(user_agent_string)['family']

    if ua_family in mobile_user_agent_families or os_family in mobile_os_families:
        return render_template('mobile.html',
                               news=news,
                               schedule=schedule,
                               bellDay=bellDay,
                               gymDay=gymDay,
                               date=date,
                               temp=temp,
                               forecastURL=forecastURL,
                               forecastString=forecastString,
                               delays=delays)

    else:
        return render_template('home.html',
                               news=news,
                               schedule=schedule,
                               bellDay=bellDay,
                               gymDay=gymDay,
                               date=date,
                               temp=temp,
                               forecastURL=forecastURL,
                               forecastString=forecastString,
                               delays=delays)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7305, debug=True)

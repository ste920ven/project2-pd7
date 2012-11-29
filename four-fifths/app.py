from flask import Flask, render_template, request, redirect, url_for
from ua_parser import user_agent_parser
#from mobile.sniffer.detect import  detect_mobile_browser
#from mobile.sniffer.utilities import get_user_agent
import extractor

app = Flask(__name__)


'''
#use mobile site if needed
_render_template = render_template
def _my_render_template(*args, **kwargs):
    if detect_mobile_browser(request.user_agent.string):
        args = ('m/' + args[0],) + args[1:]
    return _render_template(*args, **kwargs)
render_template = _my_render_template
'''

@app.route('/')
def main():
    #device = user_agent_parser.ParseDevice(request.user_agent.string)
    #print device

    user_agent_string = request.user_agent.string

    mobile_user_agent_families = ['Firefox Mobile','Opera Mobile','Opera Mini','Mobile Safari','webOS','IE Mobile','Playstation Portable','Nokia','Blackberry','Palm','Silk','Android','Maemo','Obigo','Netfront','AvantGo','Teleca','SEMC-Browser','Bolt','Iris','UP.Browser','Symphony','Minimo','Bunjaloo','Jasmine','Dolfin','Polaris','BREW','Chrome Mobile','UC Browser','Tizen Browser']

    # Some select mobile OSs report a desktop browser.
    # make sure we note they're mobile
    mobile_os_families = ['Windows Phone 6.5','Windows CE','Symbian OS']

    ua_family = user_agent_parser.ParseUserAgent(user_agent_string)['family']
    print ua_family

    os_family = user_agent_parser.ParseOS(user_agent_string)['family']
    print os_family

# Bits to match some of dmolsen's device booleans.
    if ua_family in mobile_user_agent_families:
        is_mobile = True
    elif os_family in mobile_os_families:
        is_mobile = True
    else:
        is_mobile = False

    if is_mobile:
        redirect(url_for('mobile'))

    else:
        data     = extractor.loadStuySite()
        news     = extractor.getNews(data[0])
        schedule = extractor.getSchedule(data[1],data[2])
        bellDay  = extractor.getBellDay(schedule)
        gymDay   = extractor.getGymDay(schedule)
        date     = extractor.getDate()
        return render_template('home.html',
                               news=news,
                               schedule=schedule,
                               bellDay=bellDay,
                               gymDay=gymDay,
                               date=date)

'''
    # Get HTTP_USER_AGENT from HTTP request object
    ua = request.user_agent.string
    if ua and detect_mobile_browser(ua):
        # Redirect the visitor from a web site to a mobile site
        redirect(url_for('mobile'))
    else:
'''

@app.route('/m')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7205, debug=True)

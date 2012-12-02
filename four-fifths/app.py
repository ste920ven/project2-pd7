from flask import Flask, render_template, request, redirect, url_for
from mobile.sniffer.detect import  detect_mobile_browser
from mobile.sniffer.utilities import get_user_agent
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
    data     = extractor.loadStuySite()
    news     = extractor.getNews(data[0])
    schedule = extractor.getSchedule(data[1],data[2])
    bellDay  = extractor.getBellDay(schedule)
    gymDay   = extractor.getGymDay(schedule)
    date     = extractor.getDate()

    # Get HTTP_USER_AGENT from HTTP request object
    ua = request.user_agent.string
    if ua and detect_mobile_browser(ua):
        # Redirect the visitor from a web site to a mobile site
        redirect(url_for('mobile'))
    else:
        return render_template('home.html',
                               news=news,
                               schedule=schedule,
                               bellDay=bellDay,
                               gymDay=gymDay,
                               date=date)

@app.route('/m')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7205, debug=True)

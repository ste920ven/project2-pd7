from flask import Flask, render_template, request, redirect, url_for
import extractor

app = Flask(__name__)

"""
#use mobile site if needed
_render_template = flask.render_template
def _my_render_template(*args, **kwargs):
    if detect_mobile_browser(flask.request.user_agent.string):
        args = ('m/' + args[0],) + args[1:]
    return _render_template(*args, **kwargs)
flask.render_template = _my_render_template
"""


@app.route('/')
def main():
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

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7205, debug=True)

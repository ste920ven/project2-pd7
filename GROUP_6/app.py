from flask import Flask,session,url_for,request,redirect,render_template
import db	
import util

app = Flask(__name__)
#app.secret_key = "secret"


@app.route('/', methods = ['GET', 'POST'])
def home():
	global tag
	
	if request.method == "GET":
		url_list = util.send_image_links(20)
		print url_list
		return render_template("gallery.html",url_list = url_list)

@app.route('/gallery/<tag>', methods=['GET', 'POST'])
def gallery():
	pass

@app.route('/slideshow/<tag>', methods=['GET', 'POST'])
def slide():
	global tag
	if request.method=="GET":
		taglist = db.getTaglist()
		piclist = db.getPics(tag)
		return render_template("slide.html", taglist = taglist, tags =tags)
	else:	
		url = request.form['hidSrc']
		return redirect(url_for("/slideshow/" + url ))
		
		 	 	
if __name__=="__main__":
    app.debug=True
    app.run(port=5000)

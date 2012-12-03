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

@app.route('/slideshow/<tag>', methods=['GET', 'POST'])
def slide():
	global tag
	if request.method=="GET":
		taglist = db.getTaglist()
		piclist = db.getPics(tag)
		return render_template("slide.html", taglist = taglist, piclist =piclist)
	else:	
		url = request.form['hidSrc']
		return redirect(url_for("/image/" + url ))
		
@app.route('/image/<pic>', methods=['GET', 'POST'])
def _image():
	if request.method=="GET":
		taglist = db.getTaglist()
		tags = db.getTags(pic)
		commentlist = db.getComments(pic)
		return render_template("image.html", taglist = taglist, tags =tags, commentlist = commentlist, pic = pic)
	else:	
		button = request.form['button']
				
		if button=="submit":
			aComment = request.form['comment']
			db.addComment(pic,aComment)
		elif button == "submitnewtag":
			if request.form['Addnewtag']:
				aTag = request.form['Addnewtag']
				db.addTag(pic,aTag)
			else:
				aTag =  request.form['select1']
				db.addTag(pic,aTag)
		
		 	 	
if __name__=="__main__":
    app.debug=True
    app.run(port=5000)

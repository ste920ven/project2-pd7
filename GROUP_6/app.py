from flask import Flask,session,url_for,request,redirect,render_template
import api,db	

app = Flask(__name__)
#app.secret_key = "secret"

app.route('/', methods=['GET', 'POST'])
def main():
	if request.method=="GET":
		return render_template("home.html")
        if request.method=="POST":
        	
@app.route('/gallery/<tag>', methods=['GET', 'POST'])
def gallery():
	

@app.route('/slideshow/<tag>', methods=['GET', 'POST'])
def slide():
	if request.method=="GET":
		pic = request.get('current').href
		taglist = db.getTaglist()
		tags = db.getTags(pic)
		piclist = db.getPics(<tag>)
		commentlist = db.getComments(pic)
		return render_template("slide.html", taglist = taglist, tags =tags, piclist =piclist, commentlist = commentlist, url = url)
	else:	
		button = request.form['button']
		pic = request.get('current').href
		
		if button=="submit":
			aComment = request.form['comment']
			db.addComment(pic,aComment)
		elif button == "submitnewtag":
			if request.form['Addnewtag']
				aTag = request.form['Addnewtag']
				db.addTag(pic,aTag)
			else:
				aTag =  request.form['select1']
				db.addTag(pic,aTag)
		
		 	 	
if __name__=="__main__":
    app.debug=True
    app.run(port=5300)

from flask import Flask,render_template
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

 #MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'blog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
api = Api(app)
 
# basic route
@app.route("/")
def main():
   return "Hello"

@app.route("/showAddBlog")
def showAddBlog():
	return render_template('blog.html')

@app.route('/addBlog',methods=['POST'])
def addBlog():
	_title = request.form['inputTitle']
	_description = request.form['inputDescription']
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.callproc('sp_addBlog',(_title,_description,))
	data = cursor.fetchall()
	return render_template('views.py')
	
'''@app.route('/getBlog')
def getBlog():
    try:
        if session.get('user'):
            _user = session.get('user')

            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_GetBlogByUser',(_user,))
            blogs = cursor.fetchall()

            blogs_dict = []
            for blog in blogs:
                blog_dict = {
                        'Id': blog[0],
                        'Title': blog[1],
                        'Description': blog[2],
                        'Date': blog[4]}
                blogs_dict.append(blog_dict)

            return json.dumps(blogs_dict)
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
	return render_template('error.html', error = str(e))'''

if __name__ == "__main__":
	app.jinja_env.globals.update(chr=chr)
	app.run(debug=True,threaded=True)
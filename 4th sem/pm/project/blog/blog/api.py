from flask import Flask,render_template
app = Flask(__name__)

# basic route
@app.route("/")
def main():
   return "Hello"

@app.route("/showAddBlog")
def showAddBlog():
    return render_template('blog.html')

if __name__ == "__main__":
   app.run()
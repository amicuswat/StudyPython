from flask import Flask, render_template

#__name__ is a special variable that receives the name of python script
# if we import this script the __name__ will be script1
# but if we execute this script the __name__ = __main__
app = Flask(__name__)

# @app.route('/') - with this we will find the page by localhost:5000
# if we change '/' to '/about/' the site will be accessed at localhost:5000/about
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

# bellow lines will not run if we import the script as the __name__ will be "script1"
# they run only if we execute this script so the __name__ will be "__main__"
if __name__ == "__main__":
    app.run(debug=True)

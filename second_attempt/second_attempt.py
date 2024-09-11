# Page Routing
import flask as f

app = f.Flask(__name__)

@app.route('/')
def homepage():
    return 'Home page'

@app.route('/page1')
def firstpage():
    return 'the first page'

@app.route('/page2')
def secondpage():
    return 'second page'

@app.route('/page1/subsection')
def subpage():
    return 'page1\'s subsection'

@app.route("/members/<string:name>/")
def hello(name):
    return f.render_template("the_template.html", name=name)



if __name__ == '__main__':
    app.run()
    
# Visit http://localhost:5000 after running

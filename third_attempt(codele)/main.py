# Page Routing
import flask as f

app = f.Flask(__name__)

@app.route('/')
def homepage():
    return f.render_template("home/template.html")

@app.route('/codele')
def codele():
    return f.render_template("codele/template.html")

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if f.request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/codele' to play codele"
    if f.request.method == 'POST':
        form_data = f.request.form
        return f.render_template('data.html',form_data = form_data)
 

if __name__ == '__main__':
    app.run()
    
# Visit http://localhost:5000 after running


# importing flask module fro
from flask import Flask, render_template,request

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route with url as /login
@app.route('/')
def index():
   return render_template('login.html')


@app.route('/FlaskTutorial',  methods=['POST'])
def success():
   if request.method == 'POST':
       startStop = request.form['Start']
       endStop = request.form['End']


       return render_template('success.html', Start=startStop,End = endStop)
   else:
       pass
if __name__ == "__main__":
   app.run()

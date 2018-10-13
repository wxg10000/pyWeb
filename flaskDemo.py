from flask import Flask,send_file
from flask import request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return send_file("__base__.html")

# @app.route('/',methods=['GET','POST'])
# def home():
#     return '__base__.html'

@app.route('/signin',methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
              <p>username:<input name="username"></p>
              <p>password:<input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>
    '''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello admin!</h3>'
    return '<h3>Bad username or password</h3>'




if __name__ == '__main__':
    app.run()
from flask import Flask
app = Flask(__name__)

#route是路徑
@app.route("/")
def hello_world():
    return '''
        <h1>Hello,world!</h1>
        <p>這是p</p>
    '''

@app.route("/name")
def hello_world1():
    return '''
        <ul>
            <li>主題</li>
            <li>產品</li>
        </ul>
    '''
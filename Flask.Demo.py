from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/home')
def home():
    return "home"

@app.route('/guest/<guest>')
def guest(guest):
    return 'Hello '+ guest

@app.route('/admin')
def admin():
    return 'Welcome Admin'

@app.route('/user/<access>')
def user(access):
    if access == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest=access))

if __name__ == '__main__':
    app.run()

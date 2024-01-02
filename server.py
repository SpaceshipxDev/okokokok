from datetime import timedelta
from flask import Flask, session, redirect, render_template
import os, uuid

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=30)

def create_unique_user_id():
    return str(uuid.uuid4())

@app.route('/')
def index():
    session.permanent = True
    if 'user_id' not in session:
        session['user_id'] = create_unique_user_id()
        return redirect('https://chat.hazl.org/')
    else:
        return redirect('https://chat.hazl.org/signin')

@app.route("/signin")
def signup():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

@app.route("/")
def login():
    return render_template('pages/auth/login.html')

@app.route("/forgot-password")
def forgot_password():
    return render_template('pages/auth/forgot_password.html')

@app.route("/verify-mfa", methods=['GET', 'POST'])
def verify_mfa():
    return render_template('pages/auth/verify.html')

@app.route("/set_password")
def set_password():
    return render_template('pages/auth/set_password.html')


if __name__=='__main__':
    app.run(debug=True)
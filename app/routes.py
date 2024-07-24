from flask import render_template, request, redirect, url_for
from app import app
from app.bot import generate_fake_accounts, send_comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_accounts = 50
    generate_fake_accounts(num_accounts)
    return redirect(url_for('index'))

@app.route('/start', methods=['POST'])
def start():
    url = request.form.get('url')
    send_comments(url)
    return redirect(url_for('index'))

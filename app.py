from flask import Flask, render_template, request, jsonify
import random
from faker import Faker

app = Flask(__name__)

fake = Faker()

# Generate random names for fake accounts
def generate_random_name():
    return fake.name()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_accounts = int(request.form.get('num_accounts', 0))
    if num_accounts <= 0:
        return jsonify({'error': 'Invalid number of accounts'}), 400
    
    fake_accounts = [generate_random_name() for _ in range(num_accounts)]
    return jsonify({'accounts': fake_accounts})

@app.route('/start', methods=['GET'])
def start_comments():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Here, you would handle the logic for starting the comment process
    return jsonify({'status': 'Comments have been sent!'})

if __name__ == '__main__':
    app.run(debug=True)

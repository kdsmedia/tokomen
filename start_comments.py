import time
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

app = Flask(__name__)
fake = Faker()

# Generate fake accounts
def generate_fake_accounts(num):
    return [fake.name() for _ in range(num)]

@app.route('/start', methods=['GET'])
def start_comments():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Generate 50 fake accounts
    fake_accounts = generate_fake_accounts(50)
    
    # Example process to send comments (replace with actual TikTok comment sending logic)
    for account in fake_accounts:
        driver.get(url)
        time.sleep(5)  # Simulate comment posting delay
        print(f"Comment posted by: {account}")

    driver.quit()
    return jsonify({'status': 'Comments have been sent!'})

if __name__ == '__main__':
    app.run(debug=True)

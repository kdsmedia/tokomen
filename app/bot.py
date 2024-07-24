from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from app.utils import generate_random_name

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  # Adjust path if necessary

def generate_fake_accounts(num_accounts):
    names = [generate_random_name() for _ in range(num_accounts)]
    # Implement account generation logic here with Selenium
    for name in names:
        print(f"Generated fake account with name: {name}")
        time.sleep(3)  # Simulate delay for each account generation

def send_comments(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    comments = load_comments()

    driver.get(url)
    for comment in comments:
        print(f"Sending comment: {comment}")
        # Implement commenting logic here
        time.sleep(5)  # Simulate delay for each comment

    driver.quit()

def load_comments():
    with open('comments.txt', 'r') as file:
        comments = file.readlines()
    return [comment.strip() for comment in comments]

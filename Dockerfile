# Use the official Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Install dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install dependencies for Selenium and Chrome
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatk-bridge2.0-0 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcups2 \
    libxtst6 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get -fy install

# Download and install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

# Copy application files
COPY . /app

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

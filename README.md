# Internet Speed Test Web App

A Flask-based web application that allows users to test their internet speed. The application measures download speed, upload speed, and ping.

## Features

- Real-time speed testing
- Modern and responsive UI
- Displays download speed, upload speed, and ping
- Asynchronous speed testing that doesn't block the UI

## Requirements

- Python 3.7+
- Flask
- speedtest-cli

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Amoako419/SpeedTest.git
cd SpeedTest
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the "Start Speed Test" button to begin the speed test.

## How it Works

The application uses the `speedtest-cli` library to perform the speed test. The test is run in a separate thread to prevent blocking the web interface. The results are updated in real-time as the test progresses.

## Note

The speed test may take a few minutes to complete, depending on your internet connection. Please be patient while the test is running. 
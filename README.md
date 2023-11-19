# GPT-2 Flask API

This project is a Flask-based web application that utilizes GPT-2, a language model by OpenAI, to generate text based on user input. It features a user-friendly interface and offers a unique experience with features like real-time typing effects.

## Features

- Text generation using GPT-2.
- Interactive web interface with dynamic effects.
- Automated testing with PyTest.

## Installation

### Prerequisites

- Python 3.9
- pip
- [WSL for Windows users](https://docs.microsoft.com/en-us/windows/wsl/install)

### Setup

1. **Clone the repository**:

git clone https://github.com/AayushRaghuvamshi/GPT-2-Flask-API.git
cd GPT-2-Flask-API

2. **Create and activate a virtual environment** (optional but recommended):

python3 -m venv .venv
source .venv/bin/activate # On Windows use .venv\Scripts\activate

3. **Install dependencies**:

pip install -r requirements.txt

## Running the Application

You can run the application either using Gunicorn in WSL (Windows Subsystem for Linux) or directly with Python on Windows.

### Using Gunicorn in WSL

1. **Start the Flask app with Gunicorn**:

cd src
gunicorn -w 4 -b 0.0.0.0:5000 main:app

2. **Access the application**:

- Open your web browser and go to `http://localhost:5000`.

### Directly on Windows

1. **Run the Flask app with Python**:

cd src
python3 main.py

2. **Access the application**:

- Open your web browser and navigate to the URL output by the Flask server (usually `http://127.0.0.1:5000` or `http://localhost:5000`).

Ensure you have all dependencies installed as per the instructions in the **Installation** section.

## Author

- **Aayush Raghuvamshi**

## Sources:

Button animation: https://www.youtube.com/watch?v=ueyRcYEmsrI&ab_channel=OnlineTutorials

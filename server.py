from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ NeuroX UI is online.'

@app.route('/query')
def query():
    cmd = request.args.get("cmd", "Hello")
    result = subprocess.run(['python3', 'main.py'], input=cmd, text=True, capture_output=True)
    return result.stdout.strip()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

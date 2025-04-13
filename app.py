from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Yerragunta Cloud Run Container!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use 8080 if set by Cloud Run, fallback to 5000
    app.run(host='0.0.0.0', port=port)

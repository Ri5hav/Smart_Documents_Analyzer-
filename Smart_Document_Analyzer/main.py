from app.routes import *
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Document Analyzer Ready'
if __name__ == '__main__':
    app.run(debug=True)
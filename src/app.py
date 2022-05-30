from flask import Flask

app = Flask(__name__)

@app.get(rule='/')
def index():
    return 'index'
    
app.run(host='localhost', port=5000)

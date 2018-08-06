import json, os
from flask import Flask
app = Flask(__name__)


rootPath = 'data/6hcp/'

data = []
def init():
    global data
    path = os.listdir(rootPath)
    for x in path:
        with open(rootPath+x, 'r') as f:
            d = json.loads(f.readline())
            data += d
    print(len(data))


@app.route('/result/<int:code>')
def result(code):
    if code < len(data):
        return json.dumps(data[code])
    return '{}'

if __name__ == '__main__':
    init()
    app.run()
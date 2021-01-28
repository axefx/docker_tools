#!/usr/bin/env python
import uvicorn
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    uvicorn.run(app)

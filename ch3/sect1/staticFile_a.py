# coding=utf-8

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    app_name = str(__name__)
    print '__name__:' + app_name
    return app_name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

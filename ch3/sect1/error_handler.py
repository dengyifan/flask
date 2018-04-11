# coding=utf-8

from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'home page'


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('./error.html'), 404)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

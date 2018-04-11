# coding=utf-8

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/item/<id>')
def item(id):
    return 'Item:{}'.format(id)

@app.route('/str/<string:str>')
def strType(str):
    return str

@app.route('/int/<int:i>')
def intType(i):
    return str(i)

@app.route('/float/<float:f>')
def floatType(f):
    return str(f)

@app.route('/<any(a,b):page_name>/')
def anyPath(page_name):
    return str(page_name)

@app.route('/people/')
def people():
    name = request.args.get('name')
    return name 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

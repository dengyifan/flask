# coding=utf-8

from flask import Flask
import settings

app = Flask(__name__)

app.config.from_object(settings)

@app.route('/hello')
def hello():
    print settings.A
    return 'hello,value of A:' + str(settings.A)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

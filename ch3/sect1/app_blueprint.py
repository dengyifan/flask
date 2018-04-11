# coding=utf-8

from flask import Flask
import user
import apple


app = Flask(__name__)
app.register_blueprint(user.bp)
app.register_blueprint(apple.bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

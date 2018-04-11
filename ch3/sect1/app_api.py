# coding=utf-8

from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)


class UserAPI(MethodView):

    def get(self):
        return jsonify({
            'username': 'lishi',
            'avatar': 'http://a.hiphotos.baidu.com/image/pic/item/902397dda144ad34e98003fedca20cf431ad8588.jpg'
        })

    def post(self):
        return 'UNSUPPORTED!'


app.add_url_rule('/user', view_func=UserAPI.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

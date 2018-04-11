# coding=utf-8
from flask import Blueprint

bp = Blueprint('apple', __name__, url_prefix='/apple')

@bp.route('/')
def index():
    return 'Apple"s Home page'

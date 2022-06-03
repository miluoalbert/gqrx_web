from turtle import title
from .control import get_freq, get_sql, set_freq, get_strength, set_sql, get_rec, set_rec
from flask import (
    Blueprint, render_template, request, make_response
)

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    posts = [{
      title: '111'
    }]
    return render_template('index.html', posts=posts)

@bp.route('/get_info')
def get_info():
    suggestions_list = {
      'freq': get_freq(),
      'sql': get_sql()
    }

    return suggestions_list

@bp.route('/freq')
def freq():
    text = request.args.get('freq')
    print(text)

    response = make_response(set_freq(text), 200)
    response.mimetype = "text/plain"
    return response

@bp.route('/get_str')
def get_str():
    response = make_response(get_strength(), 200)
    response.mimetype = "text/plain"
    return response

@bp.route('/sql')
def sql():
    text = request.args.get('sql')
    response = make_response(set_sql(text), 200)
    response.mimetype = "text/plain"
    return response

@bp.route('/rec_status')
def rec_status():
    response = make_response(get_rec(), 200)
    response.mimetype = "text/plain"
    return response

@bp.route('/rec_set')
def rec_set():
    text = request.args.get('rec')
    response = make_response(set_rec(text), 200)
    response.mimetype = "text/plain"
    return response
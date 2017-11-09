#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import flask
from flask_httpauth import HTTPBasicAuth

app = flask.Flask(__name__)
auth = HTTPBasicAuth()


tasks = [
    {
        'id': 1,
        'priority': 1,
        'title': 'Python óra',
        'description': '8.15, Irinyi 108',
        'done': True
    },
    {
        'id': 2,
        'priority': 2,
        'title': 'Kötelező program elkészítése',
        'description': 'Nemsokára le kell adni :(',
        'done': False
    }
]


@app.route('/todos', methods=['GET'])
def get_tasks():
    return json.dumps({'todo_list': tasks}, ensure_ascii=False)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not flask.request.json or not 'title' in flask.request.json:
        flask.abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': flask.request.json['title'],
        'description': flask.request.json.get('description', ""),
        'done': False,
        'priority': flask.request.json.get('description', "3"),
    }
    tasks.append(task)
    return json.dumps({'task': task})


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None


@auth.error_handler
def unauthorized():
    return json.dumps({'error': 'Unauthorized access'})


@app.route('/todo/<int:id>', methods=['GET'])
@auth.login_required
def get_single_task(id):
    for task in tasks:
        if task['id'] == id:
            return json.dumps({'todo': task}, ensure_ascii=False)
    flask.abort(404)
    return json.dumps({}, ensure_ascii=False)


@app.route('/fancy')
def fancy_index():
    # https://realpython.com/blog/python/primer-on-jinja-templating/
    return flask.render_template('post.html', result=tasks)


@app.route('/')
def index():
    return '<html><body><h1>Hello World!</h1></body></html>'


if __name__ == '__main__':
    app.run(debug=True)

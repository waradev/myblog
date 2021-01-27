# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = "top"
    # htmlを表示
    return render_template('index.html', title=title)

@app.route('/prev/')
def prev():
    title = "prev"
    return render_template('prev.html', title=title)

if __name__ == '__main__':
    app.run()
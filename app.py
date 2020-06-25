from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import json
import os
import tools

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    return render_template('index.html', projects=tools.getProjects())


app.run(host='0.0.0.0', port=port, debug=True)

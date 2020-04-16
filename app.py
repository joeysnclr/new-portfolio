from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import json, os
import tools

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():

	return render_template('index.html', projects=tools.getProjects())


@app.route('/project/<string:projectId>')
def project(projectId):
	p = tools.getProject(projectId)
	if p == None:
		return redirect(url_for("index"))
	return render_template('project.html', pId=projectId, p=p)


app.run(host='0.0.0.0', port=port)
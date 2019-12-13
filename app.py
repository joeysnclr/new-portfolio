from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import json, os
import tools, text

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():

	return render_template('index.html', projects=tools.getProjects())

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	response = ""
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		subject = request.form.get('subject')
		message = request.form.get('message')
		textBody = "\n" + name + "\n" + email + "\n" + subject + "\n" + message
		sms = text.Messenger("+12406677357", "+16507593486")
		sms.sendMessage(textBody)
		response = "Message sent!"
	return render_template('contact.html', response=response)

@app.route('/project/<string:projectId>')
def project(projectId):
	p = tools.getProject(projectId)
	if p == None:
		return redirect(url_for("index"))
	return render_template('project.html', pId=projectId, p=p)


app.run(host='0.0.0.0', port=port)
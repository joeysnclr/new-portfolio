import json

def getProjects():
	with open("./static/data/projects.json", "r+") as file:
		data = json.load(file)
	return data

def getProject(projId):
	return getProjects().get(projId)
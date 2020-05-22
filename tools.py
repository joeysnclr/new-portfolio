import json


def getProjects():
    with open("./static/data/projects.json", "r+") as file:
        data = json.load(file)
    return data

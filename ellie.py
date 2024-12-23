import os
from datetime import date
import requests

ELLIE_API_KEY = os.environ.get("ELLIE_API_KEY")

def getList():
    url = "https://api.ellieplanner.com/v1/tasks/byDate?date=" + str(date.today().isoformat())
    headers = {'content-type': 'application/json', 'Accept': 'application/json',
               'x-api-key': ELLIE_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    jsonResponse = response.json()
    return jsonResponse

def getLabelList():
    url = "https://api.ellieplanner.com/v1/labels/getLabels"
    headers = {'content-type': 'application/json', 'Accept': 'application/json',
               'x-api-key': ELLIE_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    jsonResponse = response.json()
    return jsonResponse

def getLabel(labelId, labelJson):
    labelName = [index for index in labelJson if index['id'] == labelId]
    for label in labelName:
        return label['name']

def getLabelColor(labelId, labelJson):
    labelName = [index for index in labelJson if index['id'] == labelId]
    for label in labelName:
        return label['color']

def getTasks():
    list = getList()
    taskList = {}
    labelList = getLabelList()
    line = 0

    for index in list:
        taskName = index['description']
        taskCompletion = index['complete']
        if taskCompletion == 1:
            taskStatus = "complete"
        else:
            taskStatus = "incomplete"
        taskLabel = getLabel(index['label'], labelList)
        taskLabelColor = getLabelColor(index['label'], labelList)
        tasks = {'name': taskName, 'status': taskStatus, 'label': taskLabel,
                 'labelColor': taskLabelColor}
        taskList[line] = tasks
        line = line + 1

    # taskListJson = json.dumps(taskList)
    return taskList
from msilib.schema import ODBCAttribute
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_from_directory
import uuid


Tasks= [
        {
          'id': uuid.uuid4().hex,
          'title': 'Task1',
          'description': 'About trained task',
          'X':'1',
          'Y':'0.9',
          'read':True
          
        },
        {
          'id': uuid.uuid4().hex,
          'title': 'Task2',
          'description': 'Task 2 data',
          'X':'1',
          'Y':'0.9',
         'read':False
          
        },
      ]

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route

@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Tasks.append({
          'id':uuid.uuid4().hex,
            'title': post_data.get('title'),
            'description': post_data.get('description'),
            'X':post_data.get('X'),
            'Y':post_data.get('Y'),
           'read': post_data.get('read'),
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = Tasks
    return jsonify(response_object)   

#new task

@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(task_id)
        Tasks.append({
            'id':uuid.uuid4().hex,
            'title': post_data.get('title'),
            'description': post_data.get('description'),
            'X':post_data.get('X'),
            'Y':post_data.get('Y'),
           'read': post_data.get('read'),
        })
        response_object['message'] = 'Task updated!'
    if request.method == 'DELETE':
        remove_task(task_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)

def remove_task(task_id):
    for task in Tasks:
        if task['id'] == task_id:
            Tasks.remove(task)
            return True
    return False

@app.route('/tasks/uploaded_files',methods=['GET'])
def SelectFolder():
    folders=os.listdir(request.args['path'])
    return {"data":folders}

     
if __name__ == '__main__':
    app.run(debug=True)
from asyncio.windows_events import NULL
import os
from urllib import response
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_from_directory
import uuid



Jsonfile={	

	"Dekor_Name": "3236_gedreht",
	"image_source_dir": "/media/software_new/Oberflaechen Inspektion/Datenbank/Kundenmuster/Ballerina/3236 Keramik dunkel/3236_gedreht",
	"image_source_dir_cut": False,
	"train_split": 85,	
	"Number_of_epochs": 85,
	"sliced_error_image_dir": [
		"/media/software_new/Oberflaechen Inspektion/Datenbank/Fehlerkatalog",
		"/media/software_new/Oberflaechen Inspektion/Datenbank/Fehlerkatalog/Ballerina_ausgeschnittene Fehler"
	],
	"real_errorplates_dir": "/media/software_new/Oberflaechen Inspektion/Datenbank/Kundenmuster/Ballerina/3236 Keramik dunkel/Fehlerbilder",
	"erg_pfad": "/home/knecht/Dokumente/Lokale_Datenbank/Ballerina_Training/3236_gedreht/",
	"defektor_train": {
		"plates": 0,
		"Fehler": 0,
		"global_plates_mean": -1.0,
		"global_plates_variance": -1.0,
		"stride_ratio_width": 0.5,
		"stride_ratio_height": 0.5,
		"plates_scale": 0.8,
		"target_width": 512,
		"target_height": 512,
		"rotationRangeDeg": 0.2,
		"cuttingRange": [
			300,
			300
		],
		"mirror": True,
		"rotate_90": False,
		"patch_brightnessMin": -15,
		"patch_brightnessMax": 15,
		"useNoiseOnGT": False,
		"useBrightnessOnGT": True,
		"threshold_find_errors": 5,
		"minimum_error_contour_size": 100,
		"minimum_error_size": 50,
		"error_scale_lower_range": 0.7,
		"error_scale": 0.9,
		"borderDistance": 20,
		"alphaMin": 5,
		"alphaMax": 20,
		"sigmaMin": 15,
		"sigmaMax": 20,
		"error_brightnessMin": 0.85,
		"error_brightnessMax": 1.15,
		"placingRate": [
			25,
			30,
			30,
			10,
			5
		],
		"Scalenorm_sigma": 5.326724,
		"GaussianBlur_sigmaX": 0.0,
		"__class__": "defektor"
	},
	"defektor_val": {
		"plates": 0,
		"Fehler": 0,
		"global_plates_mean": -1.0,
		"global_plates_variance": -1.0,
		"stride_ratio_width": 0.5,
		"stride_ratio_height": 0.5,
		"plates_scale": 0.8,
		"target_width": 512,
		"target_height": 512,
		"rotationRangeDeg": 0.2,
		"cuttingRange": [
			300,
			300
		],
		"mirror": True,
		"rotate_90": False,
		"patch_brightnessMin": -15,
		"patch_brightnessMax": 15,
		"useNoiseOnGT": False,
		"useBrightnessOnGT": True,
		"threshold_find_errors": 5,
		"minimum_error_contour_size": 100,
		"minimum_error_size": 50,
		"error_scale_lower_range": 0.7,
		"error_scale": 0.9,
		"borderDistance": 20,
		"alphaMin": 5,
		"alphaMax": 20,
		"sigmaMin": 15,
		"sigmaMax": 20,
		"error_brightnessMin": 0.85,
		"error_brightnessMax": 1.15,
		"placingRate": [
			25,
			30,
			30,
			10,
			5
		],
		"Scalenorm_sigma": 5.326724,
		"GaussianBlur_sigmaX": 0.0,
		"__class__": "defektor"
	},
	"model_class": {
		"width": 512,
		"height": 512,
		"batchsize": 5,
		"GPU_Memory": 8,
		"n_filters": [
			32,
			64,
			128,
			256,
			512,
			1024
		],
		"conv_padding": "same",
		"conv_activation": "sigmoid",
		"dropout": [
			0.1,
			0.1,
			0.1,
			0.1,
			0.1,
			0.1
		],
		"Batchnorm": True,
		"VAE_option": NULL,
		"inital_kl_weight": 0.1,
		"train_systematik": 1,
		"Framework_name": "U-Net\"2\"",
		"model_name": "U-Net-2",
		"Layer_INPUT_NAME": "input",
		"Layer_OUTPUT_NAME": "praed/Sigmoid",
		"__class__": "U_Net_2"
	},
	"my_callback": {
		"erg_pfad": "/home/knecht/Dokumente/Lokale_Datenbank/Ballerina_Training/3236_gedreht/",
		"use_Tensorboard": False,
		"__class__": "segment_Plates"
	},
	 "__class__": "onclass_learner"
}



Tasks= [
        {
          'id': uuid.uuid4().hex,
          'title': 'Task1',
          'description': 'About trained task',
          'folder':'folder_1',
        #   'X':'1',
        #   'Y':'0.9',
          'read':True 
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
            'folder':post_data.get('folder'),
			'par':post_data.get('par'),
            # 'X':post_data.get('X'),
            # 'Y':post_data.get('Y'),
            
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
            'folder':post_data.get('folder'),
            # 'X':post_data.get('X'),
            # 'Y':post_data.get('Y'),
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



@app.route('/tasks/parameters',methods=['GET'])   
def paramsFile():
    return jsonify(Jsonfile)



     
if __name__ == '__main__':
    app.run(debug=True)

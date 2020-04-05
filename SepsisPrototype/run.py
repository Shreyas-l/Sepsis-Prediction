from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
import csv
import tensorflow as tf
import keras
from keras import backend as k
from keras.models import Sequential,load_model
import pickle
import io


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/home')

def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		f = request.files['testpatient']
		stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
		csv_input = csv.reader(stream)
		print(csv_input)
		sample = []
		for row in csv_input:
			sample.append(row)
		sample=np.array(sample)
		model = load_model('SepsisModel.h5')
		prediction = model.predict(sample)
		print(prediction)
		# testpatient = request.form('testpatient')
		# print(testpatient)
		# #testpatient = request.form('testpatient').first()
		# # Create variable for uploaded file
		# f = request.files['testpatient']
		# # fstring = f.read()
		# # s=str(fstring)
		# # data = StringIO(s)
		# df=pd.read_csv(f)
		# sample = df.iloc[:].values
		# print(sample)
		# model = load_model('SepsisModel.h5')
		# #model = pickle.load(open("SepsisModel.pkl", "rb")) 
		# prediction = model.predict(sample)
		# print(prediction)
	#return 'OK'
	return(render_template('home.html',prediction = prediction))
	
		
if __name__ == '__main__':
	app.run(debug = True)

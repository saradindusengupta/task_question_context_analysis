# -*- coding: utf-8 -*-
import os
import nltk
import joblib
import pandas as pd
from Features import CreateFeatures
from sklearn.linear_model import LogisticRegression


class TrainClassifier:

	def __init__(self, lib_path):
		self.lib_path = lib_path
		self.Features = CreateFeatures()
	
	
	def trainClassifier(self, data):
		try:
			classifier = joblib.load(os.path.join(self.lib_path,'niki-ai-tsk-model.pkl'))
			#print(type(classifier))
			#print("Training Model Object loaded..")
		except:
			result = []
			for fl in range(0, len(data)):
				print(fl)
				feature = self.Features.CreateFeatureDataTrain(data['Sentence'][fl], data['Category'][fl])
				result.append(feature)
			data = pd.DataFrame(result)
			train_y = data['Category']
			train_x = data.drop(data[['Sentence', 'Category']], axis=1)
			classifier = LogisticRegression(tol= 0.0001, dual =False,verbose=0, max_iter=100,multi_class='multinomial', warm_start=False, random_state=0,class_weight=None,C=0.1,solver='newton-cg', penalty='l2', fit_intercept=True, intercept_scaling=1, n_jobs=-1)
			classifier.fit(train_x, train_y)
			joblib.dump(classifier, os.path.join(self.lib_path,'niki-ai-tsk-model.pkl'))
			print("Training Model Object Written..")
		return classifier
	
		
if __name__ == '__main__':
	"""
	Change the paths of the libpath(path to the trained model),
	path of the output file, and path of the input file.
	
	The input file only contains the questions list it's a .csv file seperated by "|"
	The output file is also .csv "|" seperated.
	"""
	path = '/home/saradindu/Desktop/LabelledData(1).csv' 			## path to the training data
	input = '/home/saradindu/Desktop/input.csv'		#train_1000.label
	result_path = '/home/saradindu/Desktop/Output.csv'			## path to output file
	lib_path = '/home/saradindu/Desktop/'				## path to the trained model
	
	data = pd.read_csv(path, sep=",,,", header=None)
	data=data.rename(columns = {0:'Sentence', 1:'Category'})
	classObj = TrainClassifier(lib_path)
	classifier = classObj.trainClassifier(data)
	

	test_data = pd.read_csv(input, sep="|", header=None, encoding='latin-1')
	test_data=test_data.rename(columns = {0:'Sentence'})
	test_x = []
	for fl in range(0, len(test_data)):
		feature = classObj.Features.CreateFeatureDataTest(test_data['Sentence'][fl])
		test_x.append(feature)
	test_x = pd.DataFrame(test_x)
	sent = test_x['Sentence']
	test_x = test_x.drop(test_x[['Sentence']], axis=1)
	probas = classifier.predict(test_x)
	
	catList = {0:'what', 1:'who', 2:'when', 3:'affirmation', 4:'unknown'}
	probas = [catList[i] for i in probas]
	result = pd.DataFrame({'Sentences':sent, 'Category':probas})
	result.to_csv(result_path, sep='|', index=False, columns=['Sentences', 'Category'])
	
	

# task: question_context_analysis
Based on the question determines the context on What,Who,When and Affirmation
#!/bin/python3/

Run Run.py from '/home/?/?/run.py' as 'python3 Run.py'
If the trained model is already inside the path then it will load that or it will start training.
The input data set is named as "LabelledData(1).csv 

path = '/home/saradindu/Desktop/LabelledData(1).csv' 			## path to the training data
input = '/home/saradindu/Desktop/input.csv'		#train_1000.label
result_path = '/home/saradindu/Desktop/Output.csv'			## path to output file
lib_path = '/home/saradindu/Desktop/'				## path to the trained model

The depends on the machine.

Dependencies :

scikit-learn : http://scikit-learn.org/ or pip3 install sklearn
pandas       : http://pandas.pydata.org/ or pip3 install pandas
joblib       : https://pypi.python.org/pypi/joblib or pip3 install joblib
nltk         : http://www.nltk.org/                or pip3 install nltk


	

# -*- coding: utf-8 -*-
import re
import nltk
import pandas as pd


class CreateFeatures:
	
	def __init__(self):
		#self.path = path
		self.yesno = ["can", "could", "would", "is", "does", "has", "was", "were", "had", "have", "did", "are", "will"]
		self.unknown = ["where", "why", "how", "whose", "which", "whom"]
	
	
	def tokenize(self, text):
		tokens = nltk.word_tokenize(text)
		tokens = [i.strip() for i in tokens]
		tokens = [k.strip(',|.|-|;|!|?') for k in tokens]
		tokens = [i for i in tokens if i != '']
		return tokens


	def check_type(self, toks):
		if toks[0].lower() == 'what':
			result = 0 		#'WHAT'
		elif toks[0].lower() == 'who':
			result = 1		#'WHO'
		elif toks[0].lower() == 'when':
			result = 2		#'WHEN'
		elif toks[0].lower() in self.unknown:
			result = 4		#'UNKNOWN'
		elif toks[0].lower() in self.yesno:
			result = 3		#'AFFIRMATION'
		else:
			result = 4		#'UNKNOWN'
		return result

	def check_time_factor( self, toks ):
		if len(toks) >= 2:
			tm = ['what', 'time']
			if toks[0] in tm and toks[1] in tm:
				result = 1
			else:
				result = 0
		else:
			result = 0        
		return result

	def CreateFeatureDataTrain(self, sent, category):
		toks = self.tokenize(sent)
		LENGTH = len(toks)
		pos_toks = nltk.pos_tag(toks)
		QTYPE = self.check_type(toks)
		catList = {'what':0, 'who':1, 'when': 2, 'affirmation':3, 'unknown':4}
		category = category.strip()
		category = catList[category]
		#WHAT = len([i for i in toks if i in ['what']])
		#WHO = len([i for i in toks if i in ['who']])
		#WHEN = len([i for i in toks if i in ['when']])
		#AFFRM = len([i for i in toks if i in self.yesno])
		#UNKNWN = len([i for i in toks if i in self.unknown])
		CIN = len([i for i in pos_toks if i[1] == 'IN'])
		CJJ = len([i for i in pos_toks if re.search('^JJ',i[1]) != None])
		CNN = len([i for i in pos_toks if re.search('^NN',i[1]) != None])
		CPRP = len([i for i in pos_toks if re.search('^PRP',i[1]) != None])
		CRB = len([i for i in pos_toks if re.search('^RB',i[1]) != None])
		CVB = len([i for i in pos_toks if re.search('^VB',i[1]) != None])
		CWDT = len([i for i in pos_toks if i[1] == 'WDT'])
		CWP = len([i for i in pos_toks if i[1] == 'WP'])
		CWPDO = len([i for i in pos_toks if i[1] == 'WP$'])
		CWRB = len([i for i in pos_toks if i[1] == 'WRB'])
		CCC = len([i for i in pos_toks if i[1] == 'CC'])
		WPNN = self.check_time_factor(toks)
		features = {
					"Sentence": sent,
					"LENGTH": LENGTH,
					#"WHAT": WHAT,
					#"WHO": WHO,
					#"WHEN": WHEN,
					#"AFFIRMATION": AFFRM,
					#"UNKNOWN": UNKNWN,
					"QTYPE": QTYPE,
					"TIME_FACTOR": WPNN,
					"IN_COUNT": CIN,
					"JJ_COUNT": CJJ,
					"PRP_COUNT": CPRP,
					"NN_COUNT": CNN,
					"RB_COUNT": CRB,
					"VB_COUNT": CVB,
					"WDT_COUNT": CWDT,
					"WP_COUNT": CWP,
					"WPD_COUNT": CWPDO,
					"WRB_COUNT": CWRB,
					"CONJ": CCC,
					"Category": category
				}
		return features
	
	def CreateFeatureDataTest(self, sent):
		#sent = data['']
		toks = self.tokenize(sent)
		LENGTH = len(toks)
		pos_toks = nltk.pos_tag(toks)
		QTYPE = self.check_type(toks)
		#catList = {'what':0, 'who':1, 'when': 2, 'affirmation':3, 'unknown':4}
		#category = catList[category]
		#WHAT = len([i for i in toks if i in ['what']])
		#WHO = len([i for i in toks if i in ['who']])
		#WHEN = len([i for i in toks if i in ['when']])
		#AFFRM = len([i for i in toks if i in self.yesno])
		#UNKNWN = len([i for i in toks if i in self.unknown])
		CIN = len([i for i in pos_toks if i[1] == 'IN'])
		CJJ = len([i for i in pos_toks if re.search('^JJ',i[1]) != None])
		CNN = len([i for i in pos_toks if re.search('^NN',i[1]) != None])
		CPRP = len([i for i in pos_toks if re.search('^PRP',i[1]) != None])
		CRB = len([i for i in pos_toks if re.search('^RB',i[1]) != None])
		CVB = len([i for i in pos_toks if re.search('^VB',i[1]) != None])
		CWDT = len([i for i in pos_toks if i[1] == 'WDT'])
		CWP = len([i for i in pos_toks if i[1] == 'WP'])
		CWPDO = len([i for i in pos_toks if i[1] == 'WP$'])
		CWRB = len([i for i in pos_toks if i[1] == 'WRB'])
		CCC = len([i for i in pos_toks if i[1] == 'CC'])
		WPNN = self.check_time_factor(toks)
		features = {
					"Sentence": sent,
					"LENGTH": LENGTH,
					#"WHAT": WHAT,
					#"WHO": WHO,
					#"WHEN": WHEN,
					#"AFFIRMATION": AFFRM,
					#"UNKNOWN": UNKNWN,
					"QTYPE": QTYPE,
					"TIME_FACTOR": WPNN,
					"IN_COUNT": CIN,
					"JJ_COUNT": CJJ,
					"PRP_COUNT": CPRP,
					"NN_COUNT": CNN,
					"RB_COUNT": CRB,
					"VB_COUNT": CVB,
					"WDT_COUNT": CWDT,
					"WP_COUNT": CWP,
					"WPD_COUNT": CWPDO,
					"WRB_COUNT": CWRB,
					"CONJ": CCC,
				}
		return features

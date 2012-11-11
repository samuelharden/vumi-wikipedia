import re
import porter
import numpy
from numpy import zeros,dot
from numpy.linalg import norm

__all__=['compare']
stop_words = [w.strip() for w in open('english.stop','r').readlines()]
splitter=re.compile ( "[a-z\-']+", re.I )
stemmer=porter.PorterStemmer()

class CosineSimilarity(object):


		
	def __init__(self):
		a = "compare"

	def add_word(self,word,d):
		 """
		    Adds a word the a dictionary for words/count
		    first checks for stop words
			the converts word to stemmed version
		 """
		 w=word.lower() 
		 if w not in stop_words:
			 ws=stemmer.stem(w,0,len(w)-1)
		 	 d.setdefault(ws,0)
			 d[ws] += 1

	def doc_vec(self,doc,key_idx):
	 v=zeros(len(key_idx))
	 for word in splitter.findall(doc):
	  keydata=key_idx.get(stemmer.stem(word,0,len(word)-1).lower(), None)
	  if keydata: v[keydata[0]] = 1
	 return v

	def compare(self,doc1,doc2):
	
	 # strip all punctuation but - and '
	 # convert to lower case
	 # store word/occurance in dict
	 all_words=dict()
	
	 for dat in [doc1,doc2]:
	  [self.add_word(w,all_words) for w in splitter.findall(dat)]
	 
	 # build an index of keys so that we know the word positions for the vector
	 key_idx=dict() # key-> ( position, count )
	 keys=all_words.keys()
	 keys.sort()
	 #print keys
	 for i in range(len(keys)):
	  key_idx[keys[i]] = (i,all_words[keys[i]])
	 del keys
	 del all_words

	 v1=self.doc_vec(doc1,key_idx)
	 v2=self.doc_vec(doc2,key_idx)
	 return float(dot(v1,v2) / (norm(v1) * norm(v2)))
 


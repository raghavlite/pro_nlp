# import modules & set up logging
import logging
import cPickle
from gensim import corpora, models, similarities
import os
import re
from nltk.corpus import stopwords

# savefilePath = 'path/to/file'
# with open(savefilePath, 'w') as savefile:
# cPickle.dump(myBigList, savefile)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) 
f_list = os.listdir("./dataset/")
stop = stopwords.words('english')
# f=open("1900.txt",'r').readlines()
i=0;
for f in sorted(f_list):
	sentences=[]
	# print line
	line=open("./dataset/"+f,"r").read()
	line=re.sub("(hon\.|Mr\.)","",line)
	line=re.sub("[0-9]+","",line)
	match=re.search("([A-Z])\.",line);
	line=re.sub("([A-Z])\.",match.groups()[0] ,line);
	sentence=line.strip().split('.')
	# string = "Special $#! characters   spaces 888323"

	sumt=0;
	for s in sentence:
		# string=[i for i in s.split() if i not in stop]
		string=re.sub("[^\w\s]", "",s);
		# string= ''.join(e for e in s if e.isalnum())
		# 'Specialcharactersspaces888323'
		# print "$$$$$$$$"
		if(len(string.split())>2):
			sumt=sumt+len(string.split())
			string=string.lower()
			sentences.append(string.split())
			# print sentences
	print "##################################################################"
	# sentences.append(line)
	print sumt
	print len(sentences)
	# cPickle.dump(sentences, 'sentences'+i)
	model = models.Word2Vec(sentences,size=200,window=5, min_count=5, workers=8 )
	model.save('word'+str(i))
	i=i+1	

# sentences = [['first', 'sentence'], ['second', 'sentence']]
# # train word2vec on the two sentences
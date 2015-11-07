import numpy as np
from numpy.linalg import norm
from scipy.spatial.distance import cosine, euclidean
import pickle
import gc
import codecs
from sys import argv
import gensim
# word0=input()
# word1=input()
for x in argv:
	print x
script,word0, word1=argv
model0 = gensim.models.Word2Vec.load(word0)
model1 = gensim.models.Word2Vec.load(word1)
d=200
order = []
print "Creating dictionaries"
def alllines():
    '''This function returns two dictionaries.
    These dictionaries correspond to the word vectors in _f1 and _f2 respectively.
    Each key in a dictionary corresponds to a word present in the respective file.
    Each value represents a numpy array with the vector of the word.
    '''
    # f1 = codecs.open(_f1,'r',"utf-8") represneted by model0
    # f2 = codecs.open(_f2,'r',"utf-8") ............... model1
    l1 = " "
    l2 = " "

    d1 = {}
    d2 = {}
    ###list given by name settttt
    for z in model0.vocab:
    	w0=z
    	if(len(w0)>2):
    		d1[w0]=model0[w0]
    for z in model1.vocab:
    	w1=z
    	if(len(w1)>2):
    		d2[w1]=model1[w1]
    return d1,d2
d1,d2=alllines()

print "Dictionaries created"
def getlines():
	'''This is a generator for the words in the dictionaries.
	This will only return words in the vocabularies of both corpora.'''
	keys_a = set(d1.keys())
	keys_b = set(d2.keys())
	# print len(keys_a)
	# print len(keys_b)
	intersection = keys_a.intersection(keys_b)
	# print intersection
	intersection=list(intersection)
	return intersection






n_extra = 0
intersection=getlines()
# Y = A.X
Y = np.zeros((d + 1, d + 1 + n_extra))
X = np.zeros((d + 1, d + 1 + n_extra))
print "Creating common words matrix"
# for n in xrange(d + 1 + n_extra):
#     w,v1,v2 = gen.next()
#     # Augmenting 1 so that we can deal with the bias vector `b`.
#     Y[:,n] = np.append(v2,1)
#     X[:,n] = np.append(v1,1)
# print intersection[1:200]


for n in xrange(d + 1 + n_extra):
    # w,v1,v2 = gen.next()
    # Augmenting 1 so that we can deal with the bias vector `b`.
    Y[:,n] = np.append(model0[intersection[n]],1)
    X[:,n] = np.append(model1[intersection[n]],1)
# print X
# if savefile:
#     # Loading matrix solutions from the savefile
#     print "Matrix loaded from file"
#     with open(savefile,'rb') as sfp:
#         Ab = pickle.load(sfp)
# else:
    # Solving the matrix.
print "Matrix created. Solving"
gc.collect()
# print X
# print Y
Ab = np.dot(Y,np.linalg.pinv(X))
# Sanity-check
print np.allclose(np.dot(Ab,X), Y)

# This newly-solved matrix is saved by default. This file is overwritten every time we re-solve the matrix.
print "Solved. Saving"
with open("matr_m.dat","wb") as sfp:
    pickle.dump(Ab,sfp)

# Sanity-check
if np.any(Ab):
    print "Yes!"
else:
    print "No!"
print Ab.shape
# print np.allclose(np.dot(Ab,X), Y) 
# print Ab[-2,:]

final_dic={}
for i in model1.vocab:
	b=np.append(model1[i],1)
	final_dic[i]=np.dot(Ab,b)[0:d]
	# final_dic
# print len(final_dic['kingsthorpe'])
with open("dictionaries_"+word0+".dat","wb") as sfp:
    pickle.dump(final_dic,sfp)
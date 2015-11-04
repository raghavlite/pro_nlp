from nltk.corpus import stopwords
import nltk
import re
import pickle
import os



cachedStopWords = stopwords.words("english")


def testFuncNew(text):
    # text = 'hello bye the the hi'
    # pp = nltk.word_tokenize(text)
    text = [word for word in text if word not in cachedStopWords];
    return text;

# fo = open("1890.txt", "r")
# ff = fo.read();

# fk  = open("1900.txt", "r")
# kf = fk.read();

# ff+=fk.read();





f_list = os.listdir("./dataset")
# f_list = ['S4V0010P0.xml'];

# f_list = ['S6CV0102P0.xml','S6CV0155P0.xml']







global result2;
result2 = {};

def count2(fruit):
	global result2;

	if(len(fruit)<3):
		return;

	if fruit not in result2:
		result2[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
	result2[fruit] += 1








flag=0;
for km in sorted(f_list): 

	result2 = {};

	# km = '1970.txt';

	# print km;

	if(km == '1970.txt'):
		flag=1;

	if(flag == 0):
		print 'not done',km;
		continue;

	print 'doing for',km;
	fo = open('./dataset/'+km, "r")
	line= fo.read();

	
	# line=re.sub("(hon\.|Mr\.)","",line)
	# line=re.sub("[0-9]+","",line)
	# match=re.search("([A-Z])\.",line);
	# line=re.sub("([A-Z])\.",match.groups()[0] ,line);

	line = line.lower().split();


	line = testFuncNew(line);
	fd = nltk.FreqDist(line) 
	ll = fd.most_common(2000);
	ll1 = [ qq[0] for qq in ll if(len(qq[0])>2) ];




	with open('./common/commons_'+km, 'wb') as f:
		pickle.dump(ll1, f);


	ff =None;
	fd = None;
	ll1 = None;
	line = None;


'end for'



# sentence=line.strip().split('.')


# ///////////////////////////////////////////////////////
# with open(the_filename, 'rb') as f:
#     my_list = pickle.load(f)
# ///////////////////////////////////////////////////////

# global result2;
# result2 = {};

# def count2(fruit):
# 	global result2;

# 	if(len(fruit)<3):
# 		return;

# 	if fruit not in result2:
# 		result2[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
# 	result2[fruit] += 1


# for aa in sentence:
# 	nn = nltk.word_tokenize(aa);	
# 	for bb in nn:
# 		if(bb not in cachedStopWords):
# 			count2(bb);
		
















# line=kf;
# line=re.sub("(hon\.|Mr\.)","",line)
# line=re.sub("[0-9]+","",line)
# match=re.search("([A-Z])\.",line);
# line=re.sub("([A-Z])\.",match.groups()[0] ,line);
# # sentence=line.strip().split('.')
# lll = nltk.word_tokenize(line);
# # global result1;
# # result1 = {};
# # def count(fruit):
# # 	global result1;

# # 	if(len(fruit)<3):
# # 		return;


# # 	if fruit not in result1:
# # 		result1[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
# # 	result1[fruit] += 1


# # for aa in sentence:
# # 	nn = nltk.word_tokenize(aa);	
# # 	for bb in nn:
# # 		if(bb[0] not in cachedStopWords):
# # 			count(bb);


# kf = testFuncNew(lll);
# kf = nltk.FreqDist(kf)
# oo = kf.most_common(2000);





# oo1 = [ qq[0] for qq in oo if(len(qq[0])>2)];



# with open('./commons_1900.txt', 'wb') as f:
#     pickle.dump(oo1, f);





# ///////////////////////////////Common finding code////////////////////////////////////
# fd_set = set(ll1)
# kf_set = set(oo1)



# intersect = fd_set.intersection(kf_set);

# len(intersect);

# print intersect;







# for a in kf
# //////////////////////////////////////////////////////////////////////////////////










































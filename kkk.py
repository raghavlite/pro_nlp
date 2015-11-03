from nltk.corpus import stopwords
import nltk
import re

cachedStopWords = stopwords.words("english")


def testFuncNew(text):
    # text = 'hello bye the the hi'
    # pp = nltk.word_tokenize(text)
    text = [word for word in text if word not in cachedStopWords];
    return text;

fo = open("1890.txt", "r")
ff = fo.read();

fk  = open("1900.txt", "r")
kf = fk.read();

# ff+=fk.read();





line=ff;
line=re.sub("(hon\.|Mr\.)","",line)
line=re.sub("[0-9]+","",line)
match=re.search("([A-Z])\.",line);
line=re.sub("([A-Z])\.",match.groups()[0] ,line);

lll = line.split();

# sentence=line.strip().split('.')



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
		






ff = testFuncNew(lll);
fd = nltk.FreqDist(ff) 
ll = fd.most_common(2000);
ll1 = [ qq[0] for qq in ll if(len(qq[0])>2) ];



with open('../../1980.txt', 'wb') as f:
    pickle.dump(ll1, f);








line=kf;
line=re.sub("(hon\.|Mr\.)","",line)
line=re.sub("[0-9]+","",line)
match=re.search("([A-Z])\.",line);
line=re.sub("([A-Z])\.",match.groups()[0] ,line);
# sentence=line.strip().split('.')
lll = nltk.word_tokenize(line);
# global result1;
# result1 = {};
# def count(fruit):
# 	global result1;

# 	if(len(fruit)<3):
# 		return;


# 	if fruit not in result1:
# 		result1[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
# 	result1[fruit] += 1


# for aa in sentence:
# 	nn = nltk.word_tokenize(aa);	
# 	for bb in nn:
# 		if(bb[0] not in cachedStopWords):
# 			count(bb);


kf = testFuncNew(lll);
kf = nltk.FreqDist(kf)
oo = kf.most_common(2000);





oo1 = [ qq[0] for qq in oo if(len(qq[0])>3)];



fd_set = set(ll1)
kf_set = set(oo1)



intersect = fd_set.intersection(kf_set);

len(intersect);

print intersect;







for a in kf











































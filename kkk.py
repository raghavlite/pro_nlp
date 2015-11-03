from nltk.corpus import stopwords
import nltk
import re

cachedStopWords = stopwords.words("english")


def testFuncNew(text):
    # text = 'hello bye the the hi'
    text = [word for word in text.split() if word not in cachedStopWords];
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
sentence=line.strip().split('.')



global result2;
result2 = {};
def count2(fruit):
	global result2;

	if fruit not in result2:
		result2[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
	result2[fruit] += 1


for aa in sentence:
	nn = nltk.pos_tag(kf);	
	for bb in nn:
		if(bb[0] not in cachedStopWords):
			count2(bb);
		






# ff = testFuncNew(ff);
# fd = FreqDist(ff) 
# ll = fd.most_common(500);
# ll1 = [ qq[0] for qq in ll if(len(qq[0])>4) ];



line=kf;
line=re.sub("(hon\.|Mr\.)","",line)
line=re.sub("[0-9]+","",line)
match=re.search("([A-Z])\.",line);
line=re.sub("([A-Z])\.",match.groups()[0] ,line);
sentence=line.strip().split('.')

global result1;
result1 = {};
def count(fruit):
	global result1;
	
	if fruit not in result1:
		result1[fruit] = 0 # Create a new entry in the dictionary. 0 == int()
	result1[fruit] += 1


for aa in sentence:
	nn = nltk.pos_tag(kf);	
	for bb in nn:
		if(bb[0] not in cachedStopWords):
			count(bb);


# kf = testFuncNew(kf);
# kf = FreqDist(kf)
# oo = kf.most_common(500);
# oo1 = [ qq[0] for qq in oo if(len(qq[0])>4)];



# fd_set = set(ll1)
# kf_set = set(oo1)



# intersect = fd_set.intersection(kf_set);

# len(intersect);



















































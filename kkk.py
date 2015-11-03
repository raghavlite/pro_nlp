# from nltk.corpus import stopwords
# from nltk import *
# cachedStopWords = stopwords.words("english")


# def testFuncNew():
#     text = 'hello bye the the hi'
#     text = [word for word in text.split() if word not in cachedStopWords]

#     return text;




# from collections import defaultdict;

# words = "apple banana apple strawberry banana lemon"

# # f = open('./1890.txt','r');




# def pprocess(f):
# 	line=open("./"+f,"r").read()
# 	line=re.sub("(hon\.|Mr\.)","",line)
# 	line=re.sub("[0-9]+","",line)
# 	match=re.search("([A-Z])\.",line);
# 	line=re.sub("([A-Z])\.",match.groups()[0] ,line);
# 	# sentence=line.strip().split('.')


# 	line  = line.lower();

# 	tokens = word_tokenize(line);

# 	line = [word for word in tokens if word not in cachedStopWords];

# 	return line;
# 'end def'





# token1 = pprocess('1890.txt');

# d1 = defaultdict(int)
# for word in token1:
#     d1[word] += 1




# token2 = pprocess('1900.txt');

# d2= defaultdict(int)
# for word in token2:
#     d2[word] += 1





















































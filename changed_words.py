
import pickle



# dct_read = pickle.load( open( "../recent_dictionaries/dictionaries_word0.dat", "rb" ));


dct_lst=[];
for a in range(0,12):
	dct_read = pickle.load( open( "../recent_dictionaries/dictionaries_word"+str(a)+".dat", "rb" ));
	dct_lst.append(dct_read);
'end for'



# total common words
union=set();
for pp in dct_lst:
	union.update(pp.keys());

# total intersection words
common = union.copy();
for pp in dct_lst:
	common.intersection_update(pp.keys());


pickle.dump( common, open( "./commons.dat", "wb" ) )


import math
from itertools import izip

def dot_product(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))
'end def'



def cosine_measure(v1, v2):
    prod = dot_product(v1, v2)
    len1 = math.sqrt(dot_product(v1, v1))
    len2 = math.sqrt(dot_product(v2, v2))
    return prod / (len1 * len2)
'end def'

for aa in common:













import pickle
import os

pp = os.listdir('./common/');



dct_lst=[];
for a in sorted(pp):
	dct_read = pickle.load( open( "./common/"+str(a), "rb" ));
	dct_lst.append(dct_read);


union=set();
for pp in dct_lst:
	union.update(pp);

# total intersection words
common = union.copy();
for pp in dct_lst:
	common.intersection_update(pp);


pickle.dump( common, open( "./commons_pure.dat", "wb" ) )




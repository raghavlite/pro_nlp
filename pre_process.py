from bs4 import *
import re
import os






f_list = os.listdir("./")



for km in f_list: 

	print km;
	txt_again = open('./'+km,'r');
	txt_again = txt_again.read();
	txt_again = re.sub('<col>\d+</col>','',txt_again);
	txt_again = re.sub('&#......',' ',txt_again)
	# &#x2014;
	# &#x00E2;


	soup = BeautifulSoup(txt_again);

	# /////get year////////////////////
	jj = ' '.join([str(s.extract()) for s in soup('titlepage')]);
	jj = BeautifulSoup(jj);
	jj = jj.get_text();

	year = re.search('(\d{4})',jj);
	if(year!=None):
		year = int(year.groups()[0]);
	else:
		print 'mango dolly';





	kk = ' '.join([str(s.extract()) for s in soup('housecommons')]);
	ll = ' '.join([str(s.extract()) for s in soup('houselords')]);
	mm = ' '.join([str(s.extract()) for s in soup('writtenanswers')]);





	kk = BeautifulSoup(kk+''+ll+''+mm);
	pp = ' '.join([str(s.extract()) for s in kk('p')]);



	pp = BeautifulSoup(pp);
	pp = pp.get_text();
	pp = re.sub('\r','',pp)
	pp = re.sub('\n','',pp)
	pp = re.sub('\n\n','',pp)






	# pp = pp.rstrip();

	f = open('./'+str((year/10)*10)+'.txt','a');
	f.write(pp);
	f.close();
'end for'

# txt_again = open('./'+str((year/10)*10)+'.txt','r');
# txt_again = txt_again.read();
# pp = re.sub('\r','',txt_again)
# pp = pp.rstrip();

# f = open('./'+str((year/10)*10)+'.txt','w');
# f.write(pp);
# f.close();




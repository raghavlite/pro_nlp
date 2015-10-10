from bs4 import *
import re


txt_again = open('./S5CV0001P0.xml','r');
txt_again = txt_again.read();
txt_again = re.sub('<col>\d+</col>','',txt_again);




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





kk = BeautifulSoup(kk+'\n'+ll+'\n'+mm);

pp = ' '.join([str(s.extract()) for s in kk('p')]);


pp = BeautifulSoup(pp);


pp = pp.get_text();



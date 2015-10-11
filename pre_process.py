from bs4 import *
import re
import os
import xml.etree.ElementTree as ET






f_list = os.listdir("./")


# f_list = ['S6CV0102P0.xml','S6CV0155P0.xml']


for km in f_list: 

	# print km;
	# txt_again = open('./'+km,'r');
	# txt_again = txt_again.read();


	root = ET.parse('./'+km);


	foos = root.iter('table')
	for foo in foos:
		foo.clear()


	foos = root.findall('housecommons')
	for foo in foos:
		bars = foo.findall('p')
		for bar in bars:
			foo.remove(bar)

	foos = root.findall('houselords')
	for foo in foos:
		bars = foo.findall('p')
		for bar in bars:
			foo.remove(bar)

	mm= '';
	foos = root.findall('writtenanswers')
	for foo in foos:
		bars = foo.findall('p')
		for bar in bars:
			foo.remove(bar)
		mm+=ET.tostring(foo, encoding='utf8', method='xml');
		root.getroot().remove(foo);


	txt_again = ET.tostring(root.getroot(), encoding='utf8', method='xml');




	# try:
	# 	f = open('./qq.xml','a');
	# 	f.write(txt_again);
	# 	f.close();
	# except (UnicodeEncodeError ):
	# 	print 'bad file'


	
	# txt_again = re.sub('<table>[]+<\/table>','',txt_again);
	txt_again = re.sub('<col>\d+</col>','',txt_again);
	txt_again = re.sub('&#......',' ',txt_again)




	# &#x2014;
	# &#x00E2;

	# try:
	# 	f = open('./qq.xml','a');
	# 	f.write(txt_again);
	# 	f.close();
	# except (UnicodeEncodeError ):
	# 	print 'bad file'



	# soup = BeautifulSoup(txt_again);

	# soup.table.clear()
	# txt_again1 = soup.get_text(); 


	# try:
	# 	f = open('./pp.xml','a');
	# 	f.write(txt_again);
	# 	f.close();
	# except (UnicodeEncodeError ):
	# 	print 'bad file'






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
	# mm = ' '.join([str(s.extract()) for s in soup('writtenanswers')]);


	# //*[@id="collapsible1147"]



	kk = BeautifulSoup(kk+''+ll+''+mm);
	pp = ' '.join([str(s.extract()) for s in kk('p')]);



	pp = BeautifulSoup(pp);
	pp = pp.get_text();
	pp = re.sub('\r','',pp)
	pp = re.sub('\n','',pp)
	pp = re.sub('\n\n','',pp)






	# pp = pp.rstrip();

	try:
		f = open('../final/'+str((year/10)*10)+'.txt','a');
		f.write(pp);
		f.close();
	except (UnicodeEncodeError ):
		print 'bad file'


'end for'

# txt_again = open('./'+str((year/10)*10)+'.txt','r');
# txt_again = txt_again.read();
# pp = re.sub('\r','',txt_again)
# pp = pp.rstrip();

# f = open('./'+str((year/10)*10)+'.txt','w');
# f.write(pp);
# f.close();




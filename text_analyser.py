# ctl00_ContentPlaceHolder1_lblAuthor

# ctl00_ContentPlaceHolder1_lblContentType


# ctl00_ContentPlaceHolder1_lblContentText







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re
import pickle
from sets import Set

pp = os.listdir('./');


url = 'http://localhost:8000/';


driver = webdriver.Firefox()

authors_read = pickle.load( open( "../../authors_dct.p", "rb" ) )



for aa in authors_read.keys():
	if(authors_read[aa]==''):
		authors_read[aa] = 15;


for aa in authors_read.keys():
	print authors_read[aa];


dct ={};
for a in pp:
	date=15;
	url_req = url+a;
	print url_req;
	driver.get(url_req);

	try:
		tpe = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblContentType').text;
		content = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblContentText').text;
	


	except:
		print 'not found'
		continue;

	
	try:
		author = driver.find_element_by_id('ctl00_lblWriterImage');

		lnk = author.find_element_by_tag_name('a');
		
 		url2 = lnk.get_attribute('href')

 		driver.get(url2);

		ele = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblLeft');

		year = ele.text;

		ll = re.search('(\d{4})',year)

		if(ll!=None):
			date = ll.groups()[0];
		else:
			date = 15;
			print 'year not available';
			# continue;
	except:
		
		try:
			ele = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblRight');

			year = ele.text;

			ll = re.search('(\d{4})',year)

			if(ll!=None):
				date = ll.groups()[0];
			else:
				date = 15;
				print 'year not available';
				# continue;
		except:
			print 'yy2'
		print 'year picker problem';


	# try:
	# 	date = authors_read[author]
	# except:
	# 	print 'year picker problem 2'





	if not os.path.exists('../'+tpe):
		os.makedirs('../'+tpe)


	# try:
	# 	print date;
		f = open('../'+tpe+'/'+str((int(date)/10)*10)+'.txt','a');
		f.write('\n'+content.encode('utf8'));
		f.close(); 
	# except:
	# 	print 'writing error';



'end for'








# for a in dct:
#     print a;




































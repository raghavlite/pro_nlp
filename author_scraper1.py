from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re
import pickle


pp = os.listdir('./');


url = 'http://localhost:8000/';


driver = webdriver.Firefox()

dct ={};
for a in pp:
	url_req = url+a;
	print url_req;
	driver.get(url_req);

	try:
		ele = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblName');
	except:
		print 'not found'
		continue;

	lst = ele.find_element_by_tag_name('p').text

	ele = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblLeft');

	year = ele.text;

	ll = re.search('(\d{4})',year)

	if(ll!=None):
		dct[lst] = ll.groups()[0];
	else:
		dct[lst] = '';
		print 'not available';

'end for'

dct_read = pickle.load( open( "../author_dct.p", "rb" ) )


dct.update(dct_read);

pickle.dump( dct, open( "../authors_dct.p", "wb" ) )



for a in dct.keys():
    print a,dct[a];
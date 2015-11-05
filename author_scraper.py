# //*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]

# <span id="ctl00_ContentPlaceHolder1_lblRight"><p style="color:#800000; font-size:22px;text-align:left "> हरमन हेस्से</p><p style="font-size:18px;color:#A93281"><strong>परिचय उपलब्ध नहीं है।</strong></p></span>

# pp.find_element_by_tag_name('p').text

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

	ele = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblRight');

	lst = ele.find_element_by_tag_name('p').text

	year = ele.text;

	ll = re.search('(\d{4})',year)

	if(ll!=None):
		dct[lst] = ll.groups()[0];
	else:
		dct[lst] = '';
		print 'not available';

'end for'

pickle.dump( dct, open( "../author_dct.p", "wb" ) )

dct_read = pickle.load( open( "../author_dct.p", "rb" ) )


# for a in dct_read.keys():
#     print a,dct[a];




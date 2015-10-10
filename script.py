from lxml import html
import requests
import urllib2
import urllib
import contextlib
import zipfile



def unzip(source, target):
    with contextlib.closing(zipfile.ZipFile(source , "r")) as z:
        z.extractall(target)


# df = DataFrame(columns=('Station', 'Code'))

# page = requests.get('http://storage.googleapis.com/books/ngrams/books/datasetsv2.html')
# tree = html.fromstring(page.text)


for i in range(100,200):
	# buyers = tree.xpath('//*[@id="container"]/blockquote/p[26]/a['+str(i)+']/text()');
	# print buyers;

	# response = urllib2.urlopen('"http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20090715-'+buyers+'.csv.zip"');
	# html = response.read()
	print i;
	try:
		urllib.urlretrieve('http://www.hansard-archive.parliament.uk/Parliamentary_Debates_(4th_Series)_Vol_1_(February_1892)_to_Vol_199_(December_1908)/S4CV0'+str(i)+'P0.zip','./'+str(i)+'.zip');
		unzip('./'+str(i)+'.zip','./');

	except (IOError,zipfile.BadZipfile):
		print "Oops!  That was no valid number.  Try again..."




# http://www.hansard-archive.parliament.uk/Parliamentary_Debates_(4th_Series)_Vol_1_(February_1892)_to_Vol_199_(December_1908)
'end if'
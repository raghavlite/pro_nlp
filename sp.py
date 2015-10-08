from lxml import html
import requests
import urllib2
import urllib
import contextlib

def unzip(source, target):
    with contextlib.closing(zipfile.ZipFile(source , "r")) as z:
        z.extractall(target)


# df = DataFrame(columns=('Station', 'Code'))

page = requests.get('http://storage.googleapis.com/books/ngrams/books/datasetsv2.html')
tree = html.fromstring(page.text)


for i in range(1,801):
	buyers = tree.xpath('//*[@id="container"]/blockquote/p[26]/a['+str(i)+']/text()');
	print buyers;

	response = urllib2.urlopen('"http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20090715-'+buyers+'.csv.zip"');
	html = response.read()
	urllib.urlretrieve('http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20090715-91.csv.zip', '/users/ee/bt/raghuth/'+buyers+'.zip')

	unzip('./'+buyers+'.zip','./');

'end if'



# for name in z.namelist():
# 	outpath = './';
# 	z.extract(name,outpath);
# 'end for'



# with zipfile.ZipFile('./1.zip', "r") as z:
#     z.extractall("./")

# import contextlib

# def unzip(source, target):
#     with contextlib.closing(zipfile.ZipFile(source , "r")) as z:
#         z.extractall(target)








# "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20090715-91.csv.zip"


# urllib.urlretrieve('http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20090715-91.csv.zip', './1.zip')








# buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
# for i in range(1000):
# 	df.loc[i] = [buyers2[i], buyers[i]]


# page = requests.get('https://www.cleartrip.com/trains/stations/list?page=2')
# tree = html.fromstring(page.text)
# buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
# buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
# for i in range(1000):
# 	df.loc[1000+i] = [buyers2[i], buyers[i]]


# page = requests.get('https://www.cleartrip.com/trains/stations/list?page=3')
# tree = html.fromstring(page.text)
# buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
# buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
# for i in range(1000):
# 	df.loc[2000+i] = [buyers2[i], buyers[i]]


# page = requests.get('https://www.cleartrip.com/trains/stations/list?page=4')
# tree = html.fromstring(page.text)
# buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
# buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
# for i in range(1000):
# 	df.loc[3000+i] = [buyers2[i], buyers[i]]


# page = requests.get('https://www.cleartrip.com/trains/stations/list?page=5')
# tree = html.fromstring(page.text)
# buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
# buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
# for i in range(465):
# 	df.loc[4000+i] = [buyers2[i], buyers[i]]





















# importing libraries

import urllib2
from bs4 import BeautifulSoup

# url
quote_page = 'https://s3-us-west-1.amazonaws.com/ra-training/test1.html'

# get html page
page = urllib2.urlopen(quote_page)

# parse the page into BeautifulSoup
souppage = BeautifulSoup(page, 'html.parser')
prettyhtml = souppage.prettify()

f = open("output.html", "w+")
f.write(prettyhtml)
f.close()

# Summary
# For this exercise, I imported the libraries urllib2 and BeatuifulSoup. 
# I then created a variable that held the url string of the page I was accessing. 
# After that, I open the html page of the url in the variable called page. 
# In the variable called souppage, I parse the page into BeatuifulSoup, 
# prettify the text into prettyhtml and then open an output file and write the text to the file.
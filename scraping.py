from bs4 import BeautifulSoup
import requests as rq
import re
import warnings




base_url = "http://jobsearch.monsterindia.com/jobresults/it-jobs.html"
r = rq.get(base_url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

num_pages = 785
#currentPage=Math.ceil(currentItem/itemsPerPage) therefore num_pages = (31386/40)
#manually calculated

# Add 1 because Python range.
url_list = ["{}?page={}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

for url_ in url_list:
    stack = []
    print "Processing {}...".format(url_)
    r_new = rq.get(url_)
    soup_new = BeautifulSoup(r_new.text,"html.parser")
    for link in soup_new.find_all('a'):
        print(link.text.encode('ascii','ignore'))



import requests
import re
import csv
from lxml import html
from bs4 import BeautifulSoup

regex_facebook = r"(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
regex_instagram = r"(?:(?:http|https):\/\/)?(?:www.)?instagram.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
regex_twitter = r"(?:(?:http|https):\/\/)?(?:www.)?twitter.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"

all_len = []
all_field = []
uniq = []
all_link = []
sales_emails = []

names = []
descriptions = []
whereIs = []
c1list = []
c2list = []
c3list = []
c4list = []
c5list = []
d1list = []
d2list = []
d3list = []
d4list = []
d5list = []
d6list = []
e1list = []
e2list = []
e3list = []
e4list = []
e5list = []
e6list = []
f1list = []
f2list = []
f3list = []
f4list = []
f5list = []
f6list = []
web_sites = []
fbs = []
instagrams = []
twitters = []

base_url = 'http://capsuleshow.com'
start_urls = ["http://capsuleshow.com/brands?page={}&view=list".format(x) for x in range(1, 26)]
for url in start_urls:
    r = requests.get(url)
    tree = html.fromstring(r.content)
    links = tree.xpath("//*[@id='brand-list']//a/@href")
    for link in links:
        all_link.append(base_url+link)


for profile in all_link:
    r = requests.get(profile)
    soup = BeautifulSoup(r.text)
    tree = html.fromstring(r.content)
    print(profile)

    try:
        name = soup.find('h2').text.strip()
    except:
        name = None
    try:
        where = soup.find('p',{'class', 'country'}).text.strip()
    except:
        where = None
    try:
        description = soup.find("blockquote").text.strip()
    except:
        description = None

    names.append(name)
    whereIs.append(where)
    descriptions.append(description)

    allh6 = soup.findAll('h6')
    # contact_info = allh6[0]
    # sales = allh6[1]
    # add_sales = allh6[2]
    # pr = allh6[3]
    # soc = soup.find('ul',{'class', 'soc-links list-unstyled'})
    # ss = soc.findAll('a')

    c1 = None
    c2 = None
    c3 = None
    c4 = None
    c5 = None
    d1 = None
    d2 = None
    d3 = None
    d4 = None
    d5 = None
    d6 = None
    e1 = None
    e2 = None
    e3 = None
    e4 = None
    e5 = None
    e6 = None
    f1 = None
    f2 = None
    f3 = None
    f4 = None
    f5 = None
    f6 = None

    for h6 in allh6:
        if h6.text == 'Contact information:':
            try:
                c1 = h6.nextSibling.nextSibling.text.strip()
            except:
                c1 = None
            try:
                c2 = h6.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                c2 = None
            try:
                c3 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                c3 = None
            try:
                c4 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                c4 = None
            try:
                c5 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                c5 = None

        # else:
        #     c1 = None
        #     c2 = None
        #     c3 = None
        #     c4 = None
        #     c5 = None

        c1list.append(c1)
        c2list.append(c2)
        c3list.append(c3)
        c4list.append(c4)
        c5list.append(c5)

    for h6 in allh6:
        if h6.text == 'Sales:':
            try:
                d1 = h6.nextSibling.nextSibling.text.strip()
            except:
                d1 = None
            try:
                d2 = h6.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                d2 = None
            try:
                d3 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                d3 = None
            try:
                d4 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                d4 = None
            try:
                d5 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                d5 = None
            try:
                d6 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                d6 = None
        #
        # else:
        #     d1 = None
        #     d2 = None
        #     d3 = None
        #     d4 = None
        #     d5 = None
        #     d6 = None



        d1list.append(d1)
        d2list.append(d2)
        d3list.append(d3)
        d4list.append(d4)
        d5list.append(d5)
        d6list.append(d6)

    for h6 in allh6:
        if h6.text == 'Additional Sales Contact:':
            try:
                e1 = h6.nextSibling.nextSibling.text.strip()
            except:
                e1 = None
            try:
                e2 = h6.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                e2 = None
            try:
                e3 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                e3 = None
            try:
                e4 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                e4 = None
            try:
                e5 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                e5 = None
            try:
                e6 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                e6 = None
		
    # else:
    #     e1 = None
    #     e2 = None
    #     e3 = None
    #     e4 = None
    #     e5 = None
    #     e6 = None

    e1list.append(e1)
    e2list.append(e2)
    e3list.append(e3)
    e4list.append(e4)
    e5list.append(e5)
    e6list.append(e6)
	
    for h6 in allh6:
        if h6.text == 'Marketing and PR:':
            try:
                f1 = h6.nextSibling.nextSibling.text.strip()
            except:
                f1 = None
            try:
                f2 = h6.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                f2 = None
            try:
                f3 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                f3 = None
            try:
                f4 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                f4 = None
            try:
                f5 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                f5 = None
            try:
                f6 = h6.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
            except:
                f6 = None
		
    # else:
    #     f1 = None
    #     f2 = None
    #     f3 = None
    #     f4 = None
    #     f5 = None
    #     f6 = None

    f1list.append(f1)
    f2list.append(f2)
    f3list.append(f3)
    f4list.append(f4)
    f5list.append(f5)
    f6list.append(f6)

    try:
        web_site = soup.find('ul',{'class', 'soc-links list-unstyled'}).find('a').get('href').strip()
    except:
        web_site = None

    web_sites.append(web_site)

    soc = soup.find('ul', {'class', 'soc-links list-unstyled'})
    try:
        p = re.compile(regex_facebook)
        facebook = p.search(str(soc)).group()
    except:
        facebook = None
    try:
        p = re.compile(regex_instagram)
        instagram = p.search(str(soc)).group()
    except:
        instagram = None
    try:
        p = re.compile(regex_twitter)
        twitter = p.search(str(soc)).group()
    except:
        twitter = None

    fbs.append(facebook)
    instagrams.append(instagram)
    twitters.append(twitter)
    
    print(len(names))
    print(len(e1list))
    print('pause')




# ['Contact information:', 'Sales:', 'Additional Sales Contact:', 'Marketing and PR:', 'On the web:', 'Similar brands']
# similar brands do not
print('ready!')

# http://capsuleshow.com/brand/18waits

with open ('ex.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    for row in zip(all_link, names, descriptions, whereIs, c1list, c2list, c3list, c4list, c5list, d1list, d2list, d3list, d4list,
                   d5list, d6list, e1list ,e2list ,e3list ,e4list ,e5list ,e6list ,f1list ,f2list ,f3list ,f4list ,f5list ,f6list, web_sites, fbs, instagrams, twitters ):
        writer.writerow(row)
import requests
import csv
from lxml import html
from bs4 import BeautifulSoup

all_len = []
all_field = []
uniq = []
all_link = []
sales_emails = []
web_site =[]

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
soc1list = []
soc2list = []
soc3list = []
soc4list = []

base_url = 'http://capsuleshow.com'
start_urls = ["http://capsuleshow.com/brands?page={}&view=list".format(x) for x in range(25, 26)]
for url in start_urls:
    r = requests.get(url)
    tree = html.fromstring(r.content)
    links = tree.xpath("//*[@id='brand-list']//a/@href")
    for link in links:
        all_link.append(link)


for profile in all_link:
    r = requests.get(base_url+profile)
    soup = BeautifulSoup(r.text)
    tree = html.fromstring(r.content)
    print(base_url+profile)

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
    contact_info = allh6[0]
    sales = allh6[1]
    add_sales = allh6[2]
    pr = allh6[3]
    soc = soup.find('ul',{'class', 'soc-links list-unstyled'})
    ss = soc.findAll('a')
    if allh6[0].text == 'Contact information:':
        c1 = contact_info.nextSibling.nextSibling.text.strip()
        c2 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        c3 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        c4 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        c5 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        
    if allh6[1].text == 'Sales:':
        d1 = sales.nextSibling.nextSibling.text.strip()
        d2 = sales.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        d3 = sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        d4 = sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        d5 = sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        d6 = sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
    if allh6[2].text == 'Additional Sales Contact:':
        e1 = add_sales.nextSibling.nextSibling.text.strip()
        e2 = add_sales.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        e3 = add_sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        e4 = add_sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        e5 = add_sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        e6 = add_sales.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()        
    if allh6[3].text == 'Marketing and PR:':
        f1 = pr.nextSibling.nextSibling.text.strip()
        f2 = pr.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        f3 = pr.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        f4 = pr.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        f5 = pr.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        f6 = pr.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()                
        
    soc1 = ss[0].get('href')
    soc2 = ss[1].get('href')
    soc3 = ss[2].get('href')
    soc4 = ss[3].get('href')
    all_len.append(len(tree.xpath("//h6/text()")))#max 6
    all_field.append(tree.xpath("//h6/text()"))
    for i in all_field:
        for y in i:
            uniq.append(y)


# ['Contact information:', 'Sales:', 'Additional Sales Contact:', 'Marketing and PR:', 'On the web:', 'Similar brands']
# similar brands do not
print('ready!')

# http://capsuleshow.com/brand/18waits

#with open ('ex.csv','w',encoding='utf8') as csvfile:
    #writer = csv.writer(csvfile)
    #for row in zip(urls,names,websites,professions,categories,places,looking_for_list,profile_descriptions,emails,facebooks,instagrams,pinterests,snapchats):
        #writer.writerow(row) 
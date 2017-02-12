import requests
import csv
from lxml import html
from bs4 import BeautifulSoup

all_len = []
all_field = []
uniq = []
all_link = []
names = []
sales_emails = []
web_site =[]


base_url = 'http://capsuleshow.com'
start_urls = ["http://capsuleshow.com/brands?page={}&view=list".format(x) for x in range(1, 2)]
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
    print(tree.xpath("//h6/text()"))
    name = soup.find('h2').text.strip()
    where = soup.find('p',{'class', 'country'}).text.strip()
    description = soup.find("blockquote").text.strip()
    allh6 = soup.findAll('h6')
    contact_info = allh6[0]
    sales = allh6[1]
    add_sales = allh6[2]
    pr = allh6[3]
    soc = soup.find('ul',{'class', 'soc-links list-unstyled'})
    ss = soc.findAll('a')
    if allh6[0].text == 'Contact information:':
        ci1 = contact_info.nextSibling.nextSibling.text.strip()
        ci2 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci3 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci4 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci5 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        
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
import requests
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
    tree = html.fromstring(r.content)
    print(base_url+profile)
    print(tree.xpath("//h6/text()"))
    name = soup.find('h2').text.strip()
    where = soup.find('p',{'class', 'country'}).text.strip()
    description = soup.find("blockquote").text.strip()
    contact_info = soup.find('h6')
    allh6 = soup.findAll('h6')
    if contact_info.text == 'Contact information:':
        ci1 = contact_info.nextSibling.nextSibling.text.strip()
        ci2 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci3 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci4 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
        ci5 = contact_info.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text.strip()
    all_len.append(len(tree.xpath("//h6/text()")))#max 6
    all_field.append(tree.xpath("//h6/text()"))
    for i in all_field:
        for y in i:
            uniq.append(y)


# ['Contact information:', 'Sales:', 'Additional Sales Contact:', 'Marketing and PR:', 'On the web:', 'Similar brands']
# similar brands do not
print('ready!')

# http://capsuleshow.com/brand/18waits
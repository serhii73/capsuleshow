import requests
from lxml import html

all_len = []
all_field = []
uniq = []
all_link = []


base_url = 'http://capsuleshow.com'
start_urls = ["http://capsuleshow.com/brands?page={}&view=list".format(x) for x in range(1, 26)]
for url in start_urls:
    r = requests.get(url)
    tree = html.fromstring(r.content)
    links = tree.xpath("//*[@id='brand-list']//a/@href")
    for link in links:
        all_link.append(link)


for profile in all_link:
    r = requests.get(base_url+profile)
    tree = html.fromstring(r.content)
    # name = tree.xpath("//h2/text()")
    # where = tree.xpath("//p[@class='country']//text()")
    all_len.append(len(tree.xpath("//h6/text()")))#max 6
    all_field.append(tree.xpath("//h6/text()"))
    for i in all_field:
        for y in i:
            uniq.append(y)

# ['Sales:',
#  'On the web:',
#  'Contact information:',
#  'Marketing and PR:',
#  'Additional Sales Contact:',
#  'Similar brands']

print('ready!')
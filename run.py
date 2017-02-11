import requests
from lxml import html

all_len = []
all_field = []


base_url = 'http://capsuleshow.com'
url = 'http://capsuleshow.com/brands?page=1&view=list'
r = requests.get(url)
tree = html.fromstring(r.content)
links = tree.xpath("//*[@id='brand-list']//a/@href")

for profile in links:
    r = requests.get(base_url+profile)
    tree = html.fromstring(r.content)
    # name = tree.xpath("//h2/text()")
    # where = tree.xpath("//p[@class='country']//text()")
    all_len.append(len(tree.xpath("//h6/text()")))
    all_field.append(tree.xpath("//h6/text()"))



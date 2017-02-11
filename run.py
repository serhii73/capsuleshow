import requests
url = 'http://capsuleshow.com/brands?page=1&view=list'

r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)
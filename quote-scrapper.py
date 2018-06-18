from bs4 import BeautifulSoup
import requests

res = requests.get('http://www.simplesite.com/go/cms/features/features')
soup = BeautifulSoup(res.text, 'lxml')

quote = soup.find_all('div', {'class' : 'product-feature-block grid-block large-3 medium-6 small-12 vertical'})

for q in quote:
	msg = q.find('div', {'class' : 'product-feature-title grid-block shrink align-center text-center IE-width-fix'})

	print(msg.text)

	des = q.find('div', { 'class' : 'product-feature-text grid-block align-center text-center IE-width-fix'})

	print(des.text)


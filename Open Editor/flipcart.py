from bs4 import


url = 'https://www.flipkart.com/search?q=flipkart
page = requests.get(url)
if not page.status_code == 200:
    print('An error occurred.')
    exit()
soup = BeautifulSoup(page.text, 'html5lib')

items = soup.find_all('div', class_='_2B099V')
for item in items:
    name = 
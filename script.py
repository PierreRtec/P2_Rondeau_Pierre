import requests
from bs4 import BeautifulSoup 


def scraping_book():
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one('.product_main h1').text      # remplace find("div", {"class": "col-sm-6 product_main"}).find("h1")
        print(title)
        description = product_description(soup)
        category = product_category(soup)
        upc = universal_product_code(soup)
        image_url = product_image_url(soup)
        number = product_number_available(soup)
        including = product_price_including(soup)
        excluding = product_price_excluding(soup)
        review_rating = product_review_rating(soup)

     
def product_description(soup):
  description = soup.select_one('.sub-header ~ p').text
  print(description)
  return description

def product_category(soup):
  category = soup.select('.breadcrumb li')[-2].text
  print(category)
  return category

def universal_product_code(soup):
  upc = soup.find_all('td')[-0].text
  table = soup.find('table')
  table_rows = table.find_all('tr')
  print(upc)
  return upc

def product_image_url(soup):
  image_url = soup.find('img')['src']
  print(image_url)
  return image_url

def product_number_available(soup):
  number = soup.find_all('td')[5].text
  table = soup.find('table')
  table_rows = table.find_all('tr')
  print(number)
  return number

def product_price_including(soup):
  including = soup.find_all('td')[3].text
  table = soup.find('table')
  table_rows = table.find_all('tr')
  print(including)
  return including
  
def product_price_excluding(soup):
  excluding = soup.find_all('td')[2].text
  table = soup.find('table')
  table_rows = table.find_all('tr')
  print(excluding)
  return excluding

def product_review_rating(soup):
  review_rating = soup.find('p', 'star-rating')['class'][1]
  print(review_rating)
  return review_rating
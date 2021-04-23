import requests
import csv
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scraping_category():
  pass

def get_all_categories(url):
  link_urls = []
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  if response.ok:
    menu = soup.find(class_="side_categories")
    links = menu.find_all('a')
    for link in links:
        link_urls.append(urljoin(url, link["href"]))
        print(link_urls)
  return link_urls[1:]



def get_all_urls_book_from_one_category():
  pass

def get_all_url_book_in_categories():
  pass









def save_book_info_to_csv(book_info: dict):
    with open("book_info_to.csv", "w", encoding="utf-8-sig"
    ) as csvfile:
      writer = csv.DictWriter(csvfile, book_info, dialect="excel")
      writer.writeheader()
      writer.writerow(book_info)

def scraping_book():
    url_book = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    response = requests.get(url_book)  
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one(".product_main h1").text
        print(title)
        description = product_description(soup)
        category = product_category(soup)
        upc = universal_product_code(soup)
        image_url = product_image_url(soup)
        number = product_number_available(soup)
        including = product_price_including(soup)
        excluding = product_price_excluding(soup)
        review_rating = product_review_rating(soup)
        return {
          "title": title,
          "description": description,
          "category": category,
          "upc": upc,
          "image_url": image_url,
          "number": number,
          "including": including,
          "excluding": excluding,
          "review_rating": review_rating,
          }   
     
def product_description(soup):
  description = soup.select_one(".sub-header ~ p").text
  print(description)
  return description

def product_category(soup):
  category = soup.select(".breadcrumb li")[-2].text
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
  number = soup.find_all("td")[5].text
  table = soup.find("table")
  table_rows = table.find_all("tr")
  print(number)
  return number

def product_price_including(soup):
  including = soup.find_all("td")[3].text
  table = soup.find("table")
  table_rows = table.find_all("tr")
  print(including)
  return including
  
def product_price_excluding(soup):
  excluding = soup.find_all("td")[2].text
  table = soup.find("table")
  table_rows = table.find_all("tr")
  print(excluding)
  return excluding

def product_review_rating(soup):
  review_rating = soup.find("p", "star-rating")["class"][1]
  print(review_rating)
  return review_rating
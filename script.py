import requests
import csv
import urllib3
from slugify import slugify
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve


def scraping_category(url_category):
  link_urls = []
  response = requests.get(url_category)
  if response.ok:
    soup = BeautifulSoup(response.content, "html.parser")
    category_to_scrap = soup.find(class_="side_categories")
    links = category_to_scrap.select("a")
    for link in links:
      link_urls.append(urljoin(url_category, link["href"]))
    print(link_urls[33])
  return link_urls
    


def get_all_categories(url):
  link_urls = []
  response = requests.get(url)
  if response.ok:
    soup = BeautifulSoup(response.content, "html.parser")
    menu = soup.find(class_="side_categories")
    links = menu.find_all("a")
    for link in links:
        link_urls.append(urljoin(url, link["href"]))
    print(link_urls)
  return link_urls



def get_all_urls_book_from_one_category(url):
    link_urls = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        all_urls_book = soup.select("h3 a")
        for link in all_urls_book:
            link_urls.append(urljoin(url, link["href"]))
    # Y a-t-il une page suivante ?
    next_button = soup.select_one(".next a")
    if next_button is not None:
        # Oui, il y a un bouton next -> on répète la même fonction sur la page
        link_urls += get_all_urls_book_from_one_category(
            urljoin(url, next_button["href"])
        )
    return link_urls



def get_all_url_book_in_categories(url_all_book_category):
    link_urls = []
    response = requests.get(url_all_book_category)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        menu = soup.find(class_="side_categories")
        links = menu.find_all("a")
        for link in links:
            link_urls.append(urljoin(url_all_book_category, link["href"]))
        for link in link_urls:
            book_urls = get_all_urls_book_from_one_category(link)
            book_info_list = []
            for url_all_book_category in book_urls:
              book_info = scraping_book(url_all_book_category)
              book_info_list.append(book_info)
            save_book_info_to_csv(book_info_list)
    return link_urls






def save_book_info_to_csv(book_info_list: list):
    first_book_info = book_info_list[0]
    category = first_book_info["category"].strip()
    with open(f"Scraping/{category}.csv", "w", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, first_book_info, dialect="excel")
        writer.writeheader()
        for book_info in book_info_list:
          writer.writerow(book_info)


def scraping_book(url_book):
    response = requests.get(url_book)  
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one(".product_main h1").text
        print(title)
        description = product_description(soup)
        category = product_category(soup)
        upc = universal_product_code(soup)
        image_url = url_book, product_image_url(soup)
        urlretrieve(book_info["image_name"]) 
        number = product_number_available(soup)
        including = product_price_including(soup)
        excluding = product_price_excluding(soup)
        review_rating = product_review_rating(soup)
        image_name = f"Images/{slugify(title)}.{image_url[-4:]}"
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
    description_element = soup.select_one(".sub-header ~ p")
    if description_element is not None:
      description = description_element.text
    else:
      description = ""
    return description

def product_category(soup):
  category = soup.select(".breadcrumb li")[-2].text
  print(category)
  return category

def universal_product_code(soup):
  upc = soup.find_all("td")[-0].text
  table = soup.find("table")
  table_rows = table.find_all("tr")
  print(upc)
  return upc

def product_image_url(soup):
  image_url = soup.find("img")["src"]
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
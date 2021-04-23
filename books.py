import script


def main():
    url_travel = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    script.get_all_urls_book_from_one_category(url_travel)



if __name__ == "__main__":
   main()
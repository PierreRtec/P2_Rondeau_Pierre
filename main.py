import script


def main():
   url_book = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
   book_info = script.scraping_book(url_book)
   script.save_book_info_to_csv(book_info)


if __name__ == "__main__":
   main()
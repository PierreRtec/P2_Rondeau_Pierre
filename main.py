import script


def main():
   book_info = script.scraping_book()
   script.save_book_info_to_csv(csvfile, book_info)


if __name__ == "__main__":
   main()
"""Module de lancement du projet."""

import scraper.utils as utils


def main():
    """Point d'entrée principal de l'application."""
    url_all_book_category = "http://books.toscrape.com"
    utils.get_all_url_book_in_categories(url_all_book_category)
                             


if __name__ == "__main__":
    main()
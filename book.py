import requests

class Book:
    def __init__(self, title, authors,
                genre, img_link):
        self.title = title
        self.authors = authors
        self.genre = genre
        self.img_link = img_link

    def __str__(self):
        names = ", ".join(self.authors)
        return f"{self.title} by {names}\n{self.genre} {self.img_link}"

class BookFetcher:
    url = "https://www.googleapis.com/books/v1/volumes?q=python"

    @staticmethod
    def fetch_book():
        response = requests.get(BookFetcher.url)
        if response.status_code == 200:
            book_items = response.json()
        else:
            book_items = []
        book_items = book_items["items"]
        books = []
        for item in book_items:
            #imageLinks
            book_obj = Book(
                item["volumeInfo"].get("title", "NO Title"),
                item["volumeInfo"].get("authors", ['Unknown']),
                item["volumeInfo"].get("categories", ['Unknown'])[0],
                item["volumeInfo"].get("imageLinks", "No Link")
            )
            books.append(book_obj)
        return books

if __name__ == "__main__":
    book_fetcher = BookFetcher()
    res = book_fetcher.fetch_book()
    for book in res:
        print(book)

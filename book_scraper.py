import requests
from bs4 import BeautifulSoup


def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p.get("class")[1]

        print(f"📖 Название: {title}\n💰 Цена: {price}\n⭐ Рейтинг: {rating}\n{'-' * 40}")


if __name__ == "__main__":
    scrape_books()

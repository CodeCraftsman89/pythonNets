import matplotlib.pyplot as plt
import time
import requests  # импортируем для запроса HTML страницы
from bs4 import BeautifulSoup  # импортируем для парсинга
import matplotlib.pyplot as plt

def parse_count_posts(lang: str) -> int:
    headers = {
        "Accept": "text/html,application/xhtml+xml,"
                  "application/xml;q=0.9,image/avif,image/webp,image/apng,"
                  "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36"
    }


    page = "1"
    url = f"https://habr.com/ru/hubs/{lang}/articles/page{page}/"

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        posts = soup.find_all("article")
        a_pages = soup.find_all(name="a", attrs={"class": "tm-pagination__page"})
        last_page = a_pages[-1].text  #
        print("Страниц хаба:", last_page)
        print("Постов на страницах:", len(posts) * (int(last_page) - 1))
        count_posts = len(posts) * (int(last_page) - 1)
        url = f"https://habr.com/ru/hubs/{lang}/articles/page{last_page}/"
        time.sleep(0.5)
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            posts = soup.find_all("article")
            print(len(posts))
            count_posts += len(posts)
            print(count_posts)
            return count_posts
        print(f"ОШИБКА запроса: {res.status_code}")
    return 0

langs = ["c", "cpp", "csharp", "python", "rust", "ruby", "go", "java", "javascript"]
for lang in langs:
    parse_count_posts(lang)
    time.sleep(0.5)


x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y)
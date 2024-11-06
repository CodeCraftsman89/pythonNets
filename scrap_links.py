from bs4 import BeautifulSoup as BS

file = open("habr.html", encoding="utf-8")
text = file.read()
file.close()

soup = BS(text, "html.parser")

links = soup.find_all(name="a", recursive=True)

print("Все ссылки")
for link in links:
    print(link.get("href"))

posts = soup.article.parent
contents = posts.contents
titles = posts.find_all(name="h2")
for content in contents:
    if content.name == "article":
        print("Все ссылки в посте")
        links_in_post = content.find_all(name="a", recursive=True)
        for link in links_in_post:
            print(link.text, "-", link.get("href"))
        print("Все заголовки")
        for title in titles:
            print(title.text)
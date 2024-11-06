from bs4 import BeautifulSoup as BS

file = open("habr.html", encoding="utf-8")
text = file.read()
file.close()


def print_arguments(tag):
    print(tag.name)
    print(tag.attrs)
    print(tag.string)
    print(tag.text)
    print("")


soup = BS(text, "html.parser")

'''
head = soup.head
title = head.title
link = head.link
a = soup.a
title_a = soup.a.title

tags = [head, title, link, a, title_a]

# print(head)
for tag in tags:
    print_arguments(tag)
    '''
post = soup.article
user_nick = soup.article.a["title"]
user_link = soup.article.a["href"]
user_avatar = soup.article.img["src"]
post_time = soup.article.time["title"]

post_parent = post.parent

print(user_nick)
print(user_link)
print(user_avatar)
print(post_time)
print("")
print(type(post_parent))
print(post_parent.name, post_parent.attrs)

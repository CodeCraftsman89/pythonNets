from bs4 import BeautifulSoup as BS

file = open("habr.html", encoding="utf-8")
text = file.read()
file.close()

posts_ids = []
posts_names = []
posts_authors = []
posts_votes = []
posts_bookmarks = []
posts_comments = []

soup = BS(text, "html.parser")

posts = soup.article.parent
contents = posts.contents
for content in contents:
    if content.name == "article":
        '''print(content.previous_element)
        print(content.next_element)'''
        article_contents = content.contents
        article_content = article_contents[1]
        button_contents = article_content.contents
        button_content = button_contents[3]
        comment_content = button_contents[5]

        post_id = content["id"]
        post_name = content.h2.a.span.text
        post_autor = content.a["title"]
        post_votes = article_content.span["title"]
        post_bookmarks = button_content.text
        post_comments = comment_content.text

        posts_ids.append(post_id)
        posts_names.append(post_name)
        posts_authors.append(post_autor)
        posts_votes.append(post_votes)
        posts_bookmarks.append(post_bookmarks)
        posts_comments.append(post_comments)

post_info = [(posts_ids[index], posts_names[index], posts_authors[index], posts_votes[index], posts_bookmarks[index], posts_comments[index]) for index in range(len(posts_ids))]

for post in post_info:
    print(post)


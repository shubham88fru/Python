from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)

#all anchor tags
all_anchors = soup.find_all(name="p")

for tag in all_anchors:
    print(tag.getText())
    tag.get("href")

heading = soup.find(name="h1", id="name")

section_heading = soup.find(name="h3", class_="heading")
section_heading.get("class")

company_url = soup.select_one(selector="p a")
all_class_heading = soup.select(".heading")

#############################################
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
article_upvotes.index(largest_number)

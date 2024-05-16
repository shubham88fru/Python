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
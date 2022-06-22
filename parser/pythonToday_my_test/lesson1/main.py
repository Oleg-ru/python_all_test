from bs4 import BeautifulSoup

with open('blank/index.html', encoding="utf-8") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'lxml')
title = soup.title

print(title.text)


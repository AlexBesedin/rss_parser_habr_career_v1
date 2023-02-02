from bs4 import BeautifulSoup
import requests
import csv
from time import sleep


def rss_habr_jobs_parser(content):
    soup = BeautifulSoup(content, 'xml')
    entries = soup.find_all('item')

    with open('career.csv', 'w', encoding='utf8', newline='') as csvfile:
        write = csv.writer(csvfile)
        header = ['author', 'title', 'description', 'link', 'pubDate']
        write.writerow(header)

        for entry in entries:
            author = entry.author.text
            title = entry.title.text
            description = entry.description.text
            link = entry.link.text
            pubDate = entry.pubDate.text
            info = [author, title, description, link, pubDate]
            write.writerow(info)


print('Cкрапер RSS-канала активирован')
sleep(3)
print('Запись файла завершена!')


def main():
    url = 'https://career.habr.com/vacancies/rss'
    content = requests.get(url).content
    rss_habr_jobs_parser(content)


if __name__ == "__main__":
    main()
    
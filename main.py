from bs4 import BeautifulSoup
import requests
from csv import writer
from time import sleep


def rss_habr_jobs_parser(url: str):
    soup = BeautifulSoup(url.content, 'xml')
    entries = soup.find_all('item')

    with open('career.csv', 'w', encoding='utf8') as csvfile:
        write = writer(csvfile)
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
    url = requests.get('https://career.habr.com/vacancies/rss?currency=RUR&q=python&sort=relevance&type=all')
    rss_habr_jobs_parser(url)


if __name__ == "__main__":
    main()

## RSS HABR CAREER ПАРСЕР v1.

Простейший RSS HABR CAREER парсер, который собирает 50 первых вакансий по вашему запросу и сохраняет csv файл.

## Установка, Как запустить проект:

```sh
git clone git@github.com:AlexBesedin/rss_parser_habr_career_v1.git
```
```sh
cd rss_parser_habr_career_v1
```
Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
```
Если у вас Linux/macOS
```sh
source env/bin/activate
```
Если у вас windows
```sh
source env/scripts/activate
```

```sh
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```

Далее на сайте https://career.habr.com/ прописывает необходимый запрос по интересующим вас вакансиям, нажимаете RSS и копируете ссылку. 
Далее вставляете ссылку в url в функции def main() и запускаете программу.

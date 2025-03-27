### Hexlet tests and linter status:
[![Actions Status](https://github.com/Kloym/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Kloym/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/243c8fb73479ed6d03a3/maintainability)](https://codeclimate.com/github/Kloym/python-project-83/maintainability)
&nbsp;<div align="center">
[![E-Mail](https://img.shields.io/badge/email-reveal-2a8?style=flat-square&logo=gmail&logoColor=white)](mailto:iserifom@mail.ru)
</div>
# Анализатор страниц

Сайт проверки сайтов на SEO-пригодность
Позволяет получить тему, заголовок и описание сайта

## В проекте использован Python 3.12, Pip 24.0, uv 0.6.5
Для разработки использовались следующие инструменты:

Flask — фреймворк для создания веб-приложений на языке программирования Python

Gunicorn — минивеб-сервер, осуществляющий запуск Python-приложения

Requests — библиотека для языка Python, осуществляющая работу с HTTP-запросами

BeautifulSoup — библиотека Python, используемая для парсинга HTML и XML документов

Black - простой и удобный линтер

## Clon project
```python3
git clone https://github.com/Kloym/python-project-83
cd python-project-83
```
Для хранения конфиденциональной информации создать файл .env в директории 
page-analyzer 

DATABASE_URL = postgresql://{username}{password}@{host}:{port}/{basename}

SECRET_KEY = "{your_secret_key}"

## Instll
```python3
make install
```
## Start localhost
```python3
make dev
```

## Start deploy
```python3
make render-start
```

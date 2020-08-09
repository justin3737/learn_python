# Python 學習筆記
學習 python 的資源筆記，紀錄學習 python 的過程。

### 學習 Django
- Python新手使用Django架站技術實作：活用Django 2.0 Web Framework建構動態網站的16堂課
[自主學習examle](https://github.com/justin3737/learn_python/tree/master/book_django_2_web_framewoek)

- [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

### 學習 RESTful API
- [Django rest framework tutorial](https://github.com/twtrubiks/django-rest-framework-tutorial/)


---
# 環境與指令
### 初始化環境設定
[Visual Studio Code Python 基本設定篇](https://www.youtube.com/watch?v=tS4beaq9ies)


請先確認電腦有安裝 [Python](https://www.python.org/)
> brew install python3

請在你的命令提示字元 (cmd ) 底下輸入

安裝 [Django](https://github.com/django/django)

>pip install django

安裝 [Django-REST-framework](http://www.django-rest-framework.org/)
>pip install djangorestframework

安裝 venv
> $ pip install virtualenv
---
### 在虛擬環境下開發，避免Global環境被污染

```
# Setup virtualenv if not already present
virtualenv venv

# Activate virtualenv
source venv/bin/activate

# Deactivate Virtualenv
deactivate

# Install requirements, you only need to do this once
pip install -r requirement.txt

```
---
# Django 指令
### 啟動Django
> python manage.py runserver

### 建立Super User
> python manage.py createsuperuser

### makemigrations
> python manage.py makemigrations

### migrate
> python manage.py migrate

### python shell 執行 ORM
> python manage.py shell

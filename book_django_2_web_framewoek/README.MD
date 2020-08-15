
# 自主學習examle: Python新手使用Django架站技術實作：活用Django 2.0 Web Framework建構動態網站的16堂課
 - 04 深入了解Django的MVC架構
 - 07 Models 與資料庫
 - 08 網站表單應用

## 環境與指令
### 初始化環境設定
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
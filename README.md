# Система учета посетителей

---

## Доступные страницы:

| URL                           | Описание |
|--------------------------------|----------|
| (http://127.0.0.1:8000/) | Ввод посетителей |
| (http://127.0.0.1:8000/output/) | Просмотр списка посетителей |
| (http://127.0.0.1:8000/analytics/) | Аналитика посещаемости |

---
### 1 **Склонируйте репозиторий**
```bash
git clone https://github.com/Hashira10/Visitors-project
cd Visitors-project/visitors_project
```

### 2 **Создайте и активируйте виртуальное окружение**
```bash
python -m venv venv  
```
Windows (cmd):
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```

### 3 **Установите зависимости**
```bash
pip install -r requirements.txt
```

### 4 **Настройте переменные окружения**

Создайте файл .env в корневой папке проекта Для Windows (cmd / PowerShell):
```bash
echo EMAIL_HOST_USER=your_email@example.com > .env
echo EMAIL_HOST_PASSWORD=your_password >> .env
```


### 5 **Примените миграции**
```bash
python manage.py migrate
```
### 6 **Запустите сервер**
```bash
python manage.py runserver
```

Приложение будет доступно по адресу http://127.0.0.1:8000/.

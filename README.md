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
или скачайте  Code → Download ZIP
Распакуйте архив и перейдите в папку:
```bash
cd Visitors-project-main/visitors_project
```
### 2 **Создайте и активируйте виртуальное окружение**
```bash
python -m venv venv  
```
Windows (cmd):
```bash
venv\Scripts\activate
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

**Установите Python:**
Перейдите на официальный сайт Python ( https://www.python.org/downloads/ ) и скачайте последнюю версию Python 3.x.
При установке поставьте галочку "Add Python to PATH", иначе команды python и pip не будут работать.
После установки проверьте, что Python установлен:
```bash
python --version
```
**Установите Git:**
 Скачайте и установите Git (https://git-scm.com/downloads), чтобы можно было склонировать репозиторий.
 После установки проверьте:
 ```bash
 git --version
 ```

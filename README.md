
# Estate Agent - Система управления недвижимостью

![Django](https://img.shields.io/badge/Django-5.2.3-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

Система для риэлторов и агентств недвижимости с функционалом управления объявлениями, статистикой и профилями пользователей.

## 🚀 Основные возможности

### 📊 Панель управления агента
- Общая статистика по объявлениям
- Топ-3 городов по активности
- Средние цены по типам недвижимости

### 🏠 Управление объявлениями
- Создание/редактирование/удаление объявлений
- Фильтрация по статусу (активно/продано)
- Детальная информация по объектам

### 👤 Аутентификация пользователей
- Регистрация новых агентов
- Авторизация с запоминанием сессии
- Кастомизированная модель пользователя

## 🛠 Технологический стек

- **Бэкенд**: Django 5.2.3
- **База данных**: PostgreSQL
- **Фронтенд**: Django Templates + Bootstrap
- **Дополнительно**:
  - Аутентификация через кастомную модель UserProfile
  - Загрузка файлов через MEDIA_ROOT
  - Переменные окружения (.env)

## 📋 Предварительные требования

- Python 3.10+
- PostgreSQL 15+
- pip и virtualenv

## ⚡ Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-repo/estate-agent.git
cd estate-agent
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate    # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка окружения
Создайте файл `.env` и `.env.docker-compose` в корне проекта по аналогии `.env.example`


### 5. Настройка базы данных
```bash
# Выполнить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
```

### 6. Запуск сервера
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/

## 📁 Структура проекта

```
estate_agent/
├── listings/              # Приложение объявлений
│   ├── models.py         # Модели недвижимости
│   ├── views.py          # Логика работы с объявлениями
│   ├── forms.py          # Формы создания/редактирования
│   └── urls.py           # Маршруты приложения
│
├── users/                # Приложение пользователей
│   ├── models.py         # Кастомная модель UserProfile
│   ├── manager.py        # Менеджер аутентификации
│   ├── views.py          # Регистрация/авторизация
│   └── forms.py          # Формы пользователей
│
├── templates/            # HTML шаблоны
├── static/               # CSS/JS/Изображения
├── media/                # Загруженные файлы
├── requirements.txt      # Зависимости проекта
├── .env.example         # Пример файла окружения
└── estate_agent/         # Настройки проекта
    ├── settings.py       # Основные настройки
    └── urls.py           # Главные маршруты
```



## 🔧 Дополнительные команды

### Поднять базу в Docker:
```bash
 docker-compose up 
 ```


### Сбор статических файлов
```bash
python manage.py collectstatic
```

### Создание миграций
```bash
python manage.py makemigrations
```

### Загрузка тестовых данных
```bash
python manage.py loaddata fixtures/sample_data.json
```

## 🚦 Основные маршруты

- `/` - Главная страница
- `/dashboard/` - Панель управления агента
- `/listings/` - Список объявлений
- `/listings/create/` - Создание объявления
- `/auth/login/` - Авторизация
- `/auth/register/` - Регистрация
- `/admin/` - Административная панель Django




## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request


---


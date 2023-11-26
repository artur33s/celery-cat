# Выбираем базовый образ
FROM python:3.11.6

# Устанавливаем рабочую директорию в контейнере
WORKDIR /src

# Копируем файлы зависимостей в контейнер и устанавливаем их
COPY ./webapp/requirements.txt /src/

# Устанавливаем зависимости Python
RUN pip install -r requirements.txt

# Копируем содержимое папки src в рабочую директорию контейнера
COPY ./webapp/src /src

# Указываем команду для запуска
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

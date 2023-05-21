## Инструкция по запуску проекта
1. Создать venv: `python3 -m venv <venv_name>`
2. Активировать venv: `source venv_name/bin/activate`
3. Устанавливаем зависимости: `pip install -r requirements.txt`
4. Создать DB: `python manage.py migrate`
5. Запуск: `python manage.py runserver`

## Полезные команды
1. Запуск python-terminal: `python manage.py shell_plus --ipython`
2. Инфо о подключенных модулях сохраняется в файл: `pip freeze > requirements.txt`
3. Установка модулей проекта из файла: `pip install -r requirements.txt`


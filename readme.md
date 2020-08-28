API для работы с чеками
Для  корректной работы необходимо:
Python 3.x, Django 3, Django Rest Framework, MySql,Redis

Перед началом введите в консоли команды

pip3 install jsonfield

apt-get update
apt-get install xvfb libfontconfig wkhtmltopdf

Настройки базы можно указать в файле test_api/settings.py
Не забудьте в отдельной консоли запустить воркер для обработки асинхронныых задач django-rq:
python3 manage.py rqworker default

Пример запроса на добавление чека:
```json
{
    "id":"1",
    "point_id":1,
    "type":"1",
    "products":[
        "a",
        "b",
        "c"
    ]
}
```
Примечание : "0" - kitchen / "1" - client
Пример запроса на печать готовых чеков:
http://127.0.0.1:8000/api/?api_key=1a
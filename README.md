# Test_task_Saraphan

Ссылка на тестовое задание - [клац](https://docs.google.com/document/d/1ijSd6t5pSGELWKnvswsKViuVC9fISAeG5J54BHO5W5U/edit)  



## Запуск  
 - Клонировать репозиторий 
 ```
 git clone https://github.com/Pash1et/Test_task_Saraphan.git
 ```  
 - Перейти в папку с проектом
 ```
cd task_2/
 ```
- Создать виртуальное окружение и активировать его
```
python -m venv venv
source venv/Scripts/activate  # для Windows
source venv/bin/activate  # для Linux
```
- Установить зависимости
```
pip install -r requirements.txt
```
- В корне директории task_2 создать файл ```.env``` и заполнить в соответствии с файлом ```.env.example```,  SECRET_KEY можно сгенерировать по [ссылке](https://djecrety.ir/)
- Выполнить миграции 
```
python manage.py migrate
```
- Запустить проект 
```
python manage.py runserver
```
## Документация
Доступна по [ссылке](http://127.0.0.1:8000/api/schema/swagger-ui/) при запущенном приложении
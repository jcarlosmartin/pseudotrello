# Django project for a task management webservice using REST APIs

## Steps to follow for executing the project once it is downloaded

1. Open the project folder in visual studio code (or any other IDE) and open a terminal session inside. Go to the folder where the manage.py file is located, trello folder.

2. Adapt accordingly the database in settings.py to point to yours. In our case we have used MySQL.

3. Create migrations
   ```
   python3 manage.py makemigrations
   ```
4. Execute migrations
   ```
   python3 manage.py migrate
   ```
5. Run the application
   ```
   python3 manage.py runserver
   ```
   This commannd execute the application in port number 8000 by default, which is accesible in http://localhost:8000/

6. To facilitate the testing for CRUD operations a postman collection have been included in the project directory. 

Note: in windows please use py -3 instead of python3 for all commands.


[ABOUT PROGRAM]

Онлайн каталог сотрудников для компаний.

Информация о сотрудниках храниться в базе данных и содержит следующие данные:

    ● ФИО;
    ● Должность;
    ● Дата приема на работу;
    ● Размер заработной платы;
    ● Информация о выплаченной зарплате;

У каждого сотрудника должен быть начальник.
Так же реализована иерархическая структура разделенная на следующие роли:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;

В административной панеле выводятся следующие данные:

    ● ФИО;
    ● Должность;
    ● Ссылка на информацию о начальнике;
    ● Заработная плата в месяц;
    ● Всего выплачено за все время;

В проекте реализованы фильтры по Должности и Уровне.
    Уровень - это глубина вложенности нашей иерархической структуры или по другому
    какое количество ролей сотрудников находится выше по отношению к твоей роли.

Реализована возможность удалить информацию о выплаченной заработной плате за все время.
Для этого воспользуйтесь action методов на странице Employees.

Так же в проекте присутствует  API с конечными точками:

    ● "http://127.0.0.1:8000/api/v1/employee/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_0/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_1/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_2/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_3/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_4/"
    ● "http://127.0.0.1:8000/api/v1/profile/"
    ● "http://127.0.0.1:8000/api/token/"

Данные конечные точки предоставляют доступ к полному списку сотрудников и к списку сотрудников разделенных на уровни.
Внутри "http://127.0.0.1:8000/api/v1/employee/" предусмотрен фильтр по уровню.

curl \
  -H "Authorization: Bearer {access}" \
  http://127.0.0.1:8000/api/token/ -  по данному запросу сотрудник может получить полную информацию о себе.


Однако предварительно ему необходимо будет отправить POST запрос по адресу "http://127.0.0.1:8000/api/token/" с указанием своего
имени пользователя и пароля в JSON формате.

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://127.0.0.1:8000/api/token/

В ответ вы получите:


{

  "access":"Большой набор символов, который необходимо вставить в запрос получения информации о себе.",
  "refresh":""

}

В приложении присутствуют группы:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;


Когда создается пользователь по сигналу в зависимости от роли,
ему добавится группа, сделано это для удобства распределения прав доступа.


В проекте предусмотрены две Celery задачи:

    1. Выплата заработной платы сотрудникам каждые два часа.
    2. При удаление всей информации о выплате заработной платы сотрудникам при условии,
       что необходимо удалить у более чем 20 сотрудников информацию, задача отправляется в Celery.


[REQUIREMENTS]

В самом начале соберем наши контейнеры docker:

    ● docker-compose build

Затем нам необходимо выполнить миграции командами:

    ● docker-compose run web python manage.py makemigrations
    ● docker-compose run web python manage.py migrate

Далее давайте применим еще одну команду, которая создаст группы с нужными правами
и 5 пользователей по одному на каждую роль:

    ● docker-compose run web python manage.py create_group

Данная команда хорошо демонтрирует иерархическую структуру.
Однако вам может понадобится создать еще пользователей для проверки работоспособности Celery задач, для этого воспользуйтесь командой:

    ● docker-compose run web python manage.py create_user

ПРЕДУПРЕЖДЕНИЕ!

Данная команда не придерживается иерархической структуры, а просто создает 20 пользователей.


Создайте superuser командой:

    ● docker-compose run web python manage.py createsuperuser

Введите Username и Password в командной строке.


Введите команду для запуска приложения:

    ● docker-compose up




[ABOUT PROGRAM]

Online directory of employees for companies.

Employee information is stored in a database and contains the following data:

    ● Full name;
    ● Position;
    ● Date of employment;
    ● Amount of wages;
    ● Information about paid salary;

Every employee must have a boss.
The hierarchical structure is also implemented, divided into the following roles:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;

The following data is displayed in the administrative panel:

    ● Full name;
    ● Position;
    ● Link to information about the boss;
    ● Salary per month;
    ● Total paid for all time;

Filters by Position and Level are implemented in the project.
    The level is the depth of nesting of our hierarchical structure or,
    in other words, how many employee roles are higher in relation to your role.


The ability to delete information about paid wages for the entire time has been implemented.
To do this, use the action methods on the Employees page.

The project also has an API with endpoints:

    ● "http://127.0.0.1:8000/api/v1/employee/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_0/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_1/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_2/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_3/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_4/"
    ● "http://127.0.0.1:8000/api/v1/profile/"
    ● "http://127.0.0.1:8000/api/token/"

These endpoints provide access to a complete list of employees and to a list of employees divided into levels.
Inside "http://127.0.0.1:8000/api/v1/employee/" there is a filter by level.

curl \
  -H "Authorization: Bearer {access}" \
  http://127.0.0.1:8000/api/token/ -  upon this request, an employee can receive complete information about himself.


However, he will first need to send a POST request to the address "http://127.0.0.1:8000/api/token/" with his
username and password in JSON format.

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://127.0.0.1:8000/api/token/

In return, you will receive:

{

  "access":"A large set of characters to be inserted into a request to obtain information about yourself.",
  "refresh":""

}

The application contains groups:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;

When a user is created on a signal, depending on the role, a group will be added to him,
this is done for the convenience of distributing access rights.


The project provides two Celery tasks:

    1. Payment of wages to employees every two hours.
    2. If all information about the payment of wages to employees is deleted,
       provided that it is necessary to delete information from more than 20 employees, the task is sent to Celery.


[REQUIREMENTS]

At the very beginning, let's build our docker containers:

    ● docker-compose build

Then we need to perform migrations with the commands:

    ● docker-compose run web python manage.py makemigrations
    ● docker-compose run web python manage.py migrate

Next, let's use another command that will create groups with the necessary rights
and 5 users, one for each role:

    ● docker-compose run web python manage.py create_group

This command demonstrates the hierarchical structure well.
However, you may need to create more users to check the health of Celery tasks, for this use the command:

    ● docker-compose run web python manage.py create_user

ПРЕДУПРЕЖДЕНИЕ!

This command does not adhere to a hierarchical structure, but simply creates 20 users.


Create superuser with the command:

    ● docker-compose run web python manage.py createsuperuser

Enter Username and Password on the command line.


Enter the command to start the application:

    ● docker-compose up


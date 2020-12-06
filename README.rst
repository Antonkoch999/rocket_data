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

Так же в проекте присутствует  API с конечными точками:

    ● "http://127.0.0.1:8000/api/v1/employee/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_0/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_1/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_2/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_3/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_4/"

Для полного списка сотрудников и для списка сотрудников разделенные на уровни.
Внутри "http://127.0.0.1:8000/api/v1/employee/" предусмотрен фильтр по уровню.


В приложении присутствуют группы:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;

Когда создается пользователь по сигналу в зависимости от роли,
ему добавится группа, сделано это для удобства распределения прав доступа.


[REQUIREMENTS]

В самом начале соберем наши контейнеры docker:

    ● docker-compose build

Затем нам необходимо выполнить миграции командами:

    ● docker-compose run web python manage.py makemigrations
    ● docker-compose run web python manage.py migrate

Далее давайте применим еще одну команду, которая создаст группы с нужными правами
и 5 пользователей по одному на каждую роль:

    ● docker-compose run web python manage.py create_group

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
    ● Employment date;
    ● Salary;
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
    The level is the depth of nesting of our hierarchical structure or otherwise
    how many employee roles are higher in relation to your role.

The ability to delete information about paid wages for the entire time has been implemented.

The project also has an API with endpoints:

    ● "http://127.0.0.1:8000/api/v1/employee/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_0/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_1/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_2/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_3/"
    ● "http://127.0.0.1:8000/api/v1/employee_level_4/"

For a complete list of employees and for a list of employees, divided into levels.
There is a level filter inside "http://127.0.0.1:8000/api/v1/employee/"

The application contains groups:

    ● Chief technical officer;
    ● Team lead;
    ● Senior;
    ● Middle;
    ● Junior;

When a user is created by signal depending on the role,
a group will be added to it, this is done for the convenience of distributing access rights.


[REQUIREMENTS]

At the very beginning, let's build our docker containers:

    ● docker-compose build

Then we need to perform migrations with the commands:

    ● docker-compose run web python manage.py makemigrations
    ● docker-compose run web python manage.py migrate

Next, let's use one more command that will create groups with the necessary rights
and 5 users, one for each role:

    ● docker-compose run web python manage.py create_group

Create superuser with the command:

    ● docker-compose run web python manage.py createsuperuser

Enter Username and Password on the command line.


Enter the command to start the application:

    ● docker-compose up

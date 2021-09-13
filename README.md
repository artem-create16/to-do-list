# To-do-list
## Description
Here you can create projects for users, create tasks for projects, edit and delete them, as well as write comments on tasks
## Installation
```
git clone https://github.com/artem-create16/to-do-list.git
cd to-do-list
```
Rename .env.example file to .env and fill all rows

create folder metathesis/application/static/uploads
```
docker-compose build
docker-compose up
```

(To populate the database with random values)

```
docker ps
docker exec -it {container id "to-do-list_db_1"} flask seed 
```
## Usage
Open http://0.0.0.0:5000/ in your browser <br />
Click "Sign up" if you want to register or "Sign in" as admin (if you use command "flask seed" login is your email from .env file, password: "123123") or as common user if you already have account <br />
On mane page you can see all projects <br />
If you are admin you can create projects. Just click "Create new project" and fill required rows. There you can select one or several users for whom this project was created <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/create-proj.png?raw=true) <br />
Then, by clicking on the name of the project and select "Create task", you can create a task for each of the selected project participants <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/create_task.png?raw=true) <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/create_task2.png?raw=true) <br />
The user you added to the project and gave the task will see it in "My Projects" -> "Tasks" <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/user_proj.png?raw=true) <br />
Also, the admin can delete and modify projects and tasks, for this click "Edit" or "Delete" then you open a project or task <br />
Regular users who are assigned a task can edit the progress <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/edit_status.png?raw=true) <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/edit_status2.png?raw=true) <br />
If you are an administrator, then you will receive a notification about the change in the progress of the task to the mail that you indicated in .env file
Users can write comments on tasks 
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/comments.png?raw=true) <br />
Click "Reply" and send your message <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/comments2.png?raw=true) <br />
Admin can control all projects, tasks and users <br />
Click "Admin" and select what you want to do <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/admin.png?raw=true) <br />
![alt text](https://github.com/artem-create16/to-do-list/blob/master/asserts/images/admin2.png?raw=true) <br />

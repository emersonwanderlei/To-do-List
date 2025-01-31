from toDoList import database

class Task(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    description = database.Column(database.String, unique=True)
    button_done = database.Column(database.String, default=False)
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '1dada2fsfsf3daf45fdfsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toDoList.db'

csrf = CSRFProtect(app)


database = SQLAlchemy(app)
app.app_context().push()

from toDoList import routes
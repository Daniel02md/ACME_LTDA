from flask_migrate import Migrate
from models.Funcionario import Funcionario
from models import db, app

migrate = Migrate(app=app, db=db, command="alembic")

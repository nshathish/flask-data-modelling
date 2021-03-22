from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/test.sqlite"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api.catalog import catalog
app.register_blueprint(catalog)

db.create_all()
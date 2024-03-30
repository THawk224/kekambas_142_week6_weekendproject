from flask import Flask # Import the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config # Import the Config class from the config module

# Create an instance of Flask called an app which will be the central object for our application
app = Flask(__name__)

# Set the cofiguration for the app to use the config class we created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Create an instance of SQLAlchemy called db which will be used to create the database
db = SQLAlchemy(app)
# Create an instance of Migrate called migrate which will be used to create the migrations
migrate = Migrate(app, db)

#basic_auth = HTTPBasicAuth()
#token_auth = HTTPTokenAuth()

#with app.app_context():
    #db.create_all()

# Run the following command to create the migration:
#flask db migrate -m "create task table";

# Run the following command to apply the migration to the database:
#flask db upgrade;

# Run the following command to create the migrations folder:
#flask db init

# Import the routes to the application and also the models 
from . import models, routes 
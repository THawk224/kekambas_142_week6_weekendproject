from datetime import datetime
from app import db
# from werkzeug.security import generate_password_hash, check_password_hash

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Task {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None
        }
    def __init__(self, title, description, completed=False, due_date=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

   # def set_password(self, password):
    #    self.password = bcrypt.generate_password_hash(password).decode('utf-8')
# What is the above function for? 
        #self.password = generate_password_hash(password)

   # def check_password(self, password):
   #     return bcrypt.check_password_hash(self.password, password)
# What is the above function for?
        #return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.email}>"

# DO I NEED TO ADD A DEF SAVE(SELF) HERE? (YES!!)
    def save(self):
        db.session.add(self)
        db.session.commit()
# Put an init method in the user and task models. Necessary for the classes. Need two. 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# I put the two methods up above, need to have it checked. Got rid of a bunch of comments that were unnecessary.
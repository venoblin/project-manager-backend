from models.db import db
from datetime import datetime, timezone 
from utils import update_self
from models.event import Event
from sqlalchemy import desc

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    git_url = db.Column(db.String(255), nullable=False)
    is_private = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False, onupdate=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='projects')
    todos = db.relationship('Todo', cascade='all', back_populates='project')
    bugs = db.relationship('Bug', cascade='all', back_populates='project')
    events = db.relationship('Event', cascade='all', back_populates='project', order_by=desc(Event.created_at))
    contributors = db.relationship('Contributor', cascade='all', back_populates='project')
    notifications = db.relationship('Notification', cascade='all', back_populates='project')

    def __init__(self, name, git_url, is_private, owner_id):
        self.name = name
        self.git_url = git_url
        self.is_private = is_private
        self.owner_id = owner_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'git_url': self.git_url,
            'is_private': self.is_private,
            'owner_id': self.owner_id
        }
    
    def get_id(self):
        return self.id
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def update(self, update):
        update_self(self, update)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(self):
        return Project.query.all()
    
    @classmethod
    def find_by_id(self, id):
        return db.get_or_404(self, id, description=f'Project with id: {id} not found!')
    
    @classmethod
    def delete_by_id(self, id):
        project = self.find_by_id(id)
        db.session.delete(project)
        db.session.commit()
        return f'Successfully deleted project with id: {id}'
    
    @classmethod
    def find_from_user_by_name(self, name, owner_id):
        return Project.query.filter(Project.name == name, Project.owner_id == owner_id).first()

from models.db import db
from datetime import datetime
from utils import update_self

class Contributer(db.Model):
  __tablename__ = 'contributers'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

  def __init__(self, user_id, project_id):
    self.user_id = user_id
    self.project_id = project_id

  def json(self):
    return {
      'user_id': self.user_id,
      'project_id': self.project_id
    }
  
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
    return Contributer.query.all()
    
  @classmethod
  def find_by_id(self, id):
    return db.get_or_404(self, id, description=f'Contributer with id: {id} not found!')
    
  @classmethod
  def delete_by_id(self, id):
    Contributer = self.find_by_id(id)
    db.session.delete(Contributer)
    db.session.commit()
    return f'Successfully deleted Contributer with id: {id}'


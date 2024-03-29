from flask import request
from middleware import create_token, hash_password, strip_token, read_token, check_password
from models.user import User

def register_user():
  data = request.get_json()
  params = {
    'username': data['username'],
    'name': data['name'],
    'email': data['email'],
    'password': hash_password(data['password'])
  }
  user = User(**params)
  user.create()
  return user.json(), 201

def login_user():
  data = request.get_json()
  user = User.find_by_email(data['email'])
  isVerified = check_password(data['password'], user.password)

  if isVerified:
    payload = {
      'id': user.id,
      'name': user.name,
      'username': user.username,
      'email': user.email
    }
    token = create_token(payload)
    return {
      'user': payload,
      'token': token
    }
  
  return {'error': 'Email or password invalid!'}, 400

def check_session():
  token = strip_token(request)
  payload = read_token(token)
  return payload
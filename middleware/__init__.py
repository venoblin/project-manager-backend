import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET')

def create_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def read_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.InvalidSignatureError:
        return 'Signature invalid'
    except jwt.InvalidTokenError:
        return 'Token invalid'
    
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def strip_token(req):
    try:
        token = req.headers['authorization'].split(' ')[1]
        return token
    except:
        return None
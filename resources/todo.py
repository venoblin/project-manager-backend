from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.todo import get_all_todos, post_todo, get_single_todo, delete_single_todo, patch_single_todo

class Todos(Resource):
    def get(self):
        return handle_request(request, get_all_todos)
    
    def post(self):
        return handle_request(request, post_todo)
    
class SingleTodo(Resource):
    def get(self, id):
        return handle_request(request, lambda: get_single_todo(id))
    
    def delete(self, id):
        return handle_request(request, lambda: delete_single_todo(id))
    
    def patch(self, id):
        return handle_request(request, lambda: patch_single_todo(id))
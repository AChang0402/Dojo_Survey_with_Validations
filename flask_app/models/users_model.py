from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.webfund = data['webfund']
        self.python = data['python']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        print(data)
        query = "INSERT INTO users (name, location, language, comment, webfund, python) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,%(webfund)s,%(python)s);"
        print(query)
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid
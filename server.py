from flask import Flask, request
from flask.ext.jsonify import jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite://chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to the DB
        query = conn.execute("select * from employees") # executes SQL query and returns result in JSON
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect() # connect to the DB
        query = conn.execute("select trackid, name, composer, unitprice from tracks") # executes SQL query and returns result in JSON
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]} # fetches first column that is Employee ID
        return jsonify(result)

class Employee_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect() # connect to the DB
        query = conn.execute("select * from employees where EmployeeID = %d " %int(employee_id)) # executes SQL query and returns result in JSON
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]} # fetches first column that is Employee ID
        return jsonify(result)

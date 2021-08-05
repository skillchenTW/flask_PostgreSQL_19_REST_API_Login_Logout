from flask import Flask, jsonify, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import timedelta


import psycopg2
import psycopg2.extras


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SkillChen-Secret_Key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
CORS(app)

DB_HOST = 'localhost'
DB_PORT = '5433'
DB_USER = 'postgres'
DB_PASS = 'dba'
DB_NAME = 'sampledb'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host= DB_HOST, port= DB_PORT)

@app.route("/")
def home():
    # passhash = generate_password_hash('aq')
    # print(passhash)
    if 'username' in session:
        username = session['username']        
        return jsonify({'message': 'You are already logged in', 'username': username})
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp 
        

@app.route("/login", methods=['POST'])
def login():
    _json = request.json
    _username = _json['username']
    _password = _json['password']
    print(_password)
    # validate the received value
    if _username and _password:
        # check user exists
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from useraccount where username=%s"
        sql_where = (_username,)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        username = row['username']
        password = row['password']
        if row:
            if check_password_hash(password, _password):
                session['username'] = username
                cursor.close()
                return jsonify({'message':'You are logged in successfully'})
            else:
                resp = jsonify({'message': 'Bad Request - invalid password!'})
                resp.status_code = 400
                return resp
    else:
        resp = jsonify({'message': 'Bad Request - invalid credendtials'})
        resp.status_code = 400
        return resp


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message':'You successfully logged out!'})

if __name__ == '__main__':
    app.run()
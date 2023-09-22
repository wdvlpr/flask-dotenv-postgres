#Autor: Fabio Camara

from flask import Flask, request, jsonify

import os
from dotenv import load_dotenv
load_dotenv('.env')

app = Flask(__name__)

import psycopg2
from psycopg2.extras import RealDictCursor

# Connect to the database
def get_db_connection():
    conn = psycopg2.connect(database=os.environ.get("DATABASE"), 
                            user=os.environ.get("USER"),
                            password=os.environ.get("PASSWORD"), 
                            host=os.environ.get("HOST"), 
                            port=os.environ.get("PORT"))
    return conn

@app.route('/')
def index():
    headers = request.headers
    auth = headers.get("A-Api-Key")
    if auth == 'asdewq321098':
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT NOME, LOGIN FROM USUARIOS;')
        usuarios = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(usuarios), 200
    else:
        return jsonify({"message":"ERROR: A-Api-Key invalido"}), 401

if __name__ == '__main__':
   app.run()

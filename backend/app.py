from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

DATABASE = {
    'dbname': 'counterdb',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'terraform-20240720103041771800000001.chggkk66uebv.us-east-1.rds.amazonaws.com', # replace with RDS endpoint once provisioned
    'port': '5432'
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS counter (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO counter (count) VALUES (0)
        ON CONFLICT DO NOTHING
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/api/counter', methods=['GET'])
def get_counter():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT count FROM counter WHERE id = 1')
    counter = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"counter": counter['count']})

@app.route('/api/increment', methods=['POST'])
def increment_counter():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('UPDATE counter SET count = count + 1 WHERE id = 1 RETURNING count')
    counter = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"counter": counter['count']})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
    


#### TEST ####
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(port=5000)
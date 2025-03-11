from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            dbname="flaskdb",
            user="flaskuser",
            password="postgres",
            host="postgres"
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

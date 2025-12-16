from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_db_connection
import hashlib

app = Flask(__name__)
app.secret_key = 'mi_secreto'

@app.route('/')
def home():
    return redirect(url_for('dashboard'))  # abre directo dashboard

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ignite')
def ignite():
    return render_template('ignite.html')

@app.route('/ejemplo')
def ejemplo():
    return render_template('ejemplo.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s,%s)",
            (username, password)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/suscribirse', methods=['POST'])
def suscribirse():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO suscriptores (nombre, apellido, correo)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, apellido, correo))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',   # IPv4
        port=5000,        # puerto estándar Flask
        debug=True
    )




from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, request, abort
from dotenv import load_dotenv
from page_analyzer import utils, db
import os
import psycopg2
from werkzeug.exceptions import BadRequest




load_dotenv() 
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE')
conn = psycopg2.connect(DATABASE_URL)


@app.route("/")
def index():
    url = {"name": ""}
    errors = {}
    return render_template("index.html", url=url, errors=errors)

@app.route('/process_url', methods=['POST'])
def process_url():
    return redirect(url_for('test'))

@app.route('/urls', methods=['POST'])
def add_url():
    cursor = conn.cursor()
    urls = str(request.form.get('url'))
    if not utils.validate(urls):
        return BadRequest('Invalid URL')
    cursor.execute('INSERT INTO urls (name) VALUES (%s);', (urls,))
    cursor.close()
    conn.commit()
    return redirect(url_for('show_urls'))

@app.route('/urls')
def show_urls():
    conn = db.connect_db()
    urls = db.get_all_urls(conn)
    return render_template('show.html', urls=urls)

@app.route('/urls/<int:id>')
def show_url(id):
    if id < len(urls):
        return urls[id]
    else:
        flash('Некорректный URL', 'error')
        return render_template('show.html')

@app.route('/urls/<int:url_id>/checks', methods=['POST'])
def check_url(url_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO url_checks (url_id) VALUES (%s) RETURNING id", (url_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('show_url', id=url_id))



    




if __name__ == "__main__":
    app.run(debug=True)
        
    


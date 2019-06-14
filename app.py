import sqlite3
from bs4 import BeautifulSoup
import requests
from flask import Flask, redirect, url_for, request, jsonify, render_template

# import os
# from flask import Flask, render_template, request, current_app
# from flask_pager import Pager
# app = Flask(__name__)
# app.secret_key = os.urandom(42)
# app.config['PAGE_SIZE'] = 20
# app.config['VISIBLE_PAGE_COUNT'] = 10
#
# word = "sdasd"
# @app.route("/")
# def index():
#     page = int(request.args.get('page', 1))
#     count = 300
#     data = range(count)
#     pager = Pager(page, count)
#     pages = pager.get_pages()
#     skip = (page - 1) * current_app.config['PAGE_SIZE']
#     limit = current_app.config['PAGE_SIZE']
#     data_to_show = data[skip: skip + limit]
#     return render_template('index.html', pages=pages, data_to_show=data_to_show)
#
#
#
# app.run(debug = True,host='localhost', port=8080)


conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE JOBS
#                   (id, job_name)
#                """)


source = requests.get('https://www.jobs.ge/?page=1&q=&cid=6&lid=&jid=').text
soup = BeautifulSoup(source, 'html.parser')
num = 0
rating = 1
albums = []

# for genre in soup.find_all('a', class_='vip'):
#     albums.append(('{}'.format(genre.text)))
#
# for each in range(len(albums)):
#     params = (each, albums[each])
#     cursor.execute('insert into JOBS values(?,?)', params)
#
# conn.commit()

cursor.execute("SELECT * FROM JOBS")
print("fetchall:")
result = cursor.fetchall()
out = []
for r in result:
    out.append(r)
    print(r)

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html', title=out)




app.run(debug = True,host='localhost', port=8080)

import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

app=Flask(__name__)

app.config.update(dict(
    DATABASE='/tmp/flaskr.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

def connect_db():
  conn = sqlite3.connect(app.config['DATABASE'])
  conn.row_factory = sqlite3.Row
  return conn

def get_db():
  if not hasattr(g,'sqlite_db'):
    g.sqlite_db=connect_db()
  return g.sqlite_db

def init_db():
  with app.app_context():
    db=get_db()
    with app.open_resource('schema.sql',mode='r') as f:
      db.cursor.executescript(f.read())
    db.commit()

@app.route('/')
def show_entries():
  cur=g.db.execute('selct title,text from ')


if  __name__ =='__main__':
  app.run()
  init_db()
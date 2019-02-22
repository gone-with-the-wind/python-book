from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello_world'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
      return request.args.get('aaaa', '111')

if __name__=='__main__':
  app.debug=True
  app.run()
from flask import Flask
from flask import request
from flask import send_from_directory,redirect, url_for
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = './images/aaa'

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['fileupload']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("path:%s"  % os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__=='__main__':
  app.debug=True
  app.run()
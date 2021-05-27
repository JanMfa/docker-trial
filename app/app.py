from os import replace, stat
from flask import Flask, request,send_file,flash, send_from_directory, safe_join, abort, jsonify, render_template, url_for, redirect
import sqlite3
import json
from pprint import pprint
from werkzeug.utils import secure_filename
import re
import os
from pathlib import Path

UPLOAD_FOLDER = 'Resources'
FILENAME='Dango.png'
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
APP_FOLDER=os.path.abspath(os.path.join(os.path.dirname( __file__ )))
print(APP_ROOT)
print(APP_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

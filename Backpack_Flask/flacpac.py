#21/2/2020 Jayden L Backpack with Flask
from flask import Flask, flash, render_template, request, redirect, g
import sqlite3, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Backpack_Flask/static/pictures'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'AWUBFAUIWBFAWUFAFNASAFCAW'

DATABASE = 'FlaskPack.db'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db():
    #get database from SQlite
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM flaskpac"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        #get the item and add to database
        cursor = get_db().cursor()
        new_picture = request.form["item_picture"]
        new_name = request.form["item_name"]
        new_description = request.form["item_description"]
        sql = "INSERT INTO flaskpac(name,description,picture) VALUES (?,?,?)"
        cursor.execute(sql,(new_name,new_description,new_picture,))
        get_db().commit()

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return redirect('/')

@app.route('/delete', methods=["GET","POST"])
def delete():
    if request.method == "POST":
        #get the item and delete from database
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM flaskpac WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'dont tell no one'

@app.route('/')
def index():
    flash('how you doing you freak)
    return redirect(url_for('example'))

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == '__main__':
    app.run(debug=True)
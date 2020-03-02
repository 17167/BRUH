from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Suhhhhh<h1>'

@app.route('/something/<place>')
def something(place):
    return '<h1>You are on the ' + place + ' page!<h1>'

@app.route('/home', methods = ['GET', 'POST'])
def home():
    links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.schoology.com']
    return render_template('example.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
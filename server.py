from turtle import color
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def page_two():
     return render_template("index2.html")

if __name__ == '__main__':
  app.run(debug=True)
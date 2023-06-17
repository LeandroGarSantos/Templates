from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA', 'language': 'English'},
    'Bob': {'age': 30, 'country': 'BR', 'language': 'Portuguese'},
    'Charlie': {'age': 35, 'country': 'JP', 'language': 'Japanese'}
} 

@app.route('/')
def index():
    title = "My Page"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.args.get('name')  # Extract the 'name' parameter from the query string
    return render_template('index.html', title=title, name=name, users=users, current_time=current_time)
    

@app.route('/form')
def form():
  return render_template('form.html')

@app.route('/all-users')
def all_users():
    return render_template('all_users.html', users=users)

@app.route('/greet/<name>')
def greet(name):
    name = request.args.get('name', 'Guest')  # Use 'Guest' as default value if no 'name' parameter is provided
    return render_template('greet.html', title='Home', name=name)

@app.route('/square/<int:number>')
def square(number):
    square_value= number * number
    return f"The square of {number} is {square_value}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

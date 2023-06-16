from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
} 

@app.route('/')
def index():
    title = "My Page"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # name = request.args.get('name')  # Extract the 'name' parameter from the query string
    return render_template('index.html', title=title, users=users, current_time=current_time)

@app.route('/form')
def form():
  return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

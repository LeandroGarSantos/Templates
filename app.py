from flask import Flask, render_template, request, redirect
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


@app.route('/update-country',methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form.get('name')
        country = request.form.get('country')
        language = request.form.get('language')
        if name in users:
            users[name]['country'] = country
            users[name]['language'] = language
        return redirect('/all-users')
    else:
        return render_template ('update_country.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

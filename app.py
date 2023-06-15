from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    title = "My Page"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', title=title, name='Alice', current_time=current_time)

@app.route('/from')
def form():
  return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
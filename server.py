from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/4af156202f984d3464c3'
    response = requests.get(blog_url)
    current_year = dt.datetime.now().year
    return render_template('index.html', year=current_year, all_posts=response.json())


@app.route('/blog_id')
def blog():
    blog_url = 'https://api.npoint.io/4af156202f984d3464c3'
    response = requests.get(blog_url)
    render_template('post.html', all_posts=response.json())


if __name__ == '__main__':
    app.run(debug=True)

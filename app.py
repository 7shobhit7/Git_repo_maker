from flask import Flask, request, render_template
from git_push import push_to_github  # Import your Python script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    github_username = request.form['githubUsername']
    repo_name = request.form['githubRepo']
    github_token = request.form['githubToken']

    # Call your Python script with the obtained values
    result = push_to_github(github_username, repo_name, github_token)

    return result  # You can return a response to the user here

if __name__ == '__main__':
    app.run()

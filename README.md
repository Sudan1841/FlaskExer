# FlaskExer
this is exercise  for flask app


Below are the steps to create a simple note-taking app using Flask. This example will use an in-memory list to store notes. In a production application, you would likely want to use a database to persist the notes.

Step 1: Set Up the Project
Open your terminal or Git Bash and navigate to the desired directory:

bash
Copy code
mkdir flask_note_app
cd flask_note_app
Step 2: Initialize a Virtual Environment and Install Flask
bash
Copy code
virtualenv .venv
source .venv/bin/activate  # On Windows, use ".venv\Scripts\activate"
pip install flask
Step 3: Create the "src" Directory and Navigate Inside
bash
Copy code
mkdir src
cd src
Step 4: Create the "app" Package
bash
Copy code
mkdir app
cd app
Step 5: Create the "init.py" File
Use a text editor to create the __init__.py file inside the app directory:

python
Copy code
from flask import Flask

app = Flask(__name__)

from app import routes
Step 6: Create the "routes.py" File
Use a text editor to create the routes.py file inside the app directory:

python
Copy code
from flask import render_template, request, redirect, url_for
from app import app

notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect(url_for('index'))
Step 7: Create a "templates" Folder
Inside the app directory, create a folder named templates. This is where Flask will look for HTML templates.

bash
Copy code
mkdir templates
Step 8: Create the "index.html" Template
Use a text editor to create the index.html file inside the templates directory:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Note Taking App</title>
</head>
<body>
    <h1>Note Taking App</h1>

    <form action="{{ url_for('add_note') }}" method="post">
        <label for="note">Add Note:</label>
        <input type="text" id="note" name="note" required>
        <button type="submit">Add</button>
    </form>

    <h2>Notes:</h2>
    <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
    </ul>
</body>
</html>
Step 9: Set the "FLASK_APP" Environment Variable
Back in the src directory, set the FLASK_APP environment variable:

bash
Copy code
export FLASK_APP=app
Step 10: Run the Flask App
bash
Copy code
flask run
Visit http://127.0.0.1:5000 in your browser to see and use your note-taking app. You can add notes using the form, and they will be displayed on the page.

This is a basic example, and in a real-world scenario, you might want to enhance the application's functionality, add user authentication, and use a database to store notes persistently.

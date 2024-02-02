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

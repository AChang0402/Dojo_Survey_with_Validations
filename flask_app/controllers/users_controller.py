from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    if not User.validate_form(request.form):
        return redirect('/')
    
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }

    if 'webfund' in request.form:
        data['webfund']=request.form['webfund']
    else:
        data['webfund']=""
    if 'python' in request.form:
        data['python']=request.form['python']
    else:
        data['python']=""

    new_user_id = User.create_user(data)

    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    session['checkedboxes']=[]
    if 'webfund' in request.form:
        session['checkedboxes'].append(request.form['webfund'])
    if 'python' in request.form:
        session['checkedboxes'].append(request.form['python'])

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('submitted.html')
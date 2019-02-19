from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    posts = [
        {
            'author': {'username': 'Venediktov'},
            'body': 'Выходим на улицу'
        },
        {
            'author': {'username': 'Navalny'},
            'body': 'Пора скинуть Пыню'
        },
        {
            'author': {'username': 'Tolokonnikova'},
            'body': '''Страна идёт, страна идёт на улицу с дерзостью!
                     Страна идёт, страна идёт прощаться с режимом!
                     Страна идёт, страна мдёт феминистким клином!
                     А Путин идёт, а Путин идёт прощаться скотом!'''
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts) 

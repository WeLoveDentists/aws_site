from app import app,models
import random
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Hiro'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Rod'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Shriya'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/tester')
def tester():
  user = {'nickname': 'Hiro'}  # fake user
  inventions_timeline_with_image_links = models.Inventions_timeline_with_image_links.query.all()
  num_available_rows = len(inventions_timeline_with_image_links)
  num_output_rows = 4
  random_row_indices = [random.randint(1,num_available_rows) for i in range(num_output_rows)]
  rows = []
  for i in random_row_indices:
    rows.append(inventions_timeline_with_image_links[i])
  return render_template("rows_endpoint.html",
                          title ='rows_endpoint',
                          user = user,
                          rows = rows)

 




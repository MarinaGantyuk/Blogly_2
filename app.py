"""Blogly application."""

from flask import Flask,render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, User, Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
#db.init_app(app)   
with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    return redirect('/users')


@app.route('/users')
def users_page():
    users = db.session.execute(db.select(User)).scalars()
    return render_template('home.html', users = users)

@app.route('/users/<int:id>')
def user_detail(id):
    user = db.get_or_404(User,id)
    posts = Post.query.filter_by(user_id = user.id).all()
    return render_template('user_detail.html', user = user, posts = posts)

@app.route('/users/new', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        user = User( 
            #id = num(request.form['id']),
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            image_url = request.form['image_url']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/users/' + str(user.id))

    return render_template('user_addform.html')

@app.route('/users/<int:id>/delete', methods=['POST','GET'])
def delete_user(id):
    user=db.get_or_404(User, id)
    if request.method=='POST':
        db.session.delete(user)
        db.session.commit()

    return redirect('/users')

@app.route('/users/<int:id>/edit', methods=['POST', 'GET'])
def edit_user(id):
    user=db.get_or_404(User, id)
    if request.method == 'POST':

        user.first_name = request.form['first_name'],
        user.last_name = request.form['last_name'],
        user.image_url = request.form['image_url']
        user.veryfied = True
        db.session.commit()
        return redirect('/users/' + str(user.id))

    return render_template('user_editform.html', user=user)

@app.route('/users/<int:id>/posts/new', methods=['POST', 'GET'])
def post_user(id):
    user=db.get_or_404(User, id) 
    if request.method == 'POST':
        post = Post( 
            title = request.form['title'],
            content = request.form['content'],
            user_id = user.id
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/users/' + str(user.id))

    return render_template('post_addform.html', user=user)

@app.route('/posts/<int:id>')
def post_detail(id):
    post = db.get_or_404(Post,id)
    user = db.get_or_404(User,post.user_id)
    return render_template('post_detail.html', post = post, user = user)

@app.route('/posts/<int:id>/edit', methods=['POST', 'GET'])
def edit_post(id):
    post=db.get_or_404(Post, id)
    if request.method == 'POST':

        post.title = request.form['title'],
        post.content = request.form['content'],
        post.veryfied = True
        db.session.commit()
        return redirect('/posts/' + str(post.id))

    return render_template('post_editform.html', post = post)

@app.route('/posts/<int:id>/delete', methods=['POST','GET'])
def delete_post(id):
    post=db.get_or_404(Post, id)
    if request.method=='POST':
        db.session.delete(post)
        db.session.commit()

    return redirect('/users/' + str(post.user_id))














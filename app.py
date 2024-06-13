import click
from flask import Flask, render_template, redirect, url_for, flash
from flask.cli import with_appcontext
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
from config import Config
from models import db, login_manager, User, LostProperty
from forms import LoginForm, LostPropertyForm
from admin import setup_admin

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

setup_admin(app, db)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/lost_property', methods=['GET', 'POST'])
def lost_property():
    form = LostPropertyForm()
    if form.validate_on_submit():
        photo_filename = None
        if form.photo.data:
            photo_filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join('static', 'uploads', photo_filename))

        lost_property = LostProperty(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            description=form.description.data,
            photo=photo_filename
        )
        db.session.add(lost_property)
        db.session.commit()
        flash('Lost property submitted successfully', 'success')
        return redirect(url_for('index'))
    return render_template('lost_property_form.html', form=form)


@click.command(name='create-user')
@click.argument('username')
@click.argument('password')
@with_appcontext
def create_user(username, password):
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    click.echo(f'User {username} created successfully.')


app.cli.add_command(create_user)

if __name__ == '__main__':
    app.run(debug=True)

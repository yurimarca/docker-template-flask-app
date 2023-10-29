from flask import Blueprint, render_template, request, flash, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm_password')

        print(email, password1, password2)

        if len(email) < 4:
            print("Email must be greater than 4 characters.")
            flash("Email must be greater than 4 characters.", category='error')
        elif len(password1) < 7:
            print("Password must be greater than 7 characters.")
            flash("Password must be greater than 7 characters.", category='error')
        elif password1 != password2:
            print("Passwords don't match.")
            flash("Passwords don't match.", category='error')
        else:
            # TODO: add user to database
            new_user_hash = str(generate_password_hash(password1, method='sha256'))
            print(f"new_user_hash = {new_user_hash}")

            flash("Account created!", category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")

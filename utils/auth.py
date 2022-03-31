import bcrypt

import functools

from flask import render_template, session, flash, redirect


def logged_in(page_type):
    """Decorator to check if user is logged in. You are logged in if you have logged_in as True in your session"""
    def inner_function(flask_route):

        @functools.wraps(flask_route)
        def wrapper(*args, **kwargs):
            if "logged_in" in session:
                if session.get("logged_in"):
                    return flask_route()
            return render_template("not_logged_in.html", page_type=page_type)

        return wrapper

    return inner_function

def check_access(access_level, redirect_if_no_access="/", flash_message: str = "You don't have access to this page", flash_type="info"):
    """Decorator that checks if your auth level is high enough. The level is read by reading auth_level in the session"""
    def inner_function(flask_route):

        @functools.wraps(flask_route)
        def wrapper(*args, **kwargs):
            if "auth_level" in session:
                auth_level = session.get("auth_level", 0)
                if auth_level < access_level:
                    flash(flash_message, flash_type)
                    return redirect(redirect_if_no_access)
            else:
                flash("Je have to login to do this", "info")
                return redirect(redirect_if_no_access)
            return flask_route()
        return wrapper
    return inner_function


def check_password(password: str, salt: str, password_hash: str) -> bool:
    """Check a password with a salt and password hash"""
    salted_password = password + salt
    password_hash = password_hash.encode()
    if bcrypt.check_password_hash(password_hash, salted_password):
        return True
    else:
        return False


def generate_salt() -> str:
    """Get a salt from bcrypt"""
    return bcrypt.gensalt().decode("utf-8")


def generate_password_hash(password, salt) -> str:
    """Generate a hash with bcrypt from a password and a salt"""
    salted_password = password + salt
    hashed_passsword = bcrypt.generate_password_hash(salted_password, 9)
    hashed_passsword = hashed_passsword.decode()
    return hashed_passsword


def generate_password_data(password) -> dict:
    """Generate a dictionary with a hash and salt based on the password"""
    password_data = {}
    salt = generate_salt()
    hashed_password = generate_password_hash(password, salt)
    password_data["hash"] = hashed_password
    password_data["salt"] = salt
    return password_data


def check_password_with_dict(password, password_data) -> bool:
    """Check a password with a dictionary that has "salt" and "hash" as keys for input"""
    salt = password_data.get("salt")
    pass_hash = password_data.get("hash")
    return check_password(password, salt, pass_hash)


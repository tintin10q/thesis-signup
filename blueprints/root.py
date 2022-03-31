from flask import Blueprint, render_template, request, redirect, flash

root_blueprint = Blueprint('main', __name__)


@root_blueprint.route("/", methods=["GET"])
def root_post():
    return render_template("root.html")


@root_blueprint .route("/", methods=["POST"])
def root_get():
    return render_template("root.html")

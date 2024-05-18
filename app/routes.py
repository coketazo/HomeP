from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .easymd import markdown_files_to_html_dict

main = Blueprint("main", __name__)


@main.route("/")
def index():
    sections_html = markdown_files_to_html_dict("index")
    return render_template("index.html", sections=sections_html)


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.username)

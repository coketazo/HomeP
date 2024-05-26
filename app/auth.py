# 사용자의 계정을 관리합니다
# db는 <project_name>/instance/site.db 에 생성됩니다
# 비밀번호는 sha:256으로 암호화 합니다
from flask import Blueprint, render_template, redirect, url_for, flash, request
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import login_manager

auth = Blueprint("auth", __name__, url_prefix="/auth")


# IMPORTANT
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# @login_required에 걸렸을 경우 실행
@login_manager.unauthorized_handler
def handle_needs_login():
    flash("로그인이 필요합니다")
    return redirect(url_for("auth.login", next=request.endpoint))


# 로그인
@auth.route("/login", methods=["GET", "POST"])
def login():
    next = request.args.get("next", default=url_for("main.index"))
    if request.method == "POST":
        # form_dict = request.form.to_dict()
        # print(form_dict)
        email = request.form.get("email")
        password = request.form.get("password")
        next = request.form.get("next", default=next)

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(next)
        else:
            print("failed login")
            flash("로그인 실패하였습니다. 이메일과 비밀번호를 다시 확인해주세요.")
    return render_template("login.html", next=next)


# 회원가입
@auth.route("/register", methods=["GET", "POST"])
def register():
    next = request.args.get("next", default=url_for("main.index"))
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        next = request.form.get("next", default=next)

        user = User.query.filter_by(email=email).first()
        if user:
            flash("이메일이 이미 가입되어있습니다")
            return redirect(url_for("auth.register", next=next))

        # User 생성
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password, method="pbkdf2:sha256"),
        )

        # DB에 User 추가
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(next)

    return render_template("register.html", next=next)


# 로그아웃
@auth.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for("main.index"))

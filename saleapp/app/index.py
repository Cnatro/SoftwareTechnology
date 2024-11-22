import math
from plistlib import dumps

from flask import render_template, request, redirect
from flask_login import login_user, logout_user
from app import app, login
import dao
from app.dao import add_user


# content page
@app.route("/")
def index():
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    page = request.args.get('page', 1)

    page_size = app.config['PAGE_SIZE']
    total = dao.count_product()
    product = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))
    return render_template('index.html', products=product, pages=math.ceil(total / page_size))


# login
@app.route("/login", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        # data = request.form.copy()
        username = request.form.get('username')
        password = request.form.get('password')

        user_login = dao.auth_user(username=username, password=password)
        if user_login:
            login_user(user_login)
            return redirect('/')

    return render_template('login.html')


# user login
@login.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


# logout
@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')


# register
@app.route("/register", methods=['get', 'post'])
def register_process():
    err_msg = None
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm_password = request.form.get('confirm')

        if password.__eq__(confirm_password) :

            data = request.form.copy()
            # print(data)
            del data['confirm']

            avatar = request.files.get('avatar')
            dao.add_user( avatar= avatar,**data)

            return redirect("/login")
        else:
            err_msg = "Password not success"

    return render_template('register.html', err_msg=err_msg)


@app.context_processor
def common_context_params():
    return {
        'categories': dao.load_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)

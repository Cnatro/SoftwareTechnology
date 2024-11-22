import math
from flask import render_template, request, redirect
from flask_login import login_user,logout_user

from app import app, login
import dao


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    page = request.args.get('page', 1)

    page_size = app.config['PAGE_SIZE']
    total = dao.count_product()
    product = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))
    return render_template('index.html', categories=cates, products=product, pages=math.ceil(total / page_size))


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

@login.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)

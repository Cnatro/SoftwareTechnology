import math

from flask import render_template, request, redirect, session,jsonify
from flask_login import login_user, logout_user
from app import app, login,utils
import dao
from app.models import UserRole


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


@app.route('/login-admin',methods=['POST'])
def login_admin_process():
    if request.method.__eq__('POST'):
        # data = request.form.copy()
        username = request.form.get('username')
        password = request.form.get('password')

        user_login = dao.auth_user(username=username, password=password,role=UserRole.ADMIN)
        if user_login:
            login_user(user_login)
    return redirect('/admin')


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

        if password.__eq__(confirm_password):

            data = request.form.copy()
            # print(data)
            del data['confirm']

            avatar = request.files.get('avatar')
            dao.add_user( avatar=avatar,**data)

            return redirect("/login")
        else:
            err_msg = "Password not success"

    return render_template('register.html', err_msg=err_msg)


@app.route("/api/carts",methods=['post'])
def add_to_cart():
    cart = session.get('cart')
    if not cart:
        cart = {}

    id = str(request.json.get('id'))
    name = request.json.get('name')
    price = request.json.get('price')

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id" : id,
            'name':name,
            'price':price,
            'quantity':1
        }
    session['cart'] = cart
    print(cart)
    return jsonify(utils.stats_cart(cart))


@app.route('/carts')
def carts():
    return render_template('cart.html')

@app.context_processor
def common_context_params():
    return {
        'categories': dao.load_categories(),
        'cart_stats': utils.stats_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)

import hashlib
import cloudinary.uploader
from app.models import Category,Product, User,Receipt,ReceiptDetails
from app import app, db
from flask_login import current_user
from flask import session

def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id=None, kw=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
       query = query.filter(Product.category_id == cate_id)

    # create pagination
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    query = query.slice(start, start + page_size)
    return query.all()


def count_product():
    return Product.query.count()


def auth_user(username , password,role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User.query.filter( User.username.__eq__(username),
                              User.password.__eq__(password))
    if role:
        u = u.filter(User.user_role.__eq__(role))
    return u.first()

def get_user_by_id(user_id):
    return User.query.get(user_id)


def add_user(fullname,username,password,avatar=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=fullname, username=username, password= password, avatar = avatar)

    # get avatar form cloud
    if avatar :
        res = cloudinary.uploader.upload(avatar)
        user.avatar = res.get('secure_url')

    db.session.add(user)
    db.session.commit()


def add_receipt(cart):
    if cart:
        r = Receipt(user=current_user)
        db.session.add(r)

        for c in cart:
            d = ReceiptDetails(quantity=c['quantity']
                               ,unit_price=c['price']
                               ,receipt=r
                               ,product_id=c['id'])
            # print(d)
            db.session.add(d)
        # db.session.commit()


# if __name__ == '__main__':
#    # print(add_receipt(session.get('cart')))
# def load_categories():
#     return [{
#         "id": 1,
#         "name": "Mobile"
#     },
#         {
#             "id": 2,
#             "name": "Tablet"
#         },
#         {
#             "id": 3,
#             "name": "Laptop"
#         }
#     ]
# def load_products():
#     return [{
#         "id": 1,
#         "name": "iPhone 7 Plus",
#         "description": "Apple, 32GB, RAM: 3GB, iOS13",
#         "price": 17000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
#         "category_id": 1
#     }, {
#         "id": 2,
#         "name": "iPad Pro 2020",
#         "description": "Apple, 128GB, RAM: 6GB",
#         "price": 37000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
#         "category_id": 2
#     }, {
#         "id": 3,
#         "name": "Galaxy Note 10 Plus",
#         "description": "Samsung, 64GB, RAML: 6GB",
#         "price": 24000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
#         "category_id": 1
#     }, {
#         "id": 4,
#         "name": "iPhone 7 Plus",
#         "description": "Apple, 32GB, RAM: 3GB, iOS13",
#         "price": 17000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
#         "category_id": 1
#     }, {
#         "id": 5,
#         "name": "iPad Pro 2020",
#         "description": "Apple, 128GB, RAM: 6GB",
#         "price": 37000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
#         "category_id": 2
#     }, {
#         "id": 6,
#         "name": "Galaxy Note 10 Plus",
#         "description": "Samsung, 64GB, RAML: 6GB",
#         "price": 24000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
#         "category_id": 1
#     }, {
#         "id": 7,
#         "name": "iPad Pro 2020",
#         "description": "Apple, 128GB, RAM: 6GB",
#         "price": 37000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
#         "category_id": 2
#     }, {
#         "id": 8,
#         "name": "Galaxy Note 10 Plus",
#         "description": "Samsung, 64GB, RAML: 6GB",
#         "price": 24000000,
#         "image":
#             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
#         "category_id": 1
#     }]

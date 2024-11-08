from app.models import Category,Product
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
def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id=None, kw=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
       query = query.filter(Product.category_id == cate_id)

    return query.all()


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

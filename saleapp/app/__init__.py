from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app=Flask(__name__)
app.secret_key = 'sdhfsjdhfsuhfdsu#%$%$^%'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4" %quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 8

cloudinary.config(
    cloud_name = "dzwjtcby7",
    api_key = "954977464151683",
    api_secret = "C9maHjelNjdF-fjnFizEiqAPac8", # Click 'View API Keys' above to copy your API secret
    secure=True
)
db = SQLAlchemy(app)
login = LoginManager(app)
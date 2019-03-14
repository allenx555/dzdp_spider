from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db = SQLAlchemy(app)

from dzdp_spider.spider.models import Shop
db.create_all()


import dzdp_spider.spider.spider
dzdp_spider.spider.spider.main()

from dzdp_spider import db
import time


class Shop(db.Model):
    __tablename__ = 'shops'

    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40))
    href = db.Column(db.String(60))
    star = db.Column(db.String(20))
    date = db.Column(db.String(30))

    def save(self, args):
        self.id = args['id']
        self.name = args['name']
        self.href = args['href']
        self.star = args['star']
        self.date = time.strftime("%Y-%m-%d", time.localtime())

        db.session.add(self)
        db.session.commit()
